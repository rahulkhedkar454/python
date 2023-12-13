def celsius_to_fahrenheit(celsius):
    # Formula: (Celsius * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius_temperature = float(input("Enter temperature in degrees Celsius: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")
