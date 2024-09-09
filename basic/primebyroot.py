import math

def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False
    # Check for factors up to the square root of the number
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
try:
    user_input = int(input("Enter a number to check if it is prime: "))
    # Check if the input number is prime
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
