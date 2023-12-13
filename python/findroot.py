import cmath

def find_roots(a, b, c):
    # Calculate the discriminant
    delta = b**2 - 4*a*c

    # Check the nature of roots
    if delta > 0:
        root1 = (-b + cmath.sqrt(delta)) / (2*a)
        root2 = (-b - cmath.sqrt(delta)) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root,
    else:
        # For complex roots, use cmath.sqrt
        root1 = (-b + cmath.sqrt(delta)) / (2*a)
        root2 = (-b - cmath.sqrt(delta)) / (2*a)
        return root1, root2

# Example usage:
a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

roots = find_roots(a, b, c)

print("Roots of the quadratic equation:")
for root in roots:
    print(f"Root: {root}")
