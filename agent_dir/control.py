import time
import threading
from utils.Logger import ExperimentLogger
from agent_dir.utils.ControlManager import ControlManager

class Control:
    def __init__(self, folder, communication, prompting, get_events, get_belief_set):
        self.communication = communication
        self.stop = False
        self.alive = [True]
        self.get_events = get_events
        self.get_belief_set = get_belief_set
        self.logger = ExperimentLogger(folder, 'control.log')
        self.manager = ControlManager(ExperimentLogger(folder, 'control_manager.log'))
        self.prompting = prompting

        self.initial_waiting_time = 20

        thread = threading.Thread(target=self.loop)
        thread.start()
    
    def loop(self):
        self.logger.log_debug("[LOOP] Started loop thread")
        while not self.stop and self.initial_waiting_time > 0:
            if not self.get_belief_set():
                self.logger.log_info("[LOOP] Waiting for belief set to be ready...")
                time.sleep(1)
            else:
                self.logger.log_info(f"[LOOP] Belief set is ready, waiting {self.initial_waiting_time} seconds...")
                self.initial_waiting_time -= 1
                time.sleep(1)
        
        generate_new_desire = True
        desire_id = -1
        intention_negative_evaluations = 0
        belief_set_prior = None

        while not self.stop:
            if generate_new_desire:
                self.logger.log_info("[LOOP] Checking if any desire is triggered")
                desire_id = self.manager.check_if_desire_triggered(self.get_belief_set())
                plan = self.manager.run_desire(desire_id, self.get_belief_set())
                if plan is not None:
                    self.logger.log_info(f"[LOOP] Desire triggered : {self.manager.get_desire_description(desire_id)}")
                    self.execute_plan(plan, wait_for_events=False)
                else:
                    self.logger.log_info("[LOOP] Generating new desire")
                    belief_set_prior = self.get_belief_set()
                    desire_description = self.question_1(belief_set_prior)
                    if desire_description is None:
                        self.logger.log_error("[LOOP] Error while generating desire")
                    else:
                        self.logger.log_info(f"[LOOP] Desire generated: {desire_description}")
                        desire_id = self.manager.add_desire(desire_description)
                        generate_new_desire = False
            else:
                self.logger.log_info("[LOOP] Generating new intention")
                intention_description = None
                belief_set_copy = self.get_belief_set()
                for i in range(3):
                    if intention_description is None:
                        intention_description, function_string, error = self.question_2(desire_description, belief_set_copy, self.manager.get_library())
                        for j in range(3):
                            if intention_description is None:
                                self.logger.log_error(f"[LOOP] Generation attempt {i+1}:{j+1} for intention failed with error {error}, retrying...")
                                function_string, error = self.question_3(function_string, belief_set_copy, intention_description, error, self.manager.get_library())
                if intention_description is None:
                    self.logger.log_error(f"[LOOP] Unable to generate intention for the desire")
                    generate_new_desire = True
                else:
                    self.logger.log_info(f"[LOOP] Intention generated: {intention_description}\n{function_string}")
                    intention_id = self.manager.add_intention(desire_id, intention_description, function_string)
                    plan = self.manager.run_intention(intention_id, self.get_belief_set())
                    if plan is None:
                        self.logger.log_error(f"[LOOP] Error while running intention generated")
                        self.manager.invalidate_intention(intention_id)
                        generate_new_desire = True
                    events = self.execute_plan(plan)
                    intention_evaluation = self.question_4(intention_description, plan, events)
                    if intention_evaluation is None:
                        self.logger.log_error(f"[LOOP] Unable to obtain evaluation for intention")
                        self.manager.invalidate_intention(intention_id)
                        generate_new_desire = True
                    else:
                        if intention_evaluation == "True":
                            desire_evaluation = self.question_5(desire_description, belief_set_prior, self.get_belief_set())
                            if desire_evaluation is None:
                                self.logger.log_error(f"[LOOP] Unable to obtain evaluation for desire")
                            else:
                                if desire_evaluation == "True":
                                    function_string = self.question_6(desire_description, self.get_belief_set(), belief_set_prior)
                                    if function_string is None:
                                        self.logger.log_error(f"[LOOP] Unable to obtain trigger function for desire")
                                    else:
                                        self.manager.add_trigger_function(desire_id, function_string)
                                        self.logger.log_info(f"[LOOP] Obtained trigger function for desire: {desire_description}\n{function_string}")
                                    self.logger.log_info(f"[LOOP] Desire satisfied")
                                    generate_new_desire = True
                                else:
                                    self.logger.log_info(f"[LOOP] Desire not yet satisfied")
                        else:
                            self.manager.invalidate_intention(intention_id)
                            if intention_negative_evaluations < 3:
                                intention_negative_evaluations += 1
                            else:
                                generate_new_desire = True

        self.logger.log_debug("[LOOP] Stopped loop thread")
        self.alive[0] = False
    
    def question_1(self, belief_set):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_1.txt'

        elements = [belief_set]
        elements_names = ["belief_set"]
        elements_to_extract = ["description"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q1")
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q1] Error while making request: {error}")
            return None

        return extracted_elements[0]
    
    def question_2(self, desire, belief_set, library):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_2.txt'

        elements = [desire, belief_set, library]
        elements_names = ["desire", "belief_set", "library"]
        elements_to_extract = ["goal", "function"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q2")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q2] Error while making request: {error}")
            return None, None, error
        
        intention = extracted_elements[0]
        function_string = extracted_elements[1]

        error = self.manager.test_intention(function_string, belief_set)
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q2] Error while testing intention function: {error}")
            return None, None, error
        
        return intention, function_string, None

    def question_3(self, function_string, belief_set, intention, error, library):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_3.txt'

        elements = [function_string, belief_set, intention, error, library]
        elements_names = ["function", "belief_set", "intention", "error", "library"]
        elements_to_extract = ["function"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q3")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q3] Error while making request: {error}")
            return None, error

        function_string = extracted_elements[0]

        error = self.manager.test_intention(function_string, belief_set)
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q3] Error while testing intention function: {error}")
            return None, error
        
        return function_string, None

    def question_4(self, intention, plan, events):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_4.txt'

        actions = [(action, events[i]) for i, action in enumerate(plan)]

        elements = [intention, actions]
        elements_names = ["intention", "actions"]
        elements_to_extract = ["evaluation"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q4")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q4] Error while making request: {error}")
            return None

        return extracted_elements[0]

    def question_5(self, desire, belief_set_prior, belief_set_current):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_5.txt'

        elements = [desire, belief_set_prior, belief_set_current]
        elements_names = ["desire", "belief_set_prior", "belief_set_current"]
        elements_to_extract = ["evaluation"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q5")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q5] Error while making request: {error}")
            return None
        
        return extracted_elements[0]

    def question_6(self, desire, belief_set, belief_set_prior):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_6.txt'

        elements = [desire, belief_set, belief_set_prior]
        elements_names = ["desire", "belief_set", "belief_set_prior"]
        elements_to_extract = ["function"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q6")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q6] Error while making request: {error}")
            return None
        
        function_string = extracted_elements[0]

        error = self.manager.test_trigger_function(function_string, belief_set_prior, belief_set)

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q6] Error while testing trigger function: {error}")
            return None
        
        return function_string
    
    def execute_plan(self, plan, wait_for_events=True):
        events_plan = []
        self.get_events()
        for action in plan:
            self.communication.send_to_server(action)
            if wait_for_events:
                time.sleep(0.2)
            events = self.get_events()
            events_plan.append(events)
        return events_plan
    
    def is_alive(self):
        return any(self.alive)