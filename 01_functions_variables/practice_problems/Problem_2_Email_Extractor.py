#Extract the name from the email address from a string.

user_email=input("Enter your email address: ").strip()
user_name=user_email.split("@")[0]
print(user_name)