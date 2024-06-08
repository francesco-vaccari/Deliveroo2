from dotenv import load_dotenv
import os
from openai import OpenAI

class Prompting:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI()

    def ask(self, context, question, temperature = 0.7):
        if True:
            print(f"Making request with context: {context} and question: {question} and temperature: {temperature}")
            response = "def process(event, belief_set): return {}"
            print(f"Received response: {response}")
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
    
    def get_prompt(self, prompt_file_path, elements = None, elements_names = None):
        if not os.path.exists(prompt_file_path):
            return ""
        
        with open(prompt_file_path, "r") as file:
            prompt_template = file.read()
        
        if len(elements) != len(elements_names):
            return ""
        
        extracted_elements = []
        for element_name in elements_names:
            start = prompt_template.find(f"```{element_name}```")
            if start == -1:
                return ""
            end = start + len(f"```{element_name}```")
            extracted_elements.append(prompt_template[start:end])
        
        for element, element_name in zip(elements, elements_names):
            prompt_template = prompt_template.replace(f"```{element_name}```", element)

        return prompt_template

    def extract_elements(self, response, elements_to_extract):
        # how do I extract stuff from the response?
        # maybe I specify in the request to put the extracted elements in a specific format
        # I will need to extract functions, sentences, multiple sentences from the same response, boolean values
        
        return ["def process(event, belief_set): return {}"]