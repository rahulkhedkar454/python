def calculate_geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    geometric_mean = product ** (1 / len(numbers))
    return geometric_mean
