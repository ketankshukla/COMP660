# First, prompt the user to enter the mass in pounds and convert it to a float.
mass_lb = float(
    input("Please enter the mass in lb that you would like to convert to kg: ")
)

# Next, convert the mass to kilograms where 1 kg = 2.20462 lbs
mass_kg = mass_lb / 2.20462

# Next, calculate the weight on Earth in Newtons by multiplying the mass by the
# gravitation acceleration on Earth.
weight_earth = mass_kg * 9.807

# Next calculate the weight on the Moon in Newtons, this time by using the gravitational
# acceleration on the Moon.
weight_moon = mass_kg * 1.62

# Next, calculate the percentage of the weight on the Moon compared to Earth
percentage_moon_earth = (weight_moon / weight_earth) * 100

# Finally, convert the percentage to an integer.
# If I had used the int() function to for integer conversion, the output would have been 16, because int simply
# truncates decimal without rounding.
# I used the round() function for integer conversion because it rounds the floating point number to the
# nearest whole number, which is 17 in this case.

percentage_moon_earth_int = round(percentage_moon_earth)

# Results displayed in my PyCharm console:
print(f"The converted mass in kg is: {mass_kg}")
print(f"Your weight on Earth is: {weight_earth} Newtons")
print(f"Your weight on the Moon is: {weight_moon} Newtons")
print(
    f"The percentage of the weight on the Moon in comparison to what is experienced on Earth: {percentage_moon_earth} %"
)
print(
    f"The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer is {percentage_moon_earth_int} %"
)
