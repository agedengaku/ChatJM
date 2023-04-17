from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def askQuestion(question):
  return openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
      {"role": "system", "content": "Answer as concisely as possible, unless otherwise instructed."},
      {"role": "user", "content": question}
    ]
  )