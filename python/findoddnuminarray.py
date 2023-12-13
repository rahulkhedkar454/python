def find_odd_numbers(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    return odd_numbers

# Example usage:
array = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]

odd_numbers_result = find_odd_numbers(array)

print("Odd numbers in the array:", odd_numbers_result)
