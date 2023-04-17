from dotenv import load_dotenv
from token_cost_calculation import calculate_cost
import os
import openai

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

question = input("Ask a question... ")

response = openai.ChatCompletion.create(
  model='gpt-3.5-turbo',
  messages=[
    {"role": "system", "content": "Answer as concisely as possible, unless otherwise instructed."},
    {"role": "user", "content": question}
  ]
)

answer = response['choices'][0]['message']['content']
total_tokens_used = response['usage']['total_tokens']

print(answer)
print(f"This answer costs ¥{calculate_cost(total_tokens_used)}.")
