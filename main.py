from chat import ask_question
from token_cost_calculation import calculate_cost
import getch

end = "y"

while end == "y":    
  question = input("\nAsk a question... ")
  response = ask_question(question)

  answer = response['choices'][0]['message']['content']
  total_tokens_used = response['usage']['total_tokens']

  print(f"\n{answer}\n")
  print(f"This answer costs ¥{calculate_cost(total_tokens_used)}.\n")

  print("Continue? (Press y or n)")
  end = getch.getch()

  while end not in ["y", "n"]:
    print("\nInvalid input. Please enter y or n.")
    end = getch.getch()

print("\nGoodbye!")
