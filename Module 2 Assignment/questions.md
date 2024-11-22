# Module 2 Questions and Answers

## Question 1: User Input and String Formatting

### Task
Create a program that prompts the user for their first name and prints a welcome message.

### Implementation (Question1.py)
```python
# Prompt the user for their first name
name = input("Enter your first name: ")

# Print the welcome message
print(f"Welcome {name} to Comp 660!")
```

### Screenshot
![Question 1 Output](./Question%201%20Screenshot.png)

---

## Question 2: Understanding Data Types and Operators

### Task
Evaluate different expressions to understand Python's data types and operators.

### Implementation (Question2.py)
```python
# The initial values of length and width in the question.
length = 10.0
width = 7

# Expressions and their evaluations stored in variables, as given in the question
expr1 = width // 2
expr2 = length / 2.0
expr3 = length / 2
expr4 = 1 + 4 * 5

# My answer:

# I decided to use the __name__ property of the type function at the end of the type function
# that then shows the proper English name of the type
# For instance, instead of Type: <class 'int'>, it shows Type: int
# I've used the f string to avoid manual concatenation and formatted each line in the group
# to be in a new line by using the newline character "\n"

# The // operator is used for floor division (integer division).
# It divides width by 2 and returns the largest whole number less than or equal to the result.
print(f"Expression: width // 2\nValue: {expr1}\nType: {type(expr1).__name__}\n")
# The / operator performs floating-point division.
# This means that it divides the two numbers and returns the result as a float,
# even if the division results in a whole number, the result is always a float.
print(f"Expression: length / 2.0\nValue: {expr2}\nType: {type(expr2).__name__}\n")
# Once again, the / operator performs floating-point division.
# It divides length by 2 and returns the result as a float.
print(f"Expression: length / 2\nValue: {expr3}\nType: {type(expr3).__name__}\n")
# This expression involves both addition and multiplication and according to PEMDAS rules,
# multiplication is performed before addition.
print(f"Expression: 1 + 4 * 5\nValue: {expr4}\nType: {type(expr4).__name__}\n")
```

### Screenshot
![Question 2 Output](./Question%202%20Screenshot.png)

### Explanation
The program demonstrates:
1. Floor division (//) vs floating-point division (/)
2. Type conversion and type checking
3. Order of operations (PEMDAS)
4. String formatting with f-strings
5. Different numeric data types in Python

---

## Question 3: Weight Conversion Calculator

### Task
Create a program that converts weight between different units and calculates weight on different celestial bodies.

### Implementation (Question3.py)
```python
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
```

### Screenshot
![Question 3 Output](./Question%203%20Screenshot.png)

### Explanation
The program:
1. Takes user input for mass in pounds
2. Converts pounds to kilograms
3. Calculates weight in Newtons on Earth and Moon
4. Compares weights as a percentage
5. Demonstrates proper rounding vs truncation
6. Uses constants for conversion factors
7. Implements formatted string output
