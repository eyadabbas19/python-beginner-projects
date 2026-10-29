monthly_budget = float(input("Enter your monthly budget: "))
if monthly_budget <= 0:
    print("Please enter a valid budget greater than 0.")
    exit()
expense1_name = input("Enter the name of your first expense: ")
expense1_amount = float(input(f"Enter the amount for {expense1_name}: $"))
expense2_name = input("Enter the name of your second expense: ")
expense2_amount = float(input(f"Enter the amount for {expense2_name}: $"))
expense3_name = input("Enter the name of your third expense: ")
expense3_amount = float(input(f"Enter the amount for {expense3_name}: $"))
total_expenses = expense1_amount + expense2_amount + expense3_amount
print( "------Monthly Summary------")
print(f"Your total expenses are: ${total_expenses:.2f}")
remaining_budget = monthly_budget - total_expenses
print(f"Remaining budget: ${remaining_budget:.2f}")
percentage_remaining = (remaining_budget / monthly_budget) * 100
print(f"Percentage of budget remaining: {percentage_remaining:.2f}%")
if remaining_budget < 0:
    print(f"You are over budget by ${-remaining_budget:.2f}.")
elif remaining_budget == 0:
    print("You have exactly met your budget.")
else:
    print(f"You are within budget.You have ${remaining_budget:.2f} left in your budget.")