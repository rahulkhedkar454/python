def calculate_triangle_area(side1, side2, side3):
    # Calculate semi-perimeter
    s = (side1 + side2 + side3) / 2

    # Calculate area using Heron's formula
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area

# Example usage:
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

triangle_area = calculate_triangle_area(side1, side2, side3)
print(f"The area of the triangle is: {triangle_area:.2f} square units.")
