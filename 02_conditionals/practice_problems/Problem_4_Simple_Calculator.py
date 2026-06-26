def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def multiply(val1, val2):
    return val1 * val2


def division(val1, val2):
    return val1 / val2


def main():
    print("Press 1 for + , 2 for - , 3 for * and 4 for /")
    choice = int(input("Enter your choice: "))
    print(f"You have successfully selected operation number {choice}")
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    match choice:
        case 1:
            added_result = add(number1, number2)
            print(f"The result of Addition will be {added_result}")

        case 2:
            subtracted_result = subtract(number1, number2)
            print(f"The result of Subtraction will be {subtracted_result}")

        case 3:
            product_result = multiply(number1, number2)
            print(f"The result of Multiplication will be {product_result}")

        case 4:
            if number2 == 0:
                print("Error: Denominator cannot be zero.")
            else:
                divided_result = division(number1, number2)
                print(f"The result of Division will be {divided_result}")

        case _:
            print("Invalid Choice")


main()