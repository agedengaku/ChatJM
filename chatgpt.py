from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')
url = 'https://api.openai.com/v1/chat/completions'
model = 'gpt-3.5-turbo'

question = input("Ask a question... ")

response = openai.ChatCompletion.create(
  model=model,
  messages=[
    {"role": "user", "content": question}
  ]
)

answer = response['choices'][0]['message']['content']
total_tokens_used = response['usage']['total_tokens']
gpt35turbo_rate_per_1000_tokens = 0.002
gpt35turbo_rate_per_token = gpt35turbo_rate_per_1000_tokens / 1000
cost_in_usd = total_tokens_used * gpt35turbo_rate_per_token
usd_to_jpy_rate = 134
cost_in_yen = cost_in_usd * usd_to_jpy_rate

print(answer)
print(f"This answer costs ¥{cost_in_yen}.")
