import time
import json
import math
import copy
import threading
from utils.Logger import ExperimentLogger
from agent_dir.utils.PerceptionManager import PerceptionManager

class Perception:
    def __init__(self, folder, communication, prompting, generation_only_on_error):
        self.alive = [True, True, True]
        self.stop = False
        self.status = "Initialized"
        self.communication = communication
        self.logger = ExperimentLogger(folder, 'perception.log')
        self.manager = PerceptionManager(ExperimentLogger(folder, 'perception_manager.log'))
        self.prompting = prompting

        self.events = []
        self.control_events = []

        self.initial_scaling_factor = 1.0
        self.scaling_factor_multiplier = 12.0
        self.number_example_events = 2
        self.generation_only_on_error = generation_only_on_error

        self.events_by_type = {}
        self.error_event_by_type = {}
        self.example_events_by_type = {}
        self.last_generation_by_type = {}
        self.scaling_factor_by_type = {}
        self.belief_set = {}

        storing_thread = threading.Thread(target=self.store_events)
        storing_thread.start()
        processing_thread = threading.Thread(target=self.process_events)
        processing_thread.start()
        loop_thread = threading.Thread(target=self.loop)
        loop_thread.start()
    
    def store_events(self):
        self.logger.log_debug("[STORE_EVENTS] Started storing events thread")
        while not self.stop:
            if len(self.events) > 0:
                event = self.events.pop(0)
                event = json.loads(event)
                self.control_events.append(event)
                object_type = event['object_type']
                if object_type not in self.events_by_type:
                    self.logger.log_info(f"[STORE_EVENTS] New object type detected: {object_type}")
                    self.status = f"New object type detected: {object_type}"
                    self.events_by_type[object_type] = []
                    self.error_event_by_type[object_type] = None
                    self.last_generation_by_type[object_type] = time.time()
                    self.scaling_factor_by_type[object_type] = self.initial_scaling_factor
                    self.manager.initialize_function(object_type)
                self.events_by_type[object_type].append(event)
                self.update_example_events(object_type, event)
        
        self.logger.log_debug("[STORE_EVENTS] Stopped storing events thread")
        self.alive[0] = False

    def process_events(self):
        self.logger.log_debug("[PROCESS_EVENTS] Started processing events thread")
        while not self.stop:
            events_by_type_copy = copy.deepcopy(self.events_by_type)
            for object_type in events_by_type_copy:
                if self.manager.is_function_ready(object_type):
                    if len(events_by_type_copy[object_type]) > 0:
                        self.logger.log_info(f"[PROCESS_EVENTS] Processing events for object type: {object_type}")
                        while len(events_by_type_copy[object_type]) > 0:
                            event = events_by_type_copy[object_type].pop(0)
                            res, updated_belief_set = self.manager.run_function(object_type, event, copy.deepcopy(self.belief_set))
                            if res:
                                self.belief_set = updated_belief_set
                            else:
                                self.logger.log_error(f"[PROCESS_EVENTS] Error while processing object type: {object_type} with event: {event}")
                                self.status = f"Error while processing object type: {object_type} with event: {event}"
                                self.error_event_by_type[object_type] = event
                                self.manager.remove_function(object_type)
                                break
        
        self.logger.log_debug("[PROCESS_EVENTS] Stopped processing events thread")
        self.alive[1] = False

    def loop(self):
        self.logger.log_debug("[LOOP] Started loop thread")
        while not self.stop:
            events_by_type_copy = copy.deepcopy(self.events_by_type)
            for object_type in events_by_type_copy:
                if self.generation_only_on_error:
                    trigger = not self.manager.is_function_ready(object_type)
                else:
                    trigger = self.error_event_by_type[object_type] is not None or self.threshold(object_type)
                if trigger:
                    self.logger.log_info(f"[LOOP] Generating perception function for object type: {object_type}")
                    self.status = f"Generating perception function for object type: {object_type}"
                    function_string = None
                    error = "error"
                    for i in range(3):
                        if error is not None:
                            function_string, error = self.question_1(object_type, self.get_example_events(object_type), copy.deepcopy(self.belief_set))
                            for j in range(2):
                                if error is not None:
                                    self.logger.log_error(f"[LOOP] Generation attempt {i+1}:{j+1} for object type {object_type} failed with error {error}, retrying...")
                                    self.status = f"Generation attempt {i+1}:{j+1} for object type {object_type} failed, retrying..."
                                    function_string, error = self.question_2(object_type, self.get_example_events(object_type), copy.deepcopy(self.belief_set), function_string, error)

                    if error is None:
                        self.logger.log_info(f"[LOOP] Adding perception function for object type: {object_type}\n{function_string}")
                        self.status = f"Adding perception function for object type: {object_type}"
                        self.manager.add_function(object_type, function_string)
                        self.error_event_by_type[object_type] = None
                        self.last_generation_by_type[object_type] = time.time()
                        self.scaling_factor_by_type[object_type] = self.initial_scaling_factor * self.scaling_factor_multiplier
                    
                    if error is not None:
                        self.logger.log_error(f"[LOOP] Unable to generate perception function for object type: {object_type}")
                        self.status = f"Unable to generate perception function for object type: {object_type}"
                    
        self.logger.log_debug("[LOOP] Stopped loop thread")
        self.alive[2] = False
    
    def question_1(self, object_type, example_events, belief_set):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/perception_question_1.txt'

        elements = [example_events, object_type, belief_set]
        elements_names = ["example_events", "object_type", "belief_set"]
        elements_to_extract = ["function"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="PERCEPTION Q1")
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q1] Error while making request: {error}")
            return None, error
        
        function_string = extracted_elements[0]
        error = self.manager.test_function(function_string, belief_set, example_events)
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q1] Error while testing function: {error}")
            return function_string, error
        
        return function_string, None

    def question_2(self, object_type, example_events, belief_set, function_string, error):
        context_prompt_path = 'agent_dir/prompts/context.txt'
        question_prompt_path = 'agent_dir/prompts/perception_question_2.txt'

        elements = [function_string, error, example_events, object_type, belief_set]
        elements_names = ["function", "error", "example_events", "object_type", "belief_set"]
        elements_to_extract = ["function"]

        extracted_elements, error = self.prompting.make_request(context_prompt_path, question_prompt_path, elements, elements_names, elements_to_extract, tag="PERCEPTION Q2")
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q2] Error while making request: {error}")
            return None, error
        
        function_string = extracted_elements[0]
        error = self.manager.test_function(function_string, belief_set, example_events)
        if error is not None:
            self.logger.log_error(f"[LOOP] [Q2] Error while testing function: {error}")
            return function_string, error
        
        return function_string, None
    
    def threshold(self, object_type):
        events = self.events_by_type[object_type]
        last_generation = self.last_generation_by_type[object_type]
        scaling = self.scaling_factor_by_type[object_type]
        time_elapsed = time.time() - last_generation

        events_den = 3.0 * (math.log(scaling) + 1)
        time_elapsed_den = 2.0 * (math.log(scaling) + 1)
        try:
            return ((len(events) / events_den) + (time_elapsed / time_elapsed_den)) > (1.0 * scaling)
        except:
            return False
    
    def append_event(self, event):
        self.events.append(event)
    
    def update_example_events(self, object_type, event):
        if object_type not in self.example_events_by_type:
            self.example_events_by_type[object_type] = []
        if len(self.example_events_by_type[object_type]) < self.number_example_events:
            self.example_events_by_type[object_type].append(event)
        else:
            self.example_events_by_type[object_type].pop(0)
            self.example_events_by_type[object_type].append(event)
    
    def get_example_events(self, object_type):
        events = self.example_events_by_type[object_type]
        if self.error_event_by_type[object_type] is not None:
            events.append(self.error_event_by_type[object_type])
        return events
    
    def get_control_events(self):
        events = self.control_events
        self.control_events = []
        return events
    
    def get_belief_set(self):
        return copy.deepcopy(self.belief_set)
    
    def get_printable_belief_set(self):
        if not bool(self.belief_set):
            return "Empty"
        out = ""
        for entry in self.belief_set:
            out += f"{entry}: {self.belief_set[entry]}\n"
        return out

    def is_alive(self):
        return any(self.alive)