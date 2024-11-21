# Module 3: Control Flow and Decision Making 📚

[← Back to Main Documentation](../../README.md)

## Overview 🎯
Module 3 introduces control flow concepts in Python, focusing on conditional statements, loops, and the pass statement. The assignments demonstrate practical applications of decision-making structures and string manipulation.

## Contents 📋
- [Assignments](#assignments)
  * [Question 1: Control Flow Concepts](#question-1-control-flow-concepts)
  * [Question 2: Pass Statement and String Processing](#question-2-pass-statement-and-string-processing)
  * [Question 3: Temperature-Based Clothing Recommender](#question-3-temperature-based-clothing-recommender)
- [Learning Objectives](#learning-objectives)
- [Implementation Details](#implementation-details)

## Learning Objectives 🎓
- Understand conditional statements (if, elif, else)
- Implement loop structures
- Use the pass statement effectively
- Process strings character by character
- Handle user input with conditions
- Format output based on conditions

## Assignments 📝

### Question 1: Control Flow Concepts
Theoretical understanding of control flow statements in Python.

#### Key Points
- Conditional statements
- Loop structures
- Pass statement usage
- Control flow best practices

### Question 2: Pass Statement and String Processing
A program that demonstrates the use of pass statement and string manipulation.

#### Implementation Details
```python
def process_string(text):
    """
    Process a string by replacing 'z' with spaces and handling special cases.
    
    Args:
        text (str): Input string to process
    
    Example:
        >>> process_string("Hizthere")
        "Hi there"
    """
    result = ""
    for char in text:
        if char == "mn":
            pass  # Demonstrate pass statement
        elif char == "z":
            result += " "  # Replace 'z' with space
        else:
            result += char  # Keep other characters as is
    return result

# Example usage
text = "Hizthere,zThisziszhowzazpasszstatementzworks!"
processed_text = process_string(text)
print(processed_text)
```

#### Key Features
- Demonstrates pass statement usage
- Implements character-by-character processing
- Shows string manipulation techniques
- Uses conditional statements in loops

### Question 3: Temperature-Based Clothing Recommender
A program that recommends clothing based on temperature input.

#### Implementation Details
```python
def get_clothing_recommendation(name, temperature):
    """
    Generate clothing recommendation based on temperature.
    
    Args:
        name (str): User's first name
        temperature (float): Temperature in degrees
        
    Returns:
        str: Personalized clothing recommendation
    """
    if temperature >= 70:
        return f"Hi {name}, It will be a warm day, T-shirt time!"
    else:
        return f"Hi {name}, You should probably bring a sweater"

def main():
    """
    Main program for clothing recommendation system.
    Gets user input and displays personalized recommendation.
    """
    print("What shall I wear today?\n")
    name = input("Please Enter Your First Name: ")
    temperature = float(input("What is Today's Temperature: "))
    
    recommendation = get_clothing_recommendation(name, temperature)
    print(f"\n{recommendation}")
```

#### Key Features
- Takes user input for name and temperature
- Uses conditional logic for recommendations
- Implements personalized messages
- Handles floating-point temperature values

## Implementation Details 🔧

### Control Flow Structures
- if-elif-else statements
- for and while loops
- pass statements
- conditional expressions

### Input Processing
- Type conversion
- Input validation
- Error handling

### Output Formatting
- Conditional output
- String formatting
- User-friendly messages

## Best Practices 📝
1. Use clear conditional statements
2. Implement proper indentation
3. Add descriptive comments
4. Handle edge cases

## Common Issues and Solutions 🤔
1. **Indentation Errors**
   - Issue: Incorrect code blocks
   - Solution: Use consistent indentation

2. **Logic Errors**
   - Issue: Incorrect conditional statements
   - Solution: Test boundary conditions

3. **Input Validation**
   - Issue: Invalid input handling
   - Solution: Add type checking

## Related Resources 📚
1. [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
2. [Python if Statements](https://docs.python.org/3/reference/compound_stmts.html#if)
3. [Python pass Statement](https://docs.python.org/3/reference/simple_stmts.html#pass)

## Code Structure 📂
```
Module 3 Assignment/
├── Question 1.md                           # Control flow concepts
├── Question 2.py                           # Pass statement demo
├── Question 2 Screenshot.png               # Program output
├── Question 3.py                           # Temperature recommender
├── Question 3 - Less Than 70 Degrees.png   # Cold weather output
├── Question 3 - Equal To 70 Degrees.png    # Borderline case output
└── Question 3 - Greater Than 70 Degrees.png # Warm weather output

## Notes 📌
- Temperature values are assumed to be in Fahrenheit
- The pass statement is used for demonstration purposes
- Screenshots show different temperature scenarios
- Input validation could be enhanced for production use

---
Last updated: [Current Date]
