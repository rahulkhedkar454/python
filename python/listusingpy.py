def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if target is found
    return -1  # Return -1 if target is not found

# Example usage:
array = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
target_value = int(input("Enter the value to search for: "))

result = linear_search(array, target_value)

if result != -1:
    print(f"{target_value} found at index {result}.")
else:
    print(f"{target_value} not found in the list.")
