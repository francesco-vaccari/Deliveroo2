import threading
import time
from function_tester import test_perception_function, rename_function, get_function_name
import json
import prompting as prompting

class Perception:
    def __init__(self, server):
        self.server = server
        self.prompting = prompting.Prompting()
        
        self.events = []
        self.control_events = []
        self.events_by_object = {}
        self.functions_by_object = {}
        self.belief_set = {}

        self.scaling_factor = 2
        self.initial_scaling = 1
        self.max_retries = 3
        self.n_example_events = 5

        self.last_trigger_by_object = {}
        self.scaling_by_object = {}
        self.special_triggers = {}
        self.example_events = {}

        self.stop = False
        
        # self.processing_thread = threading.Thread(target=self.process_events, args=())
        # self.processing_thread.start()

        self.storing_thread = threading.Thread(target=self.store_incoming_events, args=())
        self.storing_thread.start()
        
        # self.thread = threading.Thread(target=self.main_loop, args=())
        # self.thread.start()

    def main_loop(self):
        while not self.stop:
            events_by_object_copy = self.events_by_object.copy()
            for object_type, _ in events_by_object_copy.items():
                res = self.create_new_perception_function(object_type)
                if res == "error":
                    print(f"Could not create a new perception function for {object_type}. Exiting.")
                    self.close()
        
        self.close()
        print("Perception exited correctly.")
    
    def store_incoming_events(self):
        while not self.stop:
            if len(self.events) > 0:
                try:
                    event = json.loads(self.events.pop(0))
                    self.control_events.append(event)
                    object_type = event['object_type']
                    if object_type not in self.events_by_object:
                        self.events_by_object[object_type] = []
                        self.special_triggers[object_type] = None
                        self.last_trigger_by_object[object_type] = time.time()
                        self.scaling_by_object[object_type] = self.initial_scaling
                    
                    self.events_by_object[object_type].append(event)
                    self.set_example_events(event, object_type)
                except Exception as e:
                    print(f"Error storing incoming events (probably due to server closing): {e}")
    
    def create_new_perception_function(self, object_type):
        if self.threshold(object_type) or self.special_triggers[object_type] is not None:
            self.functions_by_object[object_type] = None

            example_events = self.get_example_events(object_type)
            res, function_string = self.ask_new_function(object_type, example_events)
            if not res:
                return "error"
            name = f"process_{object_type}" + "_" + str(int(time.time()))
            function_string = rename_function(function_string, name)

            self.last_trigger_by_object[object_type] = time.time()
            self.scaling_by_object[object_type] *= self.scaling_factor
            self.functions_by_object[object_type] = function_string

            self.special_triggers[object_type] = None

            return "success"

    def ask_new_function(self, object_type, example_events):
        tested = False
        parsing_retries = 0
        function_string = ""
        while not tested and parsing_retries < self.max_retries:
            retries = 0

            # print(f"[ASK] {object_type}")
            context_path = "prompts/context.txt"
            question_path = "prompts/perception_question_1.txt"
            elements = [example_events[object_type], self.belief_set, object_type]
            elements_names = ["example_events", "belief_set", "object_type"]
            elements_to_extract = ["function"]
            
            parsed, extracted_elements, err = self.prompting.make_request(context_path, question_path, elements, elements_names, elements_to_extract)
            # print(f"[ASK]\tparsed: {parsed}\terr: {err}")
            if parsed:
                function_string = extracted_elements[0]
                tested, err = test_perception_function(function_string, example_events[object_type], self.belief_set)
                # print(f"[ASK]\ttested: {tested}\terr: {err}")

                while not tested and retries < self.max_retries:
                    # print(f"[ASK]\t\tretrying {object_type}")
                    context_path = "prompts/context.txt"
                    question_path = "prompts/perception_question_2.txt"
                    elements = [example_events[object_type], function_string, err, self.belief_set, object_type]
                    elements_names = ["example_events", "function", "error", "belief_set", "object_type"]
                    elements_to_extract = ["function"]

                    parsed, extracted_elements, err = self.prompting.make_request(context_path, question_path, elements, elements_names, elements_to_extract)
                    # print(f"[ASK]\t\tparsed: {parsed}\terr: {err}")
                    if parsed:
                        function_string = extracted_elements[0]
                        tested, err = test_perception_function(function_string, example_events[object_type], self.belief_set)
                        # print(f"[ASK]\t\ttested: {tested}\terr: {err}")
                    
                    retries += 1
            parsing_retries += 1
        
        return tested, function_string
    
    def process_events(self):
        while not self.stop:
            events_by_object_copy = self.events_by_object.copy()
            functions_by_object_copy = self.functions_by_object.copy()

            for object_type, events in events_by_object_copy.items():
                if object_type in functions_by_object_copy and functions_by_object_copy[object_type] is not None:
                    function_string = functions_by_object_copy[object_type]
                    function_name = get_function_name(function_string)

                    for event in events:
                        try:
                            local_scope = {}
                            exec(function_string, {}, local_scope)
                            
                            if function_name not in local_scope:
                                raise ValueError(f"Function '{function_name}' is not defined.")
                            
                            func = local_scope[function_name]
                            
                            self.belief_set = func(event, self.belief_set)

                        except Exception as e:
                            self.special_triggers[object_type] = event
                            self.functions_by_object[object_type] = None
    
    def get_example_events(self, object_type):
        if self.special_triggers[object_type] is not None:
            return [self.special_triggers[object_type]] + self.example_events
        return self.example_events

    def set_example_events(self, event, object_type):
        if object_type not in self.example_events:
            self.example_events[object_type] = []

        if len(self.example_events[object_type]) == self.n_example_events:
            self.example_events[object_type].pop(0)
        self.example_events[object_type].append(event)

    def threshold(self, object_type):
        events = self.events_by_object[object_type]
        last_trigger = self.last_trigger_by_object[object_type]
        scaling = self.scaling_by_object[object_type]

        time_elapsed = time.time() - last_trigger
        return ((len(events) / 5) * ((time_elapsed / 3) ** 2)) > (1 * scaling)
    
    def control_get_events(self):
        events = self.control_events
        self.control_events = []
        return events
    
    def close(self):
        self.stop = True