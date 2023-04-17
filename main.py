from chat import ask_question
from token_cost_calculation import calculate_cost

question = input("Ask a question... ")
response = ask_question(question)

answer = response['choices'][0]['message']['content']
total_tokens_used = response['usage']['total_tokens']

print(answer)
print(f"This answer costs ¥{calculate_cost(total_tokens_used)}.")
