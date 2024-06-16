import random

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 999:
                return value
            else:
                print("Please enter a 3-digit number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Get two 3-digit integers from the user
num1 = get_input("Enter the first 3-digit integer: ")
num2 = get_input("Enter the second 3-digit integer: ")

# Ensure num1 is less than num2
if num1 > num2:
    num1, num2 = num2, num1

# Generate a random number between num1 and num2
random_number = random.randint(num1, num2)

print(f"A random number between {num1} and {num2} is {random_number}")
