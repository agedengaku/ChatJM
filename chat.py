from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def ask_question(messages):
  return openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages
  )

def create_message(role, content):
  return {"role": role, "content": content}

def insert_message(messages, new_message):
  messages.append(new_message)