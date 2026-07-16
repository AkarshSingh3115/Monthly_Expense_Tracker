# STEP 2: Monthly Expense Tracker with Categories & Goal

print("Monthly Expense Tracker")

income = float(input("Enter your monthly income: "))
goal = float(input("Enter your savings goal: "))

# Ask for number of expense categories
num_categories = int(input("How many expense categories? "))

expenses = {}
total_expense = 0

for i in range(num_categories):
    category = input(f"Enter category {i+1} name: ")
    amount = float(input(f"Enter expense for {category}: "))
    expenses[category] = amount
    total_expense += amount

savings = income - total_expense

print("\n--- Summary ---")
print("Income =", income)
print("Expenses Breakdown:")
for cat, amt in expenses.items():
    print(f"  {cat}: {amt}")
print("Total Expenses =", total_expense)
print("Savings =", savings)

if savings > 0:
    print("Good! You saved money this month.")
    if savings >= goal:
        print(" Congrats! You met your savings goal.")
    else:
        print("Keep pushing! You didn’t reach your goal.")
elif savings == 0:
    print("No savings this month.")
else:
    print(" Warning! You spent more than you earned.")

print("\nProgram completed successfully!")
input("Press Enter to exit...")
