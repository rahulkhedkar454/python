def calculate_average(numbers):
    if not numbers:
        return "Cannot calculate average for an empty set."

    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
num_list = [int(x) for x in input("Enter a set of integers separated by spaces: ").split()]
average_result = calculate_average(num_list)

print(f"The average of the given set of integers is: {average_result:.2f}")
