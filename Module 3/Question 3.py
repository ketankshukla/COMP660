print("What shall I wear today?\n")

name = input("Please Enter Your First Name: ")
temperature = float(input("What is Today's Temperature: "))

if temperature >= 70:
    recommendation = f"Hi {name}, It will be a warm day, T-shirt time!"
else:
    recommendation = f"Hi {name}, You should probably bring a sweater"

print(f"\n{recommendation}")
