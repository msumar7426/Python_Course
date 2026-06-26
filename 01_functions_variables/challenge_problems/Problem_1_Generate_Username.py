def generate_username(name, year):
    return name + year


name = input("Enter your name: ").strip().lower().split()[0]
year = input("Enter your birth year: ").strip()
username = generate_username(name, year)
print(f"Username will be {username}")