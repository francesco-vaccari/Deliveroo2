import os
import json
from .AzureOpenAIClient import AzureOpenAIClient

class Prompting:
    def __init__(self):
        self.client = AzureOpenAIClient()
        self.counter = 0

    def send_request(self, context, question, temperature = 0.7):
        if self.counter == 0:
            self.counter += 1
            return """{"description": "this is the desire"}"""
        if self.counter == 1:
            self.counter += 1
            return """{"description": "intention number 1", "function": "def process(belief_set):\n    move_up(belief_set)"}"""
        if self.counter == 2:
            self.counter += 1
            return """{"evaluation": "True"}"""
        if self.counter == 3:
            self.counter += 1
            return """{"evaluation": "False"}"""
        if self.counter == 4:
            self.counter += 1
            return """{"description": "Intention number 2 for this desire", "function": "def func(belief_set):\n    move_down(belief_set)"}"""
        if self.counter == 5:
            self.counter += 1
            return """{"evaluation": "True"}"""
        if self.counter == 6:
            self.counter += 1
            return """{"evaluation": "True"}"""
        if self.counter == 7:
            self.counter += 1
            return """{"function": "def trigger(belief_set):\n    import random\n    return random.choice([True, False])"}"""

        

        # response = None
        # max_retries = 3
        # retry = 0
        # while response is None and retry < max_retries:
        #     response = self.client.send_request(context, question, temperature)
        #     retry += 1
        # if response is None:
        #     return "error"
        # return response.choices[0].message.content
        return ""
    
    def get_prompt(self, prompt_file_path, elements = [], elements_names = []):
        if not os.path.exists(prompt_file_path):
            return "error"

        with open(prompt_file_path, "r") as file:
            prompt_template = file.read()
        
        if len(elements) != len(elements_names):
            return "error"
        
        extracted_elements = []
        for element_name in elements_names:
            start = prompt_template.find(f"```{element_name}```")
            if start == -1:
                return "error"
            end = start + len(f"```{element_name}```")
            extracted_elements.append(prompt_template[start:end])
        
        for element, element_name in zip(elements, elements_names):
            prompt_template = self.replace_element(prompt_template, element, element_name)

        return prompt_template

    def replace_element(self, prompt_template, element, element_name):
        if element_name == "example_events":
            string = ""
            for i, event in enumerate(element):
                string += f"Example {i + 1}:\n{event}\n\n"
            prompt_template = prompt_template.replace(f"```{element_name}```", string)
        else:
            prompt_template = prompt_template.replace(f"```{element_name}```", str(element))

        return prompt_template
    
    def make_request(self, context_path, question_path, elements, elements_names, elements_to_extract):
        context = self.get_prompt(context_path)
        if context == "error":
            return False, [], "Error creating context prompt"
        question = self.get_prompt(question_path, elements, elements_names)
        if question == "error":
            return False, [], "Error creating question prompt"
        response = self.send_request(context, question)
        if response == "error":
            return False, [], "Error getting response from OpenAI"
        res, extracted_elements, err = self.extract_elements(response, elements_to_extract)
        if not res:
            return res, extracted_elements, f"Error parsing response: {err}"
        return res, extracted_elements, err

    def extract_elements(self, response, elements_to_extract):
        response = response.replace("\n", "\\n")
        response = response.replace("\t", "\\t")
        
        try:
            response = json.loads(response)
            extracted_elements = []
            for name in elements_to_extract:
                extracted_elements.append(response[name])
        except Exception as e:
            return False, [], e

        return True, extracted_elements, None