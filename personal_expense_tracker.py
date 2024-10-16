# Client: Google Finance Team ; Due date: October 17 ; Category: MVP

def pet():
    print("Welcome to PET!")
    print("Your Personal Expense Tracker, helping you keep track of your expenses.")
    print("Expenses Categories:")
    print("[1] Food & Groceries")
    print("[2] Transportation (Fuel, Public Transportation, etc...)")
    print("[3] Utilities (Electricity, Water, Internet, etc...)")
    print("[4] Entertainment & Leisure")
    print("[5] Healthcare & Medical Expenses")
    print("[6] Rent & Mortgage")
    print("[7] Miscellaneous (for any uncategorized expenses)")
    
    categories = [
        "Food & Groceries",
        "Transportation (Fuel, Public Transportation, etc...)",
        "Utilities (Electricity, Water, Internet, etc...)",
        "Entertainment & Leisure",
        "Healthcare & Medical Expenses",
        "Rent & Mortgage",
        "Miscellaneous (for any uncategorized expenses)"
    ]

    food = []
    transportation = []
    utilities = []
    entertainment = []
    healthcare = []
    rent = []
    miscs = []

    while True:
        while True:
            try:
                choice = int(input("Select category: "))
                if 1 <= choice <= 7:
                    break
                else:
                    raise ValueError
            except ValueError:
                return "Choose a valid category!"

        while True:
                try:
                    amount = float(input("Amount: "))
                    break
                except ValueError:
                    return "Invalid number! Enter the amount of the expense."

        if choice == 1:
            food.append(amount)
            print(f"${amount} added to {categories[0]}")
        elif choice == 2:
            transportation.append(amount)
            print(f"${amount} added to {categories[1]}")
        elif choice == 3:
            utilities.append(amount)
            print(f"${amount} added to {categories[2]}")
        elif choice == 4:
            entertainment.append(amount)
            print(f"${amount} added to {categories[3]}")
        elif choice == 5:
            healthcare.append(amount)
            print(f"${amount} added to {categories[4]}")
        elif choice == 6:
            rent.append(amount)
            print(f"${amount} added to {categories[5]}")
        elif choice == 7:
            miscs.append(amount)
            print(f"${amount} added to {categories[6]}")

        option = input("Do you want to add another expense? (Y/N)").lower()

        if option != 'y':
            break
        else: 
            continue
    
    food_total = sum(food)
    transportation_total = sum(transportation)
    utilities_total = sum(utilities)
    entertainment_total = sum(entertainment)
    healthcare_total = sum(healthcare)
    rent_total = sum(rent)
    miscs_total = sum(miscs)

    print("Options:")
    print("[1] View total spent")
    print("[2] View total per category")

    while True:
        try:
            show_expenses = int(input("Choose an option: "))
            if 1 <= show_expenses <= 2:
                break
            else:
                raise ValueError
        except ValueError:
            return "Invalid! Insert a valid option."

    if show_expenses == 1:
        total_expenses = food_total + transportation_total + utilities_total + entertainment_total + healthcare_total + rent_total + miscs_total
        print(f"Your total expenses: ${total_expenses}")
    elif show_expenses == 2:
        print(f"{categories[0]} total is: ${food_total}")
        print(f"{categories[1]} total is: ${transportation_total}")
        print(f"{categories[2]} total is: ${utilities_total}")
        print(f"{categories[3]} total is: ${entertainment_total}")
        print(f"{categories[4]} total is: ${healthcare_total}")
        print(f"{categories[5]} total is: ${rent_total}")
        print(f"{categories[6]} total is: ${miscs_total}")
pet()