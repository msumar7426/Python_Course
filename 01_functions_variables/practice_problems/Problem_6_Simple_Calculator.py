#Simple Calculator

def add(val1,val2):
    added_result=val1+val2
    return added_result

def subtract(val1,val2):
    subtracted_result=val1-val2
    return subtracted_result

def multiply(val1,val2):
    product=val1*val2
    return product

def division(val1,val2):
    division_result=val1/val2
    return division_result

def main():
    number1=float(input("Enter first number: "))
    number2=float(input("Enter second number: "))

    added_result=add(number1,number2)
    subtracted_result=subtract(number1,number2)
    product_result=multiply(number1,number2)
    divided_result=division(number1,number2)

    print(f"The result of Addition will be {added_result}")
    print(f"The result of Subtraction will be {subtracted_result}")
    print(f"The result of Multliplication will be {product_result}")
    print(f"The result of Division will be {divided_result}")
main()