from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv('CHATGPT_API_KEY')
url = 'https://api.openai.com/v1/chat/completions'

prompt = 'Hello, ChatGPT!'
payload = {
    'model': 'gpt-3.5-turbo',
    'messages': [{'role': 'user', 'content': prompt}],
    'max_tokens': 10,
    'temperature': 0.5,
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

response = requests.post(url, json=payload, headers=headers)
response_data = response.json()

generated_text = response_data['choices'][0]['message']['content']
print(generated_text)
