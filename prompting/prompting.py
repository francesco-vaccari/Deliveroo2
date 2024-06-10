from dotenv import load_dotenv
import os
from openai import OpenAI
import json

class Prompting:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI()

    def ask(self, context, question, temperature = 0.7):
        if True:
            # print(f"CONTEXT:\n{context}\n\nQUESTION:\n{question}")
            
            # parcel
            # response = """{"function": "def update_belief_set(event, belief_set):\n    \n    event_type = event['event_type']\n    object_type = event['object_type']\n    object_data = event['object']\n    object_id = object_data['id']\n    \n    if object_type != 'parcel':\n        return belief_set\n    \n    if event_type == 'object added':\n        belief_set[object_id] = object_data\n    elif event_type == 'object changed':\n        if object_id in belief_set:\n            belief_set[object_id].update(object_data)\n    elif event_type == 'object removed':\n        if object_id in belief_set:\n            del belief_set[object_id]\n    \n    return belief_set"}"""
            
            # map
            # response = """{"function": "def update_belief_set(event, belief_set):\n    event_type = event['event_type']\n    object_type = event['object_type']\n    object_info = event['object']\n    \n    if object_type == 'map':\n        if event_type == 'object added' or event_type == 'object changed':\n            belief_set['map'] = object_info\n        elif event_type == 'object removed':\n            if 'map' in belief_set:\n                del belief_set['map']\n    \n    return belief_set"}"""

            # agent
            # response = """{"function": "def update_belief_set(event, belief_set):\n    \n    if event['event_type'] == 'object added':\n        if event['object_type'] == 'agent':\n            belief_set['agents'] = belief_set.get('agents', [])\n            belief_set['agents'].append(event['object'])\n    elif event['event_type'] == 'object changed':\n        if event['object_type'] == 'agent':\n            agents = belief_set.get('agents', [])\n            for i, agent in enumerate(agents):\n                if agent['id'] == event['object']['id']:\n                    agents[i] = event['object']\n                    break\n    elif event['event_type'] == 'object removed':\n        if event['object_type'] == 'agent':\n            agents = belief_set.get('agents', [])\n            belief_set['agents'] = [agent for agent in agents if agent['id'] != event['object']['id']]\n    return belief_set"}"""

            response = """{}"""
            # print(f"RESPONSE: {response}")

            return response

        try:
            completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": question}
            ],
            temperature = temperature
            )
            return completion.choices[0].message
        except Exception as e:
            return "error"
        # maybe retry if there is an error?
    
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
        question = self.get_prompt(question_path, elements, elements_names)
        response = self.ask(context, question)
        res, extracted_elements, err = self.extract_elements(response, elements_to_extract)
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