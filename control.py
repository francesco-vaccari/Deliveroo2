import time
import threading
import prompting as prompting
from function_tester import test_control_function, rename_function, get_function_name
from actions.library import Library

class Control:
    def __init__(self, server, perception):
        self.server = server
        self.prompting = prompting.Prompting()

        self.belief_set = perception.belief_set
        self.get_events = perception.control_get_events

        self.intial_waiting_time = 20
        self.max_retries = 3

        self.library = Library("actions/actions.json")
        self.library.update_library("test_function", """def test_function(belief_set):\n    pick_up(belief_set)\n    move_left(belief_set)""", "picks up and moves left")

        self.desires = []

        self.stop = False
        self.thread = threading.Thread(target=self.main_loop, args=())
        self.thread.start()

    def main_loop(self):
        # while not self.belief_set and not self.stop:
        #     time.sleep(1)
        # if not self.stop:
        #     time.sleep(self.intial_waiting_time)
        
        new_desire_generation = True
        intention_retries = 0
        max_intention_retries = 3
        
        desire = ""
        intentions = []
        belief_set_prior = {}
        
        while not self.stop:
            if new_desire_generation:
                while new_desire_generation and not self.stop:
                    belief_set_prior = self.belief_set.copy()
                    res, desire = self.question_1()
                    if res:
                        new_desire_generation = False
                        intention_retries = 0
                        intentions = []
                    else:
                        print("Could not obtain the desire. Retrying.")
                        time.sleep(1)
            else:
                # testare tutte le funzioni in libreria con il belief set e poi tenere quello per tutto il ciclo?
                res, intention, function_string = self.question_2_3(desire)
                if not res:
                    print("Could not obtain intention or a function. Exiting.")
                    new_desire_generation = True
                else:
                    plan = self.generate_plan(function_string)
                    events = self.execute_plan(plan)
                    res, evaluation = self.question_4(plan, events, intention)
                    if not res:
                        print("Could not obtain intention evaluation. Exiting.")
                        new_desire_generation = True
                    else:
                        if not evaluation:
                            if intention_retries < max_intention_retries:
                                intention_retries += 1
                            else:
                                new_desire_generation = True
                        else:
                            intention_object = self.library.update_library(get_function_name(function_string), function_string, intention)
                            intentions.append(intention_object)
                            res, evaluation = self.question_5(desire, belief_set_prior)
                            if not res:
                                print("Could not obtain desire evaluation. Exiting.")
                                new_desire_generation = True
                            else:
                                if evaluation:
                                    self.desires.append({"desire": desire, "intentions": intentions})
                                    new_desire_generation = True
                                    print(self.desires)

        
        self.close()
        print("Control exited correctly.")
    
    def question_1(self):
        parsed = False
        parsing_retries = 0
        while not parsed and parsing_retries < self.max_retries:
            context_path = "prompts/context.txt"
            question_path = "prompts/control_question_1.txt"
            elements = [self.belief_set]
            elements_names = ["belief_set"]
            elements_to_extract = ["description"]

            parsed, extracted_elements, err = self.prompting.make_request(context_path, question_path, elements, elements_names, elements_to_extract)
            parsing_retries += 1
        
        if not parsed:
            return False, ""
        return True, extracted_elements[0]

    def question_2_3(self, desire):
        tested = False
        parsing_retries = 0
        intention = ""
        function_string = ""
        while not tested and parsing_retries < self.max_retries:
            retries = 0

            context_path = "prompts/context.txt"
            question_path = "prompts/control_question_2.txt"
            elements = [desire, self.library.get_unified_library(), self.belief_set]
            elements_names = ["desire", "library", "belief_set"]
            elements_to_extract = ["function", "description"]
            parsed, extracted_elements, err = self.prompting.make_request(context_path, question_path, elements, elements_names, elements_to_extract)

            if parsed:
                function_string = extracted_elements[0]
                intention = extracted_elements[1]
                tested, err = test_control_function(function_string, self.belief_set, self.library.get_test_file_content(), self.library.get_list_function_names())
                
                while retries < self.max_retries and not tested:
                    context_path = "prompts/context.txt"
                    question_path = "prompts/control_question_3.txt"
                    elements = [function_string, self.belief_set, intention, err, self.library.get_dump()]
                    elements_names = ["function", "belief_set", "intention", "error", "library"]
                    elements_to_extract = ["function"]
                    parsed, extracted_elements, err = self.prompting.make_request(context_path, question_path, elements, elements_names, elements_to_extract)

                    if parsed:
                        function_string = extracted_elements[0]
                        tested, err = test_control_function(function_string, self.belief_set, self.library.get_test_file_content(), self.library.get_list_function_names())

                    retries += 1
            parsing_retries += 1

        return tested, intention, function_string
    
    def question_4(self, plan, events, intention):
        parsed = False
        parsing_retries = 0
        while not parsed and parsing_retries < self.max_retries:
            context_path = "prompts/context.txt"
            question_path = "prompts/control_question_4.txt"
            actions = {}
            for action, event in zip(plan, events):
                actions[action] = event
            elements = [intention, actions]
            elements_names = ["intention", "actions"]
            elements_to_extract = ["evaluation"]

            parsed, extracted_elements, err = self.prompting.make_request(context_path, question_path, elements, elements_names, elements_to_extract)
            parsing_retries += 1

        if not parsed:
            return False, ""
        return True, extracted_elements[0]

    def question_5(self, desire, belief_set_prior):
        parsed = False
        parsing_retries = 0
        while not parsed and parsing_retries < self.max_retries:
            context_path = "prompts/context.txt"
            question_path = "prompts/control_question_5.txt"
            elements = [desire, belief_set_prior, self.belief_set]
            elements_names = ["desire", "belief_set_prior", "belief_set_current"]
            elements_to_extract = ["evaluation"]

            parsed, extracted_elements, err = self.prompting.make_request(context_path, question_path, elements, elements_names, elements_to_extract)
            parsing_retries += 1

        if not parsed:
            return False, ""
        return True, extracted_elements[0]

    def generate_plan(self, function_string):
        with open("actions/functions.py", "w") as file:
            file.write(self.library.get_file_content())
        
        import actions.functions as functions
        global_scope = {}
        for name in self.library.get_list_function_names():
            global_scope[name] = getattr(functions, name)
        
        local_scope = {}
        exec(function_string, global_scope, local_scope)

        function_name = get_function_name(function_string)
        func = local_scope[function_name]
        func(self.belief_set)
        
        return functions.plan

    def execute_plan(self, plan):
        events_plan = []
        self.get_events()
        
        for action in plan:
            self.server.send(action)
            time.sleep(0.5)
            events = self.get_events()
            events_plan.append(events)
        
        return events_plan
    
    def send_action(self, action):
        self.server.send(action)
    
    def close(self):
        self.stop = True