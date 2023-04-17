GPT35TURBO_RATE_PER_1000 = 0.002
GPT35TURBO_RATE_PER_TOKEN = GPT35TURBO_RATE_PER_1000 / 1000
USD_TO_JPY_RATE = 134

def calculate_cost(num_of_tokens):
    cost_in_usd = num_of_tokens * GPT35TURBO_RATE_PER_TOKEN
    return cost_in_usd * USD_TO_JPY_RATE