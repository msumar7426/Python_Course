"""Convert Temperature from Celsius to Fahrenheit"""

def c_to_f(temp):
    return (temp * 9/5) + 32


def main():
    temp_in_celsius = float(input("Enter the temp in Celsius: "))
    result = c_to_f(temp_in_celsius)
    print(f"The temperature in Fahrenheit will be {result:.4f}")

main()