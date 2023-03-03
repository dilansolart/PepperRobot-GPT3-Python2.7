import requests
from dotenv import load_dotenv
import os

load_dotenv()
secret_api_key = os.getenv('OPENAI_API_KEY')

def generate_response(text):
    text_length = 1000
    gpt3_model = "gpt-3.5-turbo"

    url = "https://api.openai.com/v1/chat/completions"
    data = {
        "model": gpt3_model,
        "max_tokens": text_length,
        "messages": [{"role": "user", "content": text}]
    }
    headers = {
        "Authorization": secret_api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json = data, headers = headers)
    return response.json()['choices'][0]['message']['content']