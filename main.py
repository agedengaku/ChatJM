from chat import ask_question, create_message, insert_message
from token_cost_calculation import calculate_cost
import getch

end = "y"

messages=[{"role": "system", "content": "Answer as concisely as possible, unless otherwise instructed."}]

while end == "y":
  question = input("\nAsk a question: ")
  insert_message(messages, create_message("user", question))
  response = ask_question(messages)

  answer = response['choices'][0]['message']['content']
  total_tokens_used = response['usage']['total_tokens']

  print(f"\n{answer}\n")
  print(f"This answer costs ¥{calculate_cost(total_tokens_used)}.\n")
  
  print("Continue? (Press y or n)")
  end = getch.getch()

  insert_message(messages, create_message("assistant", answer))

  while end not in ["y", "n"]:
    print("\nInvalid input. Please enter y or n.")
    end = getch.getch()

print("\nGoodbye!")
