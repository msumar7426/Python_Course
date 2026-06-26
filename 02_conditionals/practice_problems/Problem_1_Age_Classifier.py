# Program to classify based on age

age = int(input("Enter your age: "))
if age < 0:
    print("Invalid Age")
elif age > 50:
    print("OLD")
elif age > 25:
    print("YOUNG")
elif age >= 13:
    print("TEEN")
else:
    print("CHILD")  