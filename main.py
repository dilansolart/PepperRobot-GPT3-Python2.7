from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import openai
import os

app = FastAPI()

load_dotenv()

openai.api_key = os.getenv('SECRET_KEY')


class Prompt(BaseModel):
    text: str = Field(min_length=10, max_length=100)

@app.post('/chat')
def generate_response(prompt: Prompt):
    text_length = 1000
    gpt3_model = "text-davinci-003"
    response = openai.Completion.create(
        engine=gpt3_model,
        prompt=prompt.text,
        max_tokens = text_length,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response['choices'][0]['text']