from dotenv import load_dotenv
import os
from openai import OpenAI

class Prompting:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI()

    def ask(self, context, question, temperature = 0.7):
        if True:
            print(f"CONTEXT:\n{context}\n\nQUESTION:\n{question}")
            response = "def process(event, belief_set): return {}"
            print(f"RESPONSE: {response}")
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
            prompt_template = prompt_template.replace(f"```{element_name}```", str(element))

        return prompt_template
    
    def make_request(self, context_path, question_path, elements, elements_names, elements_to_extract):
        context = self.get_prompt(context_path)
        question = self.get_prompt(question_path, elements, elements_names)
        response = self.ask(context, question)
        extracted_elements = self.extract_elements(response, elements_to_extract)
        return extracted_elements

    def extract_elements(self, response, elements_to_extract):
        # how do I extract stuff from the response?
        # maybe I specify in the request to put the extracted elements in a specific format
        # I will need to extract functions, sentences, multiple sentences from the same response, boolean values
        # I need to specify to the LLM a way to let me locate in the response string the elements I want to extract

        # chatgpt suggests something: Provide stuff in the following format: Function: <function> \n Description: <description>
        
        return [response]