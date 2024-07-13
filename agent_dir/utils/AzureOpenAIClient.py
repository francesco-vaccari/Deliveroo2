import os
from dotenv import load_dotenv
from openai import AzureOpenAI

class AzureOpenAIClient:
    def __init__(self):
        load_dotenv()
        self._validate_env_vars()
        self._configure_openai_api()

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
            return response, None
        except Exception as e:
            return None, f"Failed request to API: {e}"



# context = "This is a test."
# question = "Repond with 'test'."

# client = AzureOpenAIClient()
# response = client.send_request(context, question)

# print(response.choices[0].message.content)
# print("\n\n\n")
# print(response)