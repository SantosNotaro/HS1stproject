# Earned Amount
bubblegum = float(input("Bubblegum: ").replace('$', '').replace(',', ''))
toffee = float(input("Toffee: ").replace('$', '').replace(',', ''))
icecream = float(input("Ice Cream: ").replace('$', '').replace(',', ''))
milkchocolate = float(input("Milk Chocolate: ").replace('$', '').replace(',', ''))
doughnut = float(input("Doughnut: ").replace('$', '').replace(',', ''))
pancake = float(input("Pancake: ").replace('$', '').replace(',', ''))

# Expenses
staffexpenses = float(input("How much are staff expenses?: ").replace('$', '').replace(',', ''))
otherexpenses = float(input("How much are other expenses?: ").replace('$', '').replace(',', ''))

# Net Income
income = bubblegum + toffee + icecream + milkchocolate + doughnut + pancake
net_income = income - staffexpenses - otherexpenses

# print
print()
print("Earned Amount: ")
print("Bubblegum: $", bubblegum)
print("Toffee: $", toffee)
print("Ice Cream: $", icecream)
print("Milk Chocolate: $", milkchocolate)
print("Doughnut: $", doughnut)
print("Pancake: $", pancake)
print()
print("Income: $", income)
print("Staff Expenses: $", staffexpenses)
print("Other Expenses: $", otherexpenses)
print("Your Net Income: $", net_income)