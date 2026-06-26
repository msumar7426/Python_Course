# Program to check if a user is eligible to vote (must be 18 or older)


def is_eligible(age):
    return age >= 18


def main():
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid Age")
    elif is_eligible(age):
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")


main()