import time
import threading
from utils.Logger import ExperimentLogger
from agent_dir.utils.ControlManager import ControlManager

class Control:
    def __init__(self, folder, communication, prompting, get_events, get_belief_set, user_generated_desire, stateless_intention_generation, no_desire_triggering, no_evaluation_triggered_desires):
        self.communication = communication
        self.stop = False
        self.alive = [True]
        self.status = "Initialized"
        self.get_events = get_events
        self.get_belief_set = get_belief_set
        self.logger = ExperimentLogger(folder, 'control.log')
        self.evolution_logger = ExperimentLogger(folder, 'evolution.log')
        self.desire_steps = 0
        self.intention_steps = 0
        self.cumulative_intention_steps = 0
        self.manager = ControlManager(ExperimentLogger(folder, 'control_manager.log'), folder.split('/')[-1])
        self.prompting = prompting
        self.user_generated_desire = user_generated_desire
        self.stateless_intention_generation = stateless_intention_generation
        self.no_desire_triggering = no_desire_triggering
        self.no_evaluation_triggered_desires = no_evaluation_triggered_desires

        self.initial_waiting_time = 30

        self.initialize_memory()

        thread = threading.Thread(target=self.loop)
        thread.start()
    
    def loop(self):
        self.logger.log_debug("[LOOP] Started loop thread")
        while not self.stop and self.initial_waiting_time > 0:
            if not self.get_belief_set():
                self.logger.log_info("[LOOP] Waiting for belief set to be ready...")
                self.status = "Waiting for belief set to be ready"
                time.sleep(1)
            else:
                self.logger.log_info(f"[LOOP] Belief set is ready, waiting {self.initial_waiting_time} seconds...")
                self.status = f"Belief set is ready, waiting {self.initial_waiting_time} seconds"
                self.initial_waiting_time -= 1
                time.sleep(1)
        
        generate_new_desire = True
        desire_id = -1
        intention_negative_evaluations = 0
        belief_set_prior = None
        called_intentions = []
        last_intention_error = False

        while not self.stop:
            if generate_new_desire:
                # everytime it generates a new desire or checks for triggers, passes here
                self.desire_steps += 1
                res = input("Step concluded. Type 'stop' to avoid further generation: ")
                if res == "stop":
                    self.stop = True
                    break
                self.intention_steps = 0
                last_intention_error = False
                plan = None
                self.clear_memory()
                if not self.no_desire_triggering:
                    self.evolution_logger.log_info(f"[{self.desire_steps}]\tChecking desire triggers...")
                    self.logger.log_info("[LOOP] Checking if any desire is triggered")
                    self.status = "Checking if any desire is triggered"
                    desire_id = self.manager.check_if_desire_triggered(self.get_belief_set())
                    belief_set_before_execution = self.get_belief_set()
                    error, plan, events = self.manager.run_desire(desire_id, self.get_belief_set, self.execute_action)
                    belief_set_after_execution = self.get_belief_set()
                if plan is not None:
                    self.evolution_logger.log_info(f"[{self.desire_steps}]\tDesire triggered: {desire_id}")
                    self.logger.log_info(f"[LOOP] Desire triggered : {desire_id}")
                    self.logger.log_info(f"[LOOP] Plan generated: {plan}")
                    self.logger.log_info("[LOOP] Plan executed, asking for desire evaluation...")
                    self.status = f"Desire triggered and executed: {desire_id}, asking for desire evaluation"
                    if self.no_evaluation_triggered_desires:
                        self.logger.log_info("[LOOP] Evaluation of triggered desires disabled")
                        self.status = "Evaluation of triggered desires disabled"
                        desire_evaluation = "True"
                    else:
                        desire_evaluation = self.question_5(self.manager.get_desire_description(desire_id), belief_set_before_execution, belief_set_after_execution)
                    if desire_evaluation is None:
                        self.logger.log_error(f"[LOOP] Unable to obtain evaluation for desire")
                        self.status = "Unable to obtain evaluation for desire"
                        self.manager.invalidate_desire(desire_id)
                    else:
                        if desire_evaluation == "True":
                            self.logger.log_info(f"[LOOP] Desire triggered evaluated positively")
                            self.status = "Desire triggered evaluated positively"
                        else:
                            self.logger.log_info(f"[LOOP] Desire triggered evaluated negatively")
                            self.status = "Desire triggered evaluated negatively"
                            self.manager.invalidate_desire(desire_id)
                else:
                    self.evolution_logger.log_info(f"[{self.desire_steps}]\tGenerating new desire...")
                    self.logger.log_info("[LOOP] Generating new desire")
                    self.status = "Generating new desire"
                    belief_set_prior = self.get_belief_set()
                    if self.user_generated_desire:
                        self.status = "Please input in the terminal the desire you want to generate..."
                        desire_description = input("Enter a desire: ")
                    else:
                        implemented_desires_descriptions = self.manager.get_desires_descriptions()
                        desire_description = self.question_1(belief_set_prior, implemented_desires_descriptions)
                    if desire_description is None:
                        self.logger.log_error("[LOOP] Error while generating desire")
                        intention_negative_evaluations = 0
                        called_intentions = []
                        generate_new_desire = True
                    else:
                        self.logger.log_info(f"[LOOP] Desire generated: {desire_description}")
                        self.status = f"Desire generated: {desire_description}"
                        desire_id = self.manager.add_desire(desire_description)
                        self.evolution_logger.log_info(f"[{self.desire_steps}]\tDesire generated: {desire_id}")
                        intention_negative_evaluations = 0
                        called_intentions = []
                        generate_new_desire = False
            else:
                # everytime it generates a new intention, passes here
                if not last_intention_error:
                    self.clear_memory()
                self.intention_steps += 1
                self.cumulative_intention_steps += 1
                self.evolution_logger.log_info(f"[{self.desire_steps}]\t[{self.intention_steps}]\tGenerating new intention...")
                self.logger.log_info("[LOOP] Generating new intention ...")
                self.status = "Generating new intention"
                intention_description = None
                error = "error"
                belief_set_copy = self.get_belief_set()
                for i in range(3):
                    if error is not None:
                        if last_intention_error:
                            intention_description, function_string, error = self.question_2_MEM(desire_description, belief_set_copy, self.manager.get_library(self.stateless_intention_generation), self.get_memory())
                        else:
                            intention_description, function_string, error = self.question_2(desire_description, belief_set_copy, self.manager.get_library(self.stateless_intention_generation))
                        for j in range(2):
                            if error is not None and intention_description is not None:
                                self.logger.log_error(f"[LOOP] Generation attempt {i+1}:{j+1} for intention failed with error {error}, retrying...")
                                self.status = f"Generation attempt {i+1}:{j+1} for intention failed with error {error}, retrying..."
                                function_string, error = self.question_3(function_string, belief_set_copy, intention_description, error, self.manager.get_library(self.stateless_intention_generation))
                if error is not None or intention_description is None:
                    self.logger.log_error(f"[LOOP] Unable to generate intention for the desire")
                    self.status = "Unable to generate intention for the desire"
                    intention_negative_evaluations = 0
                    called_intentions = []
                    generate_new_desire = True
                else:
                    self.logger.log_info(f"[LOOP] Intention generated: {intention_description}\n{function_string}")
                    self.status = f"Intention generated: {intention_description}"
                    intention_id = self.manager.add_intention(desire_id, intention_description, function_string)
                    self.evolution_logger.log_info(f"[{self.desire_steps}]\t[{self.intention_steps}]\tIntention generated: {intention_id}")
                    library_before_execution = self.manager.get_library(self.stateless_intention_generation)
                    belief_set_before_execution = self.get_belief_set()
                    error, plan, events = self.manager.run_intention(intention_id, self.get_belief_set, self.execute_action)
                    belief_set_after_execution = self.get_belief_set()
                    if error is not None:
                        self.logger.log_error(f"[LOOP] Error while running intention generated: {error}")
                        self.status = f"Error while running intention generated: {error}"
                        intention_evaluation = "False"
                        last_intention_error = True
                        new_memory = self.question_7(function_string, intention_description, error, belief_set_before_execution, belief_set_after_execution, plan, events, library_before_execution)
                        self.update_memory(new_memory)
                        if new_memory is None:
                            self.logger.log_error(f"[LOOP] Unable to obtain new memory for intention after execution error")
                            self.status = "Unable to obtain new memory for intention after execution error"
                            intention_evaluation = None
                    else:
                        self.logger.log_info(f"[LOOP] Plan executed: {plan}")
                        self.logger.log_info(f"[LOOP] Events received: {events}")
                        self.logger.log_info(f"[LOOP] Asking for intention evaluation and memory update...")
                        self.status = "Asking for intention evaluation and memory update..."
                        intention_evaluation, new_memory = self.question_4(intention_description, plan, events, belief_set_before_execution, belief_set_after_execution)
                        self.update_memory(new_memory)
                    if intention_evaluation is None:
                        self.logger.log_error(f"[LOOP] Unable to obtain evaluation for intention")
                        self.status = "Unable to obtain evaluation for intention"
                        self.manager.invalidate_intention(intention_id)
                        intention_negative_evaluations = 0
                        called_intentions = []
                        generate_new_desire = True
                    else:
                        if intention_evaluation == "True":
                            last_intention_error = False
                            self.clear_memory()
                            intention_negative_evaluations = 0
                            called_intentions = []
                            self.logger.log_info(f"[LOOP] Intention evaluation positive")
                            self.status = "Intention evaluation positive, now asking for desire evaluation..."
                            self.logger.log_info("[LOOP] Asking for desire evaluation...")
                            if self.user_generated_desire:
                                desire_evaluation = None
                                while desire_evaluation is None or desire_evaluation not in ["True", "False"]:
                                    desire_evaluation = input("Enter evaluation for the desire (True/False): ")
                            else:
                                desire_evaluation = self.question_5(desire_description, belief_set_prior, self.get_belief_set())
                            if desire_evaluation is None:
                                self.logger.log_error(f"[LOOP] Unable to obtain evaluation for desire")
                                self.status = "Unable to obtain evaluation for desire"
                            else:
                                if desire_evaluation == "True":
                                    self.logger.log_info(f"[LOOP] Desire evaluation positive")
                                    self.status = "Desire evaluation positive, now asking for trigger function..."
                                    if not self.user_generated_desire:
                                        function_string = self.question_6(desire_description, self.get_belief_set(), belief_set_prior)
                                        if function_string is None:
                                            self.logger.log_error(f"[LOOP] Unable to obtain trigger function for desire")
                                            self.status = "Unable to obtain trigger function for desire"
                                        else:
                                            self.manager.add_trigger_function(desire_id, function_string)
                                            self.logger.log_info(f"[LOOP] Obtained trigger function for desire: {desire_description}\n{function_string}")
                                            self.status = f"Obtained trigger function for desire: {desire_description}"
                                    self.logger.log_info(f"[LOOP] Desire satisfied")
                                    self.status = f"Desire satisfied: {desire_description}"
                                    intention_negative_evaluations = 0
                                    called_intentions = []
                                    generate_new_desire = True
                                else:
                                    self.logger.log_info(f"[LOOP] Desire not yet satisfied")
                                    self.status = f"Desire not yet satisfied: {desire_description}"
                        else:
                            # last_intention_error = True # already True if reached this line
                            self.logger.log_info(f"[LOOP] Intention evaluated negatively or failed to run")
                            self.status = "Intention evaluated negatively or failed to run"
                            if intention_negative_evaluations == 0:
                                called_intentions = self.manager.get_intentions_called_by(intention_id)
                            else: 
                                new_called_intentions = []
                                temp = self.manager.get_intentions_called_by(intention_id)
                                for called_intention in called_intentions:
                                    if called_intention in temp:
                                        new_called_intentions.append(called_intention)
                                called_intentions = new_called_intentions
                            self.manager.invalidate_intention(intention_id)
                            if intention_negative_evaluations < 2:
                                intention_negative_evaluations += 1
                            else:
                                self.logger.log_info(f"[LOOP] Intention evaluation or intention run failed 3 times, generating new desire and invalidating called intentions: {called_intentions}")
                                self.status = f"Intention evaluation or intention run failed 3 times"
                                intention_negative_evaluations = 0
                                for called_intention in called_intentions: # intentions used in all three last failed attempts are invalidated
                                    self.manager.invalidate_intention(called_intention)
                                called_intentions = []
                                generate_new_desire = True

        self.logger.log_debug("[LOOP] Stopped loop thread")
        self.alive[0] = False
    
    def question_1(self, belief_set, descriptions):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_1.txt'

        elements = [belief_set, descriptions]
        elements_names = ["belief_set", "descriptions"]
        elements_to_extract = ["description"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q1")
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q1] Error while making request: {error}")
            return None

        return extracted_elements[0]
    
    def question_2(self, desire, belief_set, library):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        if self.stateless_intention_generation:
            question_prompt_path = 'agent_dir/prompts/control_question_2_SIG.txt'
        else:
            question_prompt_path = 'agent_dir/prompts/control_question_2.txt'

        elements = [desire, belief_set, library]
        elements_names = ["desire", "belief_set", "library"]
        elements_to_extract = ["description", "function"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q2")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q2] Error while making request: {error}")
            return None, None, error
        
        intention = extracted_elements[0]
        function_string = extracted_elements[1]

        error = self.manager.test_intention(function_string)
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q2] Error while testing intention function: {error}")
            return intention, function_string, error
        
        return intention, function_string, None

    def question_2_MEM(self, desire, belief_set, library, memory):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        if self.stateless_intention_generation:
            question_prompt_path = 'agent_dir/prompts/control_question_2_SIG_MEM.txt'
        else:
            question_prompt_path = 'agent_dir/prompts/control_question_2_MEM.txt'
        
        elements = [desire, belief_set, library, memory]
        elements_names = ["desire", "belief_set", "library", "memory"]
        elements_to_extract = ["description", "function"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q2MEM")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q2MEM] Error while making request: {error}")
            return None, None, error
        
        intention = extracted_elements[0]
        function_string = extracted_elements[1]

        error = self.manager.test_intention(function_string)
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q2MEM] Error while testing intention function: {error}")
            return intention, function_string, error
        
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
            return function_string, error

        function_string = extracted_elements[0]

        error = self.manager.test_intention(function_string)
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q3] Error while testing intention function: {error}")
            return function_string, error
        
        return function_string, None

    def question_4(self, intention, plan, events, belief_set_prior, belief_set_after):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_4.txt'

        actions = [(action, events[i]) for i, action in enumerate(plan)]

        elements = [intention, belief_set_prior, actions, belief_set_after]
        elements_names = ["intention", "belief_set_prior", "actions", "belief_set_after"]
        elements_to_extract = ["evaluation", "suggestions"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q4")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q4] Error while making request: {error}")
            return None, None
        
        self.logger.log_info(f"[LOOP] Obtained evaluation for intention: {extracted_elements[0]}")
        self.logger.log_info(f"[LOOP] Obtained memory update: {extracted_elements[1]}")

        return extracted_elements[0], extracted_elements[1]

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
        
        self.logger.log_info(f"[LOOP] Obtained evaluation for desire: {extracted_elements[0]}")
        
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

    def question_7(self, function_string, intention_description, error, belief_set_before, belief_set_after, plan, events, library):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/control_question_7.txt'

        actions = [(action, events[i]) for i, action in enumerate(plan)] # needs to be cut down because of timeout error

        elements = [function_string, library, intention_description, error, belief_set_before, actions, belief_set_after]
        elements_names = ["function", "library", "intention", "error", "belief_set_before", "actionsQ7", "belief_set_after"]
        elements_to_extract = ["suggestions"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="CONTROL Q7")

        if error is not None:
            self.logger.log_error(f"[LOOP] [Q7] Error while making request: {error}")
            return None

        self.logger.log_info(f"[LOOP] [Q7] Obtained memory update: {extracted_elements[0]}")

        return extracted_elements[0]
    
    def execute_plan(self, plan, wait_for_events=True):
        events_plan = []
        self.get_events()
        for action in plan:
            if self.stop:
                events_plan.append([])
            else:
                self.communication.send_to_server(action)
                if wait_for_events:
                    time.sleep(0.2)
                events = self.get_events()
                events_plan.append(events)
        return events_plan
    
    def execute_action(self, action):
        self.get_events()
        self.communication.send_to_server(action)
        time.sleep(0.2)
        return self.get_events()
    
    def initialize_memory(self):
        initial_memory_path = 'agent_dir/prompts/initial_memory.txt'
        self.memory = []
        with open(initial_memory_path, 'r') as file:
            self.memory.append(str(file.read()))
            file.close()
    
    def clear_memory(self):
        if self.memory[-1] != "":
            self.memory.append("")

    def update_memory(self, new_memory):
        if new_memory is not None:
            self.memory.append(new_memory)
            self.logger.log_info(f"[LOOP] Memory updated: {new_memory}")
    
    def get_memory(self):
        return self.memory[-1]
    
    def get_printable_memory(self):
        out = ""
        for memory in self.memory:
            out += f"- {memory}\n"
        return out
    
    def is_alive(self):
        return any(self.alive)