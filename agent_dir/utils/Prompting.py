import os
import json
from agent_dir.utils.AzureOpenAIClient import AzureOpenAIClient
from utils.Logger import ExperimentLogger

class Prompting:
    def __init__(self, folder, agent_id):
        self.client = AzureOpenAIClient()
        self.logger = ExperimentLogger(folder, 'prompting.log')
        self.stop = False # change to False when ready to use
        self.requests_made = 0
        self.agent_id = agent_id
    
    def send_request(self, context, question, tag, temperature=0.7):
        log = f"\n[{tag}]\nContext: {context}\nQuestion: {question}\nTemperature: {temperature}"
        if not self.stop:
            response = None
            max_retries = 3
            retry = 0
            while response is None and retry < max_retries:
                response, error = self.client.send_request(context, question, temperature)
                self.requests_made += 1
                retry += 1
                if error is not None:
                    log += f"\nAttempt {retry+1}/{max_retries}\nError: {error}"
            if response is None:
                log += f"\nFailed to get response after {max_retries} attempts."
            else:
                log += f"\nResponse: {response.choices[0].message.content}"
            self.logger.log_info(log)
            try:
                return response.choices[0].message.content
            except Exception as e:
                self.logger.log_error(f"[{tag}] Failed to get response, error: {e}")
                return ""

        self.logger.log_error(f"[{tag}] Prompting is stopped, cannot send request.")
        return ""

    def create_prompt(self, prompt_file_path, elements = [], elements_names = []):
        if not os.path.exists(prompt_file_path):
            raise FileNotFoundError(f"Prompt file not found: {prompt_file_path}")

        with open(prompt_file_path, "r") as file:
            prompt_template = file.read()
        
        if len(elements) != len(elements_names):
            raise ValueError("The number of elements and elements names must be the same")
        
        extracted_elements = []
        for element_name in elements_names:
            start = prompt_template.find(f"```{element_name}```")
            if start == -1:
                raise ValueError(f"Element {element_name} not found in the prompt template")
            end = start + len(f"```{element_name}```")
            extracted_elements.append(prompt_template[start:end])
        
        for element, element_name in zip(elements, elements_names):
            prompt_template = self.replace_element(prompt_template, element, element_name)

        return prompt_template

    def replace_element(self, prompt_template, element, element_name):
        string = ""

        if element_name == "example_events":
            for i, event in enumerate(element):
                string += f"Example {i + 1}:\n{event}\n\n"
        elif element_name == "library":
            for i, (_, intention) in enumerate(element.items()):
                string += f"- {intention.function_name}()\tDescription: {intention.description}\n"
        elif element_name == "actions":
            if len(element) == 0:
                string = "The plan was empty: no actions executed and no events received."
            else:
                for i, (name_action, events) in enumerate(element):
                    string += f"- Action: {name_action} , Events received:\n"
                    if len(events) == 0:
                        string += "None\n"
                    else:
                        for event in events:
                            string += f"\t*  {event}\n"
        elif element_name == "descriptions":
            if len(element) == 0:
                string = "No long term goal has been implemented yet."
            else:
                for i, description in enumerate(element):
                    string += f"- {description}\n"
        elif element_name == "memory":
            if element == "":
                string = "The memory is currently empty."
            else:
                string = str(element)
        else:
            string = str(element)
        
        prompt_template = prompt_template.replace(f"```{element_name}```", string)

        return prompt_template

    def make_request(self, context_path, question_path, elements, elements_names, elements_to_extract, tag):
        context = self.create_prompt(context_path, [self.agent_id], ["id"])
        question = self.create_prompt(question_path, elements, elements_names)
        response = self.send_request(context, question, tag)
        try:
            extracted_elements = self.extract_elements(response, elements_to_extract)
            return extracted_elements, None
        except Exception as e:
            return [], f'Unable to parse JSON, error: {e}'

    def extract_elements(self, response, elements_to_extract):
        response = response.replace("\n", "\\n")
        response = response.replace("\t", "\\t")

        start = response.find("```json")
        end = response.find("```", start + 1)
        if start != -1 and end != -1:
            response = response[start + 7:end]
        
        response = json.loads(response)
        extracted_elements = []
        for name in elements_to_extract:
            extracted_elements.append(response[name])

        return extracted_elements
    
    def get_printable_estimate(self):
        return f"Requests made: {self.requests_made}  Estimated cost: ${self.client.get_cost_estimate()}"
    
    def get_requests_made(self):
        return self.requests_made

    def get_cost_estimate(self):
        return self.client.get_cost_estimate()