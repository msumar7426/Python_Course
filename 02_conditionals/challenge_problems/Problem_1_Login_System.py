username = "msumar"
password = "123456"

username_of_user = input("Enter your Username: ")
password_of_user = input("Enter your password: ")

if username_of_user == username and password_of_user == password:
    print("Login Successful")
else:
    print("Incorrect Credentials")