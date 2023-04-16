from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

url = 'https://api.openai.com/v1/chat/completions'

prompt = 'Which driver won the 1984 F1 world championship?'
model = 'gpt-3.5-turbo'

response = openai.ChatCompletion.create(
  model=model,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

answer = response['choices'][0]['message']['content']
total_tokens_used = response['usage']['total_tokens']
gpt35turbo_rate_per_1000_tokens = 0.002
gpt35turbo_rate_per_token = gpt35turbo_rate_per_1000_tokens / 1000
cost_in_usd = total_tokens_used * gpt35turbo_rate_per_token
usd_to_jpy_rate = 134
cost_in_yen = cost_in_usd * usd_to_jpy_rate

print(response)
print(answer)
print(total_tokens_used)
print(cost_in_usd)
print(cost_in_yen)
