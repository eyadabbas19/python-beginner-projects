initial_investment = float(input("How much money are you investing? $"))    
annual_return = float(input("What is the annual return rate as a percentage? "))
def profit(initial_investment, annual_return):
    return initial_investment * (annual_return / 100)
total_capital = initial_investment + profit(initial_investment, annual_return)
print(f"Profit: ${profit(initial_investment, annual_return):.2f}")
print(f"Total Capital: ${total_capital:.2f}")