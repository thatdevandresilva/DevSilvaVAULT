# main menu
def main_menu():
    print("Welcome to BaseFinance")
    print("Which action do you desire to make?")
    print("[1] Add transaction")
    print("[2] View transactions")
    print("[3] Save transactions")
    print("[4] Load transactions")
    print("[5] Exit")

# logic for user choices
def add_transaction():
    # logice for adding a transaction
    pass

def view_transaction():
    # logic for viewing transactions
    pass

def save_transaction():
    # logic for saving transactions
    pass

def load_transaction():
    # logic for loading transactions
    pass

# main application
def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ").lower()

        if choice == "1":
            pass # placeholder for add transaction
        elif choice == "2":
            pass # placeholder for view transactions
        elif choice == "3":
            pass # placeholder for save transactions
        elif choice == "4":
            pass # placeholder for load transactions
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Select the number of the action you desire to make!")
            choice = input("Enter your choice: ").lower()

if __name__ == "__main__":
    main()