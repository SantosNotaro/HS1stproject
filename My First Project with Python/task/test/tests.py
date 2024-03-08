from hstest import StageTest, TestedProgram, CheckResult, dynamic_test

# Bubblegum: $202.0
# Toffee: $118.0
# Ice cream: $2250.0
# Milk chocolate: $1680.0
# Doughnut: $1075.0
# Pancake: $80.0
#
# Income: $5405.0
# Staff expenses: $4170
# Other expenses: $220
# Net income: $1015

class PrintFirstProject(StageTest):
    @dynamic_test()
    def test_first_project(self):
        pr = TestedProgram()
        output = pr.start().lower().strip()
        if not output:
            return CheckResult.wrong("Your program didn't print any output.")
        if '>' in output:
            return CheckResult.wrong("The greater-than symbol followed by a space (> ) represents the user input "
                                     "in examples. It's not part of the output, so you shouldn’t print this sign")
        if 'earned' not in output.lower():
            return CheckResult.wrong("Your program didn't print the 'Earned amount' line")
        products = {
            "Bubblegum": "202",
            "Toffee": "118",
            "Ice cream": "2250",
            "Milk chocolate": "1680",
            "Doughnut": "1075",
            "Pancake": "80",
        }
        for name in products.keys():
            if name.lower() not in output.lower():
                return CheckResult.wrong(f"Your program should print the '{name}' as an item")
            if products[name].lower() not in output.lower():
                return CheckResult.wrong(f"Incorrect earned amount for {name}.")
        if 'income' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Income' on a separate line")
        if '5405' not in output.lower():
            return CheckResult.wrong("Incorrect total income! Make sure you didn’t print the total income value from"
                                     " the examples, calculate it based on the earnings mentioned in previous stage.")
        if 'staff expenses' not in output.lower():
            return CheckResult.wrong("Your program should ask the user for input with the 'Staff expenses' line")
        if 'other expenses' in output.lower() or 'net income' in output.lower():
            return CheckResult.wrong("When the program has just started, you should not yet print the 'Other expenses' "
                                     "or 'Net income' lines, as no input has been provided yet.")
        if not pr.is_waiting_input():
            return CheckResult.wrong('Your program should ask the user to input the staff expenses')
        output1 = pr.execute('4170').lower().strip()
        if 'other expenses' not in output1:
            return CheckResult.wrong("Your program should ask the user for input with the 'Other expenses' line")
        if not pr.is_waiting_input():
            return CheckResult.wrong('Your program should ask the user to input other expenses')
        output2 = pr.execute('220').lower().strip()
        if 'net income' not in output2:
            return CheckResult.wrong("Your program should print the net income on a separate line")
        if '1015' not in output2.lower():
            return CheckResult.wrong(
                "Incorrect net income! Make sure you didn’t print the net income value from the examples"
                ", calculate it by subtracting expenses provided in the input from the total income")
        return CheckResult.correct()


if __name__ == '__main__':
    PrintFirstProject().run_tests()
