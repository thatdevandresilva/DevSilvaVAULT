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

def calculator():
    print("Welcome to DevSilva Simple Calculator!")
    print("Operations:")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")

    while True:
        try:
            operator_choice = int(input("Which operation you desire to perform: "))
            if 1 <= operator_choice <= 4:
                break
            else:
                raise ValueError
        except ValueError:
            print("Select a valid option.")

    while True:
        try:
            num1 = int(input("First Number: "))
            num2 = int(input("Second Number: "))
            break
        except ValueError:
            print("The value needs to be numeric..")

    if operator_choice == 1:
        print(f"Result:\n{num1} + {num2} = {add(num1, num2)}")
    elif operator_choice == 2:
        print(f"Result:\n{num1} - {num2} = {subtract(num1, num2)}")
    elif operator_choice == 3:
        print(f"Result:\n{num1} * {num2} = {multiply(num1, num2)}")
    elif operator_choice == 4:
        print(f"Result:\n{num1} / {num2} = {divide(num1, num2)}")
    replay()

def replay():
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

calculator()