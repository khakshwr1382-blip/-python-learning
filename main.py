# Daily Budget Tracker - Version 1.1
name = "Reza"
daily_income = 2000000  # Tomans
expenses = [150000, 85000, 200000]  # Food, transport, etc.

# Calculate total expenses
total_expense = sum(expenses)
remaining_money = daily_income - total_expense

print(f"Hello, {name}!")
print(f"Today's Income: {daily_income:,} Tomans")
print(f"Total Expenses: {total_expense:,} Tomans")
print(f"Remaining Savings: {remaining_money:,} Tomans")

# Financial status check
if remaining_money > 1000000:
    print("Status: Excellent! Capital accumulation is positive.")
else:
    print("Status: Warning! You need to control your expenses.")
