"""Provide a clean output of the user name by removing 
any leading space or trailing spaces and converting it to 
lowercase."""

# Problem 1: Clean User Name

clean_name = input("Enter your name: ").strip().lower()

print(clean_name)