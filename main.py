from chat import ask_question, create_message, insert_message
from token_cost_calculation import calculate_cost

messages=[{"role": "system", "content": "Answer as concisely as possible, unless otherwise instructed."}]

while True:
  question = input('\nType a question.\n(Quit anytime by typing "quit" and hitting enter)\n\n')

  if question.strip() == "quit":
    break

  insert_message(messages, create_message("user", question))
  response = ask_question(messages)

  answer = response['choices'][0]['message']['content']
  total_tokens_used = response['usage']['total_tokens']

  print(f"\n{answer}\n")
  print(f"This answer costs ¥{calculate_cost(total_tokens_used)}.")

  insert_message(messages, create_message("assistant", answer))

print("\nGoodbye!")
