# logic for conversion
def celsius_fahrenheit(temp):
    return (temp * 9/5) + 32

def celsius_kelvin(temp):
    return temp + 273.15

def fahrenheit_celsius(temp):
    return (temp - 32) * 9/5

def fahrenheit_kelvin(temp):
    return (temp - 32) * 9/5 + 273.15

def kelvin_celsius(temp):
    return temp - 273.15

def kelvin_fahrenheit(temp):
    return (temp - 273.15) * 9/5 +32

# main conversion function
def converter():
    print("Welcome to the temperature conversion app!")
    print("Current available convertions:")
    print("[1] Celsius to Fahrenheit")
    print("[2] Celsius to Kelvin")
    print("[3] Fahrenheit to Celsius")
    print("[4] Fahrenheit to Kelvin")
    print("[5] Kelvin to Celsius")
    print("[6] Kelvin to Fahrenheit")
    print("[7] Exit")
    
    while True:
        try:
            user_choice = int(input("Which option do you desire to perform: "))
            if 1 <= user_choice <= 7:
                pass
            else:
                print("Select a valid option!")
        except ValueError:
            print("Select a valid option!")

        if user_choice == 7:
            print("Thanks for using our app! See you soon.")
            break

        current_temperature = float(input("What's the current temperature? "))

        if user_choice == 1:
            result = celsius_fahrenheit(current_temperature)
            print(f"{current_temperature}ºC is equal to {result}ºF")
        elif user_choice == 2:
            result = celsius_kelvin(current_temperature)
            print(f"{current_temperature}ºC is equal to {result}ºK")
        elif user_choice == 3:
            result = fahrenheit_celsius(current_temperature)
            print(f"{current_temperature}ºF is equal to {result}ºC")
        elif user_choice == 4:
            result = fahrenheit_kelvin(current_temperature)
            print(f"{current_temperature}ºF is equal to {result}ºK")
        elif user_choice == 5:
            result = kelvin_celsius(current_temperature)
            print(f"{current_temperature}ºK is equal to {result}ºC")
        elif user_choice == 6:
            result = kelvin_fahrenheit(current_temperature)
            print(f"{current_temperature}ºK is equal to {result}ºF")
converter()