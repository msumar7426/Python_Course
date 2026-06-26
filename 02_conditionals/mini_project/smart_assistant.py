"""
What would you like to do?

1 Temperature Converter
2 Username Generator
3 Grade Checker
4 Calculator
5 Age Classifier
"""
def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def username_generator(name, year):
    return name + year


def grade_calculator(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def multiply(val1, val2):
    return val1 * val2


def divide(val1, val2):
    return val1 / val2


def age_classifier(age_of_user):
    if age_of_user >= 18:
        return "Eligible to Vote"
    else:
        return "Not Eligible to Vote"


def main():
    print("Enter 1 for temperature Conversion")
    print("Enter 2 for Username Generator")
    print("Enter 3 for Grade Checker")
    print("Enter 4 for Calculator")
    print("Enter 5 for Age Classifier")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Press 1 if you want to convert Celsius to Fahrenheit")
            print("Press 2 if you want to convert Fahrenheit to Celsius")
            conversion_choice = int(input("Enter your choice: "))
            match conversion_choice:
                case 1:
                    temp_in_celsius = float(input("Enter your temp in Celsius: "))
                    temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)
                    print(f"The temperature in Fahrenheit will be {temp_in_fahrenheit}")
                case 2:
                    temp_in_fahrenheit = float(input("Enter your temp in Fahrenheit: "))
                    temp_in_celsius = fahrenheit_to_celsius(temp_in_fahrenheit)
                    print(f"The temperature in Celsius will be {temp_in_celsius}")
                case _:
                    print("Invalid Choice")

        case 2:
            username = input("Enter your username: ").lower().strip().split()[0]
            year = input("Enter the year: ").strip()
            generated_username = username_generator(username, year)
            print(f"The generated username will be {generated_username}")

        case 3:
            course_marks = float(input("Enter your Course Marks: "))
            if course_marks < 0 or course_marks > 100:
                print("Invalid Marks (must be between 0 and 100)")
            else:
                final_grade = grade_calculator(course_marks)
                print(f"The final Grade would be {final_grade}")

        case 4:
            print("Enter 1 for Addition")
            print("Enter 2 for Subtraction")
            print("Enter 3 for Multiplication")
            print("Enter 4 for Division")

            choice_for_operation = int(input("Enter your choice: "))
            match choice_for_operation:
                case 1:
                    num1_for_addition = float(input("Enter 1st number: "))
                    num2_for_addition = float(input("Enter 2nd number: "))
                    result_of_addition = add(num1_for_addition, num2_for_addition)
                    print(f"The result of Addition will be {result_of_addition}")
                case 2:
                    num1_for_subtraction = float(input("Enter 1st number: "))
                    num2_for_subtraction = float(input("Enter 2nd number: "))
                    result_of_subtraction = subtract(num1_for_subtraction, num2_for_subtraction)
                    print(f"The result of Subtraction will be {result_of_subtraction}")
                case 3:
                    num1_for_multiplication = float(input("Enter 1st number: "))
                    num2_for_multiplication = float(input("Enter 2nd number: "))
                    result_of_multiplication = multiply(num1_for_multiplication, num2_for_multiplication)
                    print(f"The result of Multiplication will be {result_of_multiplication}")
                case 4:
                    num1_for_division = float(input("Enter 1st number: "))
                    num2_for_division = float(input("Enter 2nd number: "))
                    if num2_for_division == 0:
                        print("Error: Denominator cannot be zero.")
                    else:
                        result_of_division = divide(num1_for_division, num2_for_division)
                        print(f"The result of Division will be {result_of_division}")
                case _:
                    print("Invalid Choice")

        case 5:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Invalid Age")
            else:
                final_decison = age_classifier(age)
                print(f"The eligibility verdict is {final_decison}")

        case _:
            print("Invalid Choice")


main()



                    

            
            

