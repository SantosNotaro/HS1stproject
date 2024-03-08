# Function to calculate net income
def calculate_net_income(income, staff_expenses, other_expenses):
    return income - staff_expenses - other_expenses

# Item names and corresponding earnings
items = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

# Calculate total income
total_income = sum(items.values())

# Print earned amount for each item
print("Earned amount:")
for item, amount in items.items():
    print(f"{item}: ${amount}")

# Print total income
print("\nIncome:", f"${total_income}")

# Ask for staff expenses
staff_expenses = int(input("Staff expenses: "))

# Ask for other expenses
other_expenses = int(input("Other expenses: "))

# Calculate and print net income
net_income = calculate_net_income(total_income, staff_expenses, other_expenses)
print("Net income:", f"${net_income}")

