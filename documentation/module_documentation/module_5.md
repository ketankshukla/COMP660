# Module 5: Functions and Recursion 📚

[← Back to Main Documentation](../../README.md)

## Overview 🎯
Module 5 focuses on functions, recursion, and mathematical computations in Python. The assignments cover recursive algorithms, lambda functions, and practical mathematical applications.

## Learning Objectives 🎓
- Understand and implement recursive functions
- Work with lambda functions
- Perform mathematical calculations
- Handle edge cases and errors
- Format output appropriately

## Assignments 📝

### Question 1: Function Concepts
Theoretical understanding of Python functions and their implementation.

#### Key Points
- Function definition syntax
- Parameters and arguments
- Return values
- Function documentation

### Question 2: Factorial Calculator
A recursive function to calculate the factorial of a number.

#### Implementation Details
```python
def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): Non-negative integer to calculate factorial
        
    Returns:
        int: Factorial of n
        
    Example:
        >>> factorial(4)
        24
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

#### Key Features
- Recursive implementation
- Input validation
- Interactive user interface
- Error handling

### Question 3: Sum of Integers
A recursive function to calculate the sum of first n integers.

#### Implementation Details
```python
def sum_nint(n):
    """
    Calculate sum of first n integers using recursion.
    
    Args:
        n (int): Number of integers to sum
        
    Returns:
        int: Sum of integers from 1 to n
        
    Example:
        >>> sum_nint(3)
        6  # 1 + 2 + 3
    """
    if n == 0:
        return 0
    return n + sum_nint(n - 1)
```

#### Key Features
- Recursive summation
- Positive integer validation
- User-friendly interface
- Clear output formatting

### Question 4: String Reversal
A recursive function to reverse a string.

#### Implementation Details
```python
def semordnilap(aString, index):
    """
    Recursively print a string in reverse order.
    
    Args:
        aString (str): String to reverse
        index (int): Current position in string
        
    Example:
        >>> semordnilap("hello", 0)
        olleh
    """
    if index < len(aString):
        semordnilap(aString, index + 1)
        print(aString[index], end="")
```

#### Key Features
- Recursive string processing
- Character-by-character output
- Input validation
- Interactive program flow

### Question 5: Lambda Functions
Implementation of simple lambda functions.

#### Implementation Details
```python
mirror_lambda = lambda a: a

# Example usage
print(mirror_lambda(5))         # 5
print(mirror_lambda("hello"))   # "hello"
print(mirror_lambda([1,2,3]))   # [1,2,3]
```

#### Key Features
- Lambda function syntax
- Single-parameter function
- Multiple data type support
- Simple return operation

### Question 6: Circle Area Calculator
A function to calculate the area of a circle.

#### Implementation Details
```python
def area_circle(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): Radius of the circle
        
    Returns:
        float: Area of the circle
        
    Example:
        >>> area_circle(2)
        12.57  # π * 2²
    """
    return math.pi * radius ** 2
```

#### Key Features
- Mathematical formula implementation
- Floating-point calculations
- Input validation
- Formatted output

### Question 7: Advanced Functions
{{ ... }}

### Question 8: Complex Calculations
{{ ... }}

## Code Structure 
```
Module 5 Assignment/
├── Question 1.md       # Function concepts
├── Question 2.py       # Factorial calculator
├── Question 3.py       # Sum of integers
├── Question 4.md       # String reversal explanation
├── Question 4.py       # String reversal implementation
├── Question 5.py       # Lambda functions
├── Question 6.py       # Circle area calculator
└── Question 8.py       # Complex calculations
```

## Best Practices 
1. Function Design
   - Clear parameter names
   - Comprehensive docstrings
   - Single responsibility principle
   - Input validation

2. Recursion
   - Base case handling
   - Stack depth consideration
   - Clear termination conditions
   - Efficient implementations

3. Error Handling
   - Input validation
   - Type checking
   - User-friendly messages
   - Graceful error recovery

## Common Issues and Solutions 
1. Recursion Depth
   ```python
   # Set recursion limit if needed
   import sys
   sys.setrecursionlimit(1500)
   ```

2. Input Validation
   ```python
   def validate_input(value):
       try:
           num = float(value)
           return num > 0
       except ValueError:
           return False
   ```

3. Floating Point Precision
   ```python
   # Round results for display
   area = round(math.pi * radius**2, 2)
   ```

## Related Resources 
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Recursion in Python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

## Notes 
- Recursion requires careful consideration of base cases
- Lambda functions are best for simple operations
- Mathematical calculations should handle edge cases
- User input should always be validated

---
Last updated: [Current Date]
