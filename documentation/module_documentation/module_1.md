# Module 1: Introduction to Python Programming 📚

[← Back to Main Documentation](../../README.md)

## Overview 🎯
Module 1 introduces fundamental Python programming concepts through a series of exercises focused on mathematical operations, variable assignments, and basic program execution. The module includes both theoretical questions and practical programming tasks.

## Contents 📋
- [Assignments](#assignments)
  * [Question 1: Python Environment Setup](#question-1-python-environment-setup)
  * [Question 2: Python Basics](#question-2-python-basics)
  * [Question 3: Mathematical Operations](#question-3-mathematical-operations)
  * [Question 4: Linear Equation Calculation](#question-4-linear-equation-calculation)
- [Learning Objectives](#learning-objectives)
- [Implementation Details](#implementation-details)

## Learning Objectives 🎓
- Set up a Python development environment
- Understand basic Python syntax and structure
- Execute simple Python programs
- Apply mathematical operations in Python
- Work with variables and basic data types
- Interpret program output

## Assignments 📝

### Question 1: Python Environment Setup
Documentation of Python installation and environment configuration process.

#### Key Points
- Python version requirements
- IDE selection and setup
- Running first Python program
- Verifying installation success

### Question 2: Python Basics
Introduction to fundamental Python concepts and syntax.

#### Key Points
- Basic syntax rules
- Variable declaration
- Data types
- Print statements
- Comments

### Question 3: Mathematical Operations
Understanding mathematical operations and operator precedence in Python.

#### Key Points
- Basic arithmetic operators
- Order of operations (PEMDAS)
- Expression evaluation
- Variable assignment

### Question 4: Linear Equation Calculation
A Python program that calculates the y-value of a linear equation.

#### Implementation Details
```python
def calculate_y_value(x):
    """
    Calculate y-value using the equation: y = (-1/4)*(x-1)+3
    
    Args:
        x (float): x-coordinate value
    
    Returns:
        float: calculated y-coordinate value
    """
    return (-1/4)*(x-1)+3

# Example usage
x = 0
y = calculate_y_value(x)
print(y)  # Output: 3.25
```

#### Key Features
- Uses linear equation: y = (-1/4)*(x-1)+3
- Demonstrates order of operations
- Shows variable assignment
- Implements mathematical calculations

#### Step-by-Step Evaluation
1. Variable assignment: x = 0
2. Substitution: y = (-1/4)*(0-1)+3
3. Parentheses evaluation: y = (-1/4)*(-1)+3
4. Multiplication: y = 1/4+3
5. Addition: y = 3.25

## Code Structure 📂
```
Module 1 Assignment/
├── Question 1.md       # Environment setup documentation
├── Question 2.md       # Python basics documentation
├── Question 3.md       # Mathematical operations
├── Question 4.md       # Linear equation problem description
├── Question 4.py       # Linear equation implementation
└── graph.png          # Visual representation of the equation
```

## Best Practices 💡
1. Code Organization
   - Clear variable names
   - Proper indentation
   - Descriptive comments

2. Documentation
   - Detailed problem descriptions
   - Step-by-step solutions
   - Visual aids when applicable

3. Mathematical Concepts
   - Follow order of operations
   - Show calculation steps
   - Verify results

## Common Issues and Solutions ⚠️
1. Environment Setup
   - Ensure correct Python version
   - Verify PATH environment variables
   - Test installation with simple programs

2. Mathematical Operations
   - Pay attention to operator precedence
   - Use parentheses for clarity
   - Verify calculations step by step

## Related Resources 🔗
- [Python Official Documentation](https://docs.python.org/3/)
- [Mathematical Operations in Python](https://docs.python.org/3/tutorial/introduction.html#numbers)
- [Python Programming Basics](https://docs.python.org/3/tutorial/index.html)

## Notes 📌
- All programs should be run using Python 3.x
- Mathematical operations follow standard PEMDAS rules
- Visual aids (graphs) help understand mathematical concepts

**Additional Example Implementation:**
```python
x = 0
y = (-1 / 4) * (x - 1) + 3
print(y)
```

## Implementation Details 🔧

### Environment Setup
1. Install Python 3.x
2. Configure PyCharm IDE
3. Set up project structure

### Code Structure
- Clear variable names
- Proper indentation
- Consistent formatting

### Testing
- Test with different input values
- Verify output accuracy
- Debug any issues

## Best Practices 📝
1. Use descriptive variable names
2. Add comments for clarity
3. Follow PEP 8 style guide
4. Test code thoroughly

## Common Issues and Solutions 🤔
1. **Python Installation**
   - Issue: Path not set correctly
   - Solution: Add Python to system PATH

2. **IDE Configuration**
   - Issue: Interpreter not found
   - Solution: Configure Python interpreter in PyCharm

3. **Code Execution**
   - Issue: Syntax errors
   - Solution: Check indentation and syntax

## Related Resources 📚
1. [Python Official Documentation](https://docs.python.org/3/)
2. [PyCharm Documentation](https://www.jetbrains.com/pycharm/documentation/)
3. [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

---
Last updated: [Current Date]
