from chat import ask_question
from token_cost_calculation import calculate_cost

end = "y"

while end == "y":    
  question = input("Ask a question... ")
  response = ask_question(question)

  answer = response['choices'][0]['message']['content']
  total_tokens_used = response['usage']['total_tokens']

  print(answer)
  print(f"This answer costs ¥{calculate_cost(total_tokens_used)}.")

  end = input("Continue? [y/n] ")

  while end not in ["y", "n"]:
    end = input("Invalid input. Please enter y or n. ")

print('Goodbye!')
