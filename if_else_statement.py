user_input = input("Enter a number: ")
number = int(user_input)

if number % 2 == 0:
    print("The number", number, "is Even.")
else:
    print("The number", number, "is Odd.")

try:
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
