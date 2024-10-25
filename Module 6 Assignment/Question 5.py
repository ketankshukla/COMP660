def get_name_input(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name.capitalize()
        else:
            print("Input cannot be blank. Please try again.")

first_name = get_name_input("What is your first name? ")
last_name = get_name_input("What is your last name? ")

print(f"\nHi {first_name.title()} {last_name.title()}, welcome to my Python greet application!")
