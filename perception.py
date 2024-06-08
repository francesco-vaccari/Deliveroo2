import threading
import time
from function_tester import test_function, rename_function, get_function_name
import json
import prompting.prompting as prompting

class Perception:
    def __init__(self, server):
        self.server = server
        self.events = []
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

        self.prompting = prompting.Prompting()
        
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.main_loop, args=())
        self.thread.start()

    def main_loop(self):
        processing_thread = threading.Thread(target=self.process_events, args=())
        processing_thread.start()

        while not self.stop_event.is_set():
            if len(self.events) > 0:
                event = json.loads(self.events.pop(0))

                object_type = event['object_type']
                if object_type not in self.events_by_object:
                    self.events_by_object[object_type] = []
                    self.special_triggers[object_type] = None
                    self.last_trigger_by_object[object_type] = time.time()
                    self.scaling_by_object[object_type] = self.initial_scaling
                
                self.events_by_object[object_type].append(event)
                self.set_example_events(event, object_type)

            for object_type, events in self.events_by_object.items():
                if self.threshold(events, self.last_trigger_by_object[object_type], self.scaling_by_object[object_type]) or self.special_triggers[object_type] is not None:
                    self.functions_by_object[object_type] = None

                    example_events = self.get_example_events(object_type)

                    function_string = self.ask_function(object_type, example_events)
                    
                    name = f"process_{object_type}" + "_" + str(int(time.time()))
                    function_string = rename_function(function_string, name)

                    self.last_trigger_by_object[object_type] = time.time()
                    self.scaling_by_object[object_type] *= self.scaling_factor

                    self.functions_by_object[object_type] = function_string

                    self.special_triggers[object_type] = None
        
        print("Perception exited correctly.")
        exit()

    def ask_function(self, object_type, example_events):
        res = False
        retries = 0
        while not res:
            ### TEMP ### this could be a function in the prompting class
            elements = [example_events, self.belief_set]
            elements_names = ["example_events", "belief_set"]
            elements_to_extract = ["function"]
            
            context = self.prompting.get_prompt("prompting/perception_context.txt")
            question = self.prompting.get_prompt("prompting/perception_question_1.txt", elements, elements_names)
            response = self.prompting.ask(context, question)
            extracted_elements = self.prompting.extract_elements(response, elements_to_extract)

            function_string = extracted_elements[0]
            ### TEMP ###

            res, err = test_function(function_string, example_events, self.belief_set)
            
            if not res:
                while retries < self.max_retries and not res:
                    ### TEMP ### this could be a function in the prompting class
                    elements = [example_events, function_string, err, self.belief_set]
                    elements_names = ["example_events", "function", "error", "belief_set"]
                    elements_to_extract = ["function"]
                    
                    context = self.prompting.get_prompt("prompting/perception_context.txt")
                    question = self.prompting.get_prompt("prompting/perception_question_2.txt", elements, elements_names)
                    response = self.prompting.ask(context, question)
                    extracted_elements = self.prompting.extract_elements(response, elements_to_extract)

                    function_string = extracted_elements[0]
                    ### TEMP ###

                    res, err = test_function(function_string, example_events, self.belief_set)
                    retries += 1
        
        return function_string
    
    def process_events(self):
        while not self.stop_event.is_set():
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

    def threshold(self, events, last_trigger, scaling):
        time_elapsed = time.time() - last_trigger
        return ((len(events) / 5) * ((time_elapsed / 3) ** 2)) > (1 * scaling)

    
    def close(self):
        self.stop_event.set()