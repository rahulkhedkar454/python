def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
user_input = int(input("Enter a non-negative integer: "))

if user_input < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(user_input)
    print(f"The factorial of {user_input} is: {result}")
