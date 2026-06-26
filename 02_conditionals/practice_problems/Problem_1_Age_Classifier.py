#Program to classify based on age

age=int(input("Enter your age: "))
if age>50:
    print("OLD")
elif age > 25:
    print("YOUNG")
else:
    print("TEEN")  