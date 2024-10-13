# input
age = input("What's your age: (years) ")
# conversion
months = int(age) * 12
# print
print(f"You are {age} years old, which is {months} in months.")

'''
Suggestions for Improvement:

Input Validation:
Consider adding a check to ensure the user inputs a valid number (e.g., handle cases where they might enter non-numeric values).
You can use try and except for this.

User Experience:
It might be helpful to specify the units in the input prompt. For example, instead of just asking "What's your age?"
you could say "What's your age in years?".
'''