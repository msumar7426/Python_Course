def generate_username(name,year):
    username=name + year
    return username

name=input("Enter your name: ").strip().lower().split(" ")[0]
year=input("Enter your birth year: ").strip()
username=generate_username(name,year)
print(f"Username will be {username}")