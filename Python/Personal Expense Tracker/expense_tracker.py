from datetime import date, datetime

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

    category_select = {
        'food': [],
        'transportation': [],
        'utilities': [],
        'entertainment': [],
        'healthcare': [],
        'rent': [],
        'miscs': []
    }

    def category_food_amount():
        food_entry = category_select.__getitem__('food')
        first_entry = food_entry[0]
        food_value = first_entry[0]
        return food_value

    def category_transportation_amount():
        transportation_entry = category_select.__getitem__('transportation')
        first_entry = transportation_entry[0]
        transportation_value = first_entry[0]
        return transportation_value

    def category_utilities_amount():
        utilities_entry = category_select.__getitem__('utilities')
        first_entry = utilities_entry[0]
        utilities_value = first_entry[0]
        return utilities_value

    def category_entertainment_amount():
        entertainment_entry = category_select.__getitem__('entertainment')
        first_entry = entertainment_entry[0]
        entertainment_value = first_entry[0]
        return entertainment_value

    def category_healthcare_amount():
        healthcare_entry = category_select.__getitem__('healthcare')
        first_entry = healthcare_entry[0]
        healthcare_value = first_entry[0]
        return healthcare_value
    
    def category_rent_amount():
        rent_entry = category_select.__getitem__('rent')
        first_entry = rent_entry[0]
        rent_value = first_entry[0]
        return rent_value

    def category_miscs_amount():
        miscs_entry = category_select.__getitem__('miscs')
        first_entry = miscs_entry[0]
        miscs_value = first_entry[0]
        return miscs_value

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

        # LATEST WORK
        # introduction of date input with input validation
        # added date_as_datetime to the print functions
        # created a variable to save date as datetime to be able to store the date
        # formated the format of the datetime using strptime
        # removed the hour from datetime using the .date()
        while True:
            try:
                format = "%b %d, %Y"
                user_date = input("Date (example: oct 17, 2024): ")
                break
            except ValueError:
                return "Enter a valid date."
            
        date_as_datetime = datetime.strptime(user_date, format).date()

        if choice == 1:
            choice = 'food'
            category_select[choice].append((amount, date_as_datetime))
            print(f"${amount} added to {categories[0]}. {date_as_datetime}")
        elif choice == 2:
            choice = 'transportation'
            category_select[choice].append((amount, date_as_datetime))
            print(f"${amount} added to {categories[1]}. {date_as_datetime}")
        elif choice == 3:
            choice = 'utilities'
            category_select[choice].append((amount, date_as_datetime))
            print(f"${amount} added to {categories[2]}. {date_as_datetime}")
        elif choice == 4:
            choice = 'entertainment'
            category_select[choice].append((amount, date_as_datetime))
            print(f"${amount} added to {categories[3]}. {date_as_datetime}")
        elif choice == 5:
            choice = 'healthcare'
            category_select[choice].append((amount, date_as_datetime))
            print(f"${amount} added to {categories[4]}. {date_as_datetime}")
        elif choice == 6:
            choice = 'rent'
            category_select[choice].append((amount, date_as_datetime))
            print(f"${amount} added to {categories[5]}. {date_as_datetime}")
        elif choice == 7:
            choice = 'miscs'
            category_select[choice].append((amount, date_as_datetime))
            print(f"${amount} added to {categories[6]}. {date_as_datetime}")

        option = input("Do you want to add another expense? (Y/N)").lower()

        if option != 'y':
            break
        else: 
            continue
    
    def food_total():
        for food_value in category_food_amount:
            total_value = sum(food_value)
            print(total_value)

    def transportation_total():
        for transportation_value in category_transportation_amount:
            total_value = sum(transportation_value)
            print(total_value)

    def utilities_total():
        for utilities_value in category_utilities_amount:
            total_value = sum(utilities_value)
            print(total_value)

    def entertainment_total():
        for entertainment_value in category_entertainment_amount:
            total_value = sum(entertainment_value)
            print(total_value)

    def healthcare_total():
        for healthcare_value in category_healthcare_amount:
            total_value = sum(healthcare_value)
            print(total_value)

    def rent_total():
        for rent_value in category_rent_amount:
            total_value = sum(rent_value)
            print(total_value)

    def miscs_total():
        for miscs_value in category_miscs_amount:
            total_value = sum(miscs_value)
            print(total_value)

    #food_total = sum(category_food_amount)
    #transportation_total = sum(category_transportation_amount)
    #utilities_total = sum(category_utilities_amount)
    #entertainment_total = sum(category_entertainment_amount)
    #healthcare_total = sum(category_healthcare_amount)
    #rent_total = sum(category_rent_amount)
    #miscs_total = sum(category_miscs_amount)

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
        pass
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