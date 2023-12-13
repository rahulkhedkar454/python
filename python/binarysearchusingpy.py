def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return -1  # Return -1 if target is not found

# Example usage:
array = sorted([int(x) for x in input("Enter a sorted list of integers separated by spaces: ").split()])
target_value = int(input("Enter the value to search for: "))

result = binary_search(array, target_value)

if result != -1:
    print(f"{target_value} found at index {result}.")
else:
    print(f"{target_value} not found in the list.")
