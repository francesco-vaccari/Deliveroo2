import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import tiktoken

class AzureOpenAIClient:
    def __init__(self):
        load_dotenv()
        self._validate_env_vars()
        self._configure_openai_api()
        self.input_prompt_lenghts = []
        self.output_prompt_lenghts = []
        self.enc = tiktoken.encoding_for_model("gpt-4")

    def _validate_env_vars(self):
        required_vars = ['AZURE_OPENAI_API_KEY', 'AZURE_OPENAI_ENDPOINT', 'OPENAI_API_VERSION', 'AZURE_OPENAI_DEPLOYMENT_NAME']
        if [var for var in required_vars if var not in os.environ]:
            raise Exception('Missing required environment variables')

    def _configure_openai_api(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("OPENAI_API_VERSION")
        )

    def send_request(self, context, question, temperature):
        try:
            response = self.client.chat.completions.create(
                model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": question}
                ],
                temperature = temperature
            )
            self.input_prompt_lenghts.append(int(response.usage.prompt_tokens)) # input tokens
            self.output_prompt_lenghts.append(int(response.usage.completion_tokens)) # output tokens
            return response, None
        except Exception as e:
            context_length = len(self.enc.encode(context))
            question_length = len(self.enc.encode(question))
            self.input_prompt_lenghts.append(context_length + question_length) # use estimate of number input tokens
            return None, f"Failed request to API: {e}"
    
    def get_estimate(self):
        input_pricing = 0.06 # dollars per 1000 input tokens for a GPT-4 legacy model with 32K context window (worst pricing)
        output_pricing = 0.12 # dollars per 1000 output tokens for a GPT-4 legacy model with 32K context window (worst pricing)
        input_tokens = sum(self.input_prompt_lenghts)
        output_tokens = sum(self.output_prompt_lenghts)
        return input_tokens / 1000 * input_pricing + output_tokens / 1000 * output_pricing




# context = "This is a test."
# question = "Repond with 'test'."

# client = AzureOpenAIClient()
# response = client.send_request(context, question)

# print(response.choices[0].message.content)
# print("\n\n\n")
# print(response)