# Module 2: Input/Output and Basic Operations 📚

[← Back to Main Documentation](../../README.md)

## Overview 🎯
This module focuses on input/output operations and basic mathematical calculations in Python. Students learn to handle user input, perform calculations, and format output appropriately.

## Contents 📋
- [Learning Objectives](#learning-objectives)
- [Assignments](#assignments)
  * [Question 1: User Input and Output](#question-1-user-input-and-output)
  * [Question 2: Expressions and Types](#question-2-expressions-and-types)
  * [Question 3: Weight Conversion Calculator](#question-3-weight-conversion-calculator)
- [Implementation Details](#implementation-details)
- [Best Practices](#best-practices)
- [Common Issues and Solutions](#common-issues-and-solutions)

## Learning Objectives 🎓
- Handle user input effectively
- Perform basic mathematical operations
- Understand type conversion
- Format output for readability
- Implement unit conversion calculations

## Assignments 📝

### Question 1: User Input and Output
Create a program that takes user input and displays a welcome message.

**Implementation:**
```python
# Prompt the user for their first name
name = input("Enter your first name: ")

# Print the welcome message
print(f"Welcome {name} to Comp 660!")
```

### Question 2: Expressions and Types
Evaluate different expressions and understand their types.

**Implementation:**
```python
# The initial values of length and width in the question.
length = 10.0
width = 7

# Expressions and their evaluations stored in variables
expr1 = width // 2
expr2 = length / 2.0
expr3 = length / 2
expr4 = 1 + 4 * 5

# Print expressions and their types
print(f"Expression: width // 2\nValue: {expr1}\nType: {type(expr1).__name__}\n")
print(f"Expression: length / 2.0\nValue: {expr2}\nType: {type(expr2).__name__}\n")
print(f"Expression: length / 2\nValue: {expr3}\nType: {type(expr3).__name__}\n")
print(f"Expression: 1 + 4 * 5\nValue: {expr4}\nType: {type(expr4).__name__}\n")
```

### Question 3: Weight Conversion Calculator
Create a program that converts weight between pounds and kilograms and calculates weight on Earth vs Moon.

**Implementation:**
```python
# Get mass in pounds and convert to kilograms
mass_lb = float(input("Please enter the mass in lb that you would like to convert to kg: "))
mass_kg = mass_lb / 2.20462

# Calculate weights on Earth and Moon
weight_earth = mass_kg * 9.807
weight_moon = mass_kg * 1.62

# Calculate percentage of weight on Moon compared to Earth
percentage_moon_earth = (weight_moon / weight_earth) * 100
percentage_moon_earth_int = round(percentage_moon_earth)

# Display results
print(f"The converted mass in kg is: {mass_kg}")
print(f"Your weight on Earth is: {weight_earth} Newtons")
print(f"Your weight on the Moon is: {weight_moon} Newtons")
print(f"The percentage of the weight on the Moon compared to Earth: {percentage_moon_earth} %")
print(f"The percentage as an integer: {percentage_moon_earth_int} %")
```

## Implementation Details 🔧

### Input Handling
- Use appropriate input prompts
- Validate numeric input
- Handle type conversion safely

### Calculations
- Use correct mathematical operators
- Apply proper order of operations
- Maintain precision in calculations

### Output Formatting
- Use f-strings for formatted output
- Round numbers appropriately
- Present results clearly

## Best Practices 📝
1. Validate user input
2. Use meaningful variable names
3. Add descriptive comments
4. Format output for readability

## Common Issues and Solutions 🤔
1. **Input Validation**
   - Issue: Invalid input crashes program
   - Solution: Add try-except blocks

2. **Type Conversion**
   - Issue: String to float conversion errors
   - Solution: Validate input before conversion

3. **Calculation Precision**
   - Issue: Floating point precision errors
   - Solution: Use round() function appropriately

## Related Resources 📚
1. [Python Input/Output](https://docs.python.org/3/tutorial/inputoutput.html)
2. [Python Type Conversion](https://docs.python.org/3/library/functions.html#float)
3. [Python String Formatting](https://docs.python.org/3/library/string.html#formatstrings)
