def abbreviate_middle_name(full_name):
   name_parts = [part.capitalize() for part in full_name.split()]

   # If there's only one name part, return it as is
   if len(name_parts) == 1:
      return name_parts[0]

   # If there are two parts (first and last), return them as is
   if len(name_parts) == 2:
      return f"{name_parts[0]} {name_parts[1]}"

   # Otherwise, abbreviate the middle name(s)
   first_name = name_parts[0]
   last_name = name_parts[-1]
   middle_names = " ".join([f"{name[0].upper()}." for name in name_parts[1:-1]])

   return f"{first_name} {middle_names} {last_name}"

full_name = input("Enter your full name: ").lower()

print(f"Abbreviated name is: {abbreviate_middle_name(full_name)}")
