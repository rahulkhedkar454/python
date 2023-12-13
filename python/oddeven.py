def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

# Example usage:
user_input = int(input("Enter a number: "))
check_even_or_odd(user_input)
