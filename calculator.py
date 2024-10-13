def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero"

# operations
def calculator():
    print("Welcome to DevSilva Simple Calculator!")

    while True:
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        operator_choice = int(input("Choose a number for the operator: [1]add, [2]subtract, [3]multiply or [4]divide! "))

        if operator_choice == 1:
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif operator_choice == 2:
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif operator_choice == 3:
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif operator_choice == 4:
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            return "Choose a valid operator."

    # replay options
        choice_options = ('y', 'n')
        choice = input("Again? (y/n): ").lower()
        while choice not in choice_options:
            print("Mispelled! Try again...")
            choice = input("Again? (y/n): ").lower()


        if choice != 'y':
            print("Thanks for using our calculator! See you soon.")
            return

calculator()

'''
Suggestions for Improvement:

Input Validation:
Consider adding validation for the numbers entered by the user. If a user inputs a non-integer, it will raise an error.
You could use try and except to handle this.

Output Formatting:
You can improve the output formatting to be more user-friendly by separating the result with a newline or formatting it nicely.

Function for Input Handling:
Consider creating a separate function for handling user input. This could make your main calculator function cleaner and improve
readability.

Loop Control:
Since you're using a while True loop, you might consider removing the inner while loop for the replay option and simply ask the user once for replay, which can
streamline the process.
'''