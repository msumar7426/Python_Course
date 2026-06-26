# Convert Fahrenheit to Celsius


def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5/9
    return celsius


def main():
    temp_in_fahrenheit = float(input("Enter temp in F: "))
    result = fahrenheit_to_celsius(temp_in_fahrenheit)
    print(f"The temperature in Celsius will be {result:.4f}")

main()