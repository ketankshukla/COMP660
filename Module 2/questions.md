[Back to README](../README.md)

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

### Sample Output
```
Enter your first name: John
Welcome John to Comp 660!
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

### Sample Output
```
Expression: width // 2
Value: 3
Type: int

Expression: length / 2.0
Value: 5.0
Type: float

Expression: length / 2
Value: 5.0
Type: float

Expression: 1 + 4 * 5
Value: 21
Type: int
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

### Sample Output
```
Please enter the mass in lb that you would like to convert to kg: 100
The converted mass in kg is: 45.35923700000001
Your weight on Earth is: 444.79568639000005 Newtons
Your weight on the Moon is: 73.48196994000001 Newtons
The percentage of the weight on the Moon in comparison to what is experienced on Earth: 16.520467836257308 %
The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer is 17 %
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

---

# Discussion

## How is Python interpreted from source code?

The source code in Python is written in .py files using text that is readable by humans
and follows Python's syntax rules.

When a Python script is run, the Python interpreter first compiles the code in the .py file
into another form known as bytecode.

This intermediate form is a lower-level, platform-independent set of instructions specific to
the Python Virtual Machine (PVM), but it is not directly executable by the hardware.

The compiled bytecode is stored in .pyc files in the __pycache__ directory, allowing the interpreter
to skip the compilation step if the source code hasn't changed in subsequent executions.

When the script is executed, the PVM reads the compiled bytecode and executes it line-by-line.
This step is where the program actually runs, with the PVM interpreting the bytecode instructions
and interacting with the computer's hardware and operating system. The PVM is part of the runtime
environment and acts as the interpreter, rather than compiling the code directly into machine-specific instructions,
which is why Python is known as an interpreted language.

Before bytecode is generated, the interpreter performs several steps.
First, it breaks down the source code into a series of tokens.
These are the smallest building blocks of the code, including keywords, operators, identifiers, and literals.
The tokens are then passed to a parser, which arranges them into an Abstract Syntax Tree (AST) representing the
code's structure according to Python's syntax rules. At this point, the interpreter checks for syntax errors to
ensure the code is well-formed.

Once the AST is created, the interpreter carries out semantic analysis to verify the logical correctness of the code,
checking things like variable scope and type mismatches. After passing these checks, the AST is compiled into bytecode,
which is then stored in .pyc files. By compiling to this intermediate form, Python can use the cached bytecode for
future runs, making execution faster.

The final step involves the PVM interpreting the bytecode.
It executes each instruction one by one, interacting with the system's resources as needed.
Some Python implementations, like PyPy, include a Just-In-Time (JIT) compiler, which further optimizes the
execution by translating bytecode into machine code at runtime. This can significantly speed up the performance
for frequently executed code segments.

This entire process, from source code to bytecode compilation and interpretation by the PVM,
makes Python a flexible and portable language. The use of bytecode allows the same Python code to run on different
operating systems, and the caching mechanism speeds up subsequent executions. Additionally, Python's interpreted
nature provides ease of debugging, as errors can be caught and corrected during runtime.
