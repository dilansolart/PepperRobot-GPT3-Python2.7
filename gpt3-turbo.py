import requests
from dotenv import load_dotenv
import os

load_dotenv()
secret_api_key = os.getenv('OPENAI_API_KEY')

text_length = 1000
gpt3_model = "gpt-3.5-turbo"
text = "Hola, que tal el clima en santa marta?"

url = "https://api.openai.com/v1/chat/completions"
data = {
    "model": gpt3_model,
    "max_tokens": text_length,
    "messages": [{"role": "user", "content": text}
                 ]}
headers = {"Authorization": secret_api_key,
           "Content-Type": "application/json"}

response = requests.post(url, json = data, headers = headers)

print response.json()['choices'][0]['message']['content']