import time
import threading
import prompting as prompting
from function_tester import test_control_function, get_function_name, check_library_functions, test_desire_trigger_function
from actions.library import Library
import importlib

class Control:
    def __init__(self, server, perception):
        self.server = server
        self.prompting = prompting.Prompting()

        self.belief_set = perception.belief_set
        self.get_events = perception.control_get_events

        self.intial_waiting_time = 20
        self.max_retries = 3

        self.library = Library("actions/actions.json")

        self.desires = [] # contains the description and the list of intentions with their descriptions and functions
        self.desires_trigger_functions = [] # contains the functions that trigger the execution of its desire

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
            if new_desire_generation: # desire generation or desire trigger
                trigger, desire_index = self.check_trigger_functions()
                if trigger:
                    print(f"Desire triggered: {self.desires[desire_index]['desire']}")
                    plan = []
                    for intention in self.desires[desire_index]["intentions"]:
                        function_string = intention.function_string
                        if function_string not in self.library.broken_function_names:
                            plan += self.generate_plan(function_string)
                        else:
                            print(f"Desire {self.desires[desire_index]['desire']} has a broken intention.")
                            self.desires_trigger_functions[desire_index] = None
                            plan = []
                    print(f"Plan: {plan}")
                    self.execute_plan(plan)
                    time.sleep(1) # to remove
                else:
                    belief_set_prior = self.belief_set.copy()
                    res, desire = self.question_1()
                    if res:
                        print(f"Desire generated: {desire}")
                        new_desire_generation = False
                        intention_retries = 0
                        intentions = []
                    else:
                        print("Could not obtain the desire. Retrying.")
                        time.sleep(1)
            else: # intention generation
                res, intention, function_string = self.question_2_3(desire)
                if not res:
                    print("Could not obtain intention or function.")
                    new_desire_generation = True
                else:
                    print(f"Intention generated: {intention}")
                    plan = self.generate_plan(function_string)
                    if plan is None:
                        print("Could not generate a plan.")
                    else:
                        print(f"Plan: {plan}")
                        events = self.execute_plan(plan)
                        res, evaluation = self.question_4(plan, events, intention)
                        if not res:
                            print("Could not obtain intention evaluation.")
                            new_desire_generation = True
                        else:
                            print(f"Intention evaluation: {evaluation}")
                            if evaluation == "True":
                                intention_object = self.library.update_library(function_string, intention)
                                intentions.append(intention_object)
                                res, evaluation = self.question_5(desire, belief_set_prior)
                                if not res:
                                    print("Could not obtain desire evaluation.")
                                    new_desire_generation = True
                                else:
                                    print(f"Desire evaluation: {evaluation}")
                                    if evaluation == "True":
                                        self.desires.append({"desire": desire, "intentions": intentions})
                                        res, function_string = self.question_6(desire, belief_set_prior)
                                        if res:
                                            self.desires_trigger_functions.append(function_string)
                                        else:
                                            print("Could not obtain desire trigger function.")
                                            self.desires_trigger_functions.append(None)
                                        new_desire_generation = True
                                    else:
                                        pass # means keep generating intentions
                            else:
                                intention_retries += 1
                                if intention_retries >= max_intention_retries:
                                    new_desire_generation = True
                                    print("Three intention evaluations failed. Generating a new desire.")

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

    def question_6(self, desire, belief_set_prior):
        tested = False
        retries = 0
        function_string = ""
        while not tested and retries < self.max_retries: # function has to be both parsable and executable
            context_path = "prompts/context.txt"
            question_path = "prompts/control_question_6.txt"
            elements = [desire, belief_set_prior, self.belief_set]
            elements_names = ["desire", "belief_set_prior", "belief_set"]
            elements_to_extract = ["function"]

            parsed, extracted_elements, err = self.prompting.make_request(context_path, question_path, elements, elements_names, elements_to_extract)

            if parsed:
                function_string = extracted_elements[0]
                tested, err = test_desire_trigger_function(function_string, self.belief_set, belief_set_prior)
        
            retries += 1
        
        return tested, function_string

    def generate_plan(self, function_string):
        belief_set = self.belief_set
        base_test_functions = self.library.get_base_test_file_content()

        to_remove = []
        for i in range(self.library.get_number_of_functions()):
            not_base_test_functions = self.library.get_not_base_test_file_content(i)
            base_function_names = self.library.get_base_list_function_names()
            not_base_functions_names = self.library.get_n_not_base_list_function_names(i)
            functions_names = base_function_names + not_base_functions_names
            function_to_test = self.library.get_definition(i)
            res = check_library_functions(base_test_functions, not_base_test_functions, functions_names, function_to_test, belief_set)
            if not res:
                to_remove.append(self.library.get_function_name(i))
        
        is_broken = self.library.is_function_dependent(function_string, to_remove)
        for name in to_remove:
            print(f"Removing now broken function {name}")
            self.library.remove_function(name)
        if is_broken:
            return None
        
        with open("actions/functions.py", "w") as file:
            file.write(self.library.get_file_content())
        try:
            import actions.functions as functions
            global_scope = {}
            for name in self.library.get_list_function_names():
                importlib.reload(functions)
                global_scope[name] = getattr(functions, name)
            
            local_scope = {}
            exec(function_string, global_scope, local_scope)

            function_name = get_function_name(function_string)
            func = local_scope[function_name]
            func(belief_set)
        except Exception as e:
            return None
        
        return functions.plan

    def execute_plan(self, plan):
        events_plan = []
        self.get_events()
        
        for action in plan:
            self.server.send(action)
            time.sleep(0.2)
            events = self.get_events()
            events_plan.append(events)
        
        return events_plan
    
    def check_trigger_functions(self):
        trigger = False
        i = -1
        for i, function_string in enumerate(self.desires_trigger_functions):
            if not trigger:
                if function_string is not None:
                    try:
                        local_scope = {}
                        exec(function_string, {}, local_scope)
                        func = local_scope[get_function_name(function_string)]
                        trigger = func(self.belief_set)
                    except Exception as e:
                        trigger = False
        return trigger, i

    def send_action(self, action):
        self.server.send(action)
    
    def close(self):
        self.stop = True
    
    def print_desires(self):
        print("--------------------------------")
        for desire in self.desires:
            print(f"Desire: {desire['desire']}")
            print("Intentions:")
            for intention in desire["intentions"]:
                print(f"    - name: {intention.function_name}\t description: {intention.description}")
        print("--------------------------------")