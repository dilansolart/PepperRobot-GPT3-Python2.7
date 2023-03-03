import requests
from dotenv import load_dotenv
import os

load_dotenv()
secret_api_key = os.getenv('OPENAI_API_KEY')

text_length = 1000
gpt3_model = "text-davinci-003"
text = "Hola, que tal el clima en santa marta?"

url = "https://api.openai.com/v1/completions"
data = {
    "model": gpt3_model,
    "prompt": text,
    "max_tokens": text_length,
    "temperature": 0,
    "top_p": 1,
    "n": 1,
    "stream": False,
    "logprobs": None,
}
headers = {
    "Content-Type": "application/json",
    "Authorization": secret_api_key
}

response = requests.post(url, json = data, headers = headers)

print response.json()['choices'][0]['text']