# user input
print("Welcome to the temperature conversion app!")
print("Current available convertions:")
print("[1] Celsius to Fahrenheit")
print("[2] Celsius to Kelvin")
print("[3] Fahrenheit to Celsius")
print("[4] Fahrenheit to Kelvin")
print("[5] Kelvin to Celsius")
print("[6] Kelvin to Fahrenheit")

user_choice = int(input("Which option do you desire to perform: "))
current_temperature = float(input("What's the current temperature? "))

# logic for conversion
def celsius_fahrenheit():
    y = (current_temperature * 9/5) + 32
    return y

def celsius_kelvin():
    pass #placeholder

def fahrenheit_celsius():
    pass #placeholder

def fahrenheit_kelvin():
    pass #placeholder

def kelvin_celsius():
    pass #placeholder

def kelvin_fahrenheit():
    pass #placeholder

# main conversion function
def converter():
    while True:
        if user_choice == 1:
            print(celsius_fahrenheit)
            return

# run
converter()