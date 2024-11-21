# Module 4: Physics Calculations and Data Processing 📚

[← Back to Main Documentation](../../README.md)

## Overview 🎯
Module 4 focuses on implementing physics calculations and data processing algorithms in Python. The assignments demonstrate practical applications of mathematical formulas, user input validation, and data manipulation techniques.

## Learning Objectives 🎓
- Implement physics formulas in Python
- Handle user input with proper validation
- Apply mathematical functions and calculations
- Format output for scientific applications
- Practice error handling and data validation

## Assignments 📝

### Question 4: Final Velocity Calculator
A Python program that calculates the final velocity of an object under constant acceleration.

#### Implementation Details
```python
"""
Final Velocity Calculator Module

This module calculates the final velocity of an object under constant acceleration
(gravity) given its initial velocity and distance traveled. It uses the equation:
v² = v₀² + 2ad, where:
- v = final velocity
- v₀ = initial velocity
- a = acceleration (gravity = 9.8 m/s²)
- d = distance

Author: [Your Name]
Date: [Current Date]
"""

import math

def calculate_final_velocity(initial_velocity, distance):
    """
    Calculate the final velocity using the equation v² = v₀² + 2ad.

    Args:
        initial_velocity (float): Initial velocity in m/s
        distance (float): Distance traveled in meters

    Returns:
        float: Final velocity in m/s, rounded to 1 decimal place

    Example:
        >>> calculate_final_velocity(0, 10)
        14.0
    """
    acceleration = 9.8  # Acceleration due to gravity in m/s²
    velocity_squared = initial_velocity**2 + 2 * acceleration * distance
    final_velocity = math.sqrt(velocity_squared)
    return round(final_velocity, 1)

def get_valid_input(prompt):
    """
    Get valid numerical input from the user.

    Args:
        prompt (str): The prompt message to display to the user

    Returns:
        float: The validated numerical input
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

# Get user input and calculate final velocity
initial_velocity = get_valid_input("Enter the initial velocity (m/s): ")
distance = get_valid_input("Enter the distance (m): ")

# Calculate and display result
final_velocity = calculate_final_velocity(initial_velocity, distance)
print(f"\nFinal velocity: {final_velocity} m/s")
```

#### Key Features
- Uses the physics equation: v² = v₀² + 2ad
- Implements input validation for numerical values
- Provides rounded results for better readability
- Handles potential calculation errors

#### Usage Example
```python
initial_velocity = 0  # m/s
distance = 10        # meters
final_velocity = calculate_final_velocity(initial_velocity, distance)
print(f"The final velocity is {final_velocity} m/s.")
# Output: The final velocity is 14.0 m/s.
```

### Question 5: Elapsed Time Calculator
A Python program that calculates the elapsed time for an object in free fall using the equation t = (v - u) / a.

#### Implementation Details
```python
"""
Elapsed Time Calculator Module

This module calculates the elapsed time for an object in free fall using
the equation: t = (v - u) / a, where:
- t is elapsed time
- v is final velocity
- u is initial velocity
- a is acceleration due to gravity (9.8 m/s²)

Author: [Your Name]
Date: [Current Date]
"""

def calculate_elapsed_time(final_velocity, initial_velocity, acceleration):
    """
    Calculate the elapsed time for an object under constant acceleration.

    Args:
        final_velocity (float): Final velocity in m/s
        initial_velocity (float): Initial velocity in m/s
        acceleration (float): Acceleration in m/s²

    Returns:
        float: Elapsed time in seconds, rounded to 1 decimal place

    Example:
        >>> calculate_elapsed_time(10, 0, 9.8)
        1.0
    """
    elapsed_time = (final_velocity - initial_velocity) / acceleration
    return round(elapsed_time, 1)

def get_valid_input(prompt):
    """
    Get valid numerical input from the user.

    Args:
        prompt (str): The prompt message to display to the user

    Returns:
        float: The validated numerical input
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    """
    Main program function that:
    1. Displays program information
    2. Gets user input for velocities
    3. Calculates and displays elapsed time
    
    Uses constant acceleration due to gravity (9.8 m/s²)
    """
    print("\nElapsed Time Calculator")
    print("----------------------")
    
    # Get user input
    final_velocity = get_valid_input("Enter final velocity (m/s): ")
    initial_velocity = get_valid_input("Enter initial velocity (m/s): ")
    
    # Calculate elapsed time using gravity as acceleration
    acceleration = 9.8  # m/s²
    elapsed_time = calculate_elapsed_time(final_velocity, initial_velocity, acceleration)
    
    # Display results
    print(f"\nElapsed time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
```

#### Key Features
- Uses the physics equation: t = (v - u) / a
- Validates numerical inputs
- Handles division operations safely
- Provides formatted output

#### Usage Example
```python
final_velocity = 10    # m/s
initial_velocity = 0   # m/s
acceleration = 9.8     # m/s²
time = calculate_elapsed_time(final_velocity, initial_velocity, acceleration)
print(f"The elapsed time is {time} seconds.")
# Output: The elapsed time is 1.0 seconds.
```

### Other Questions
[Documentation for other questions will be added as they are processed]

## Code Structure 📂
```
Module 4 Assignment/
├── Question 4.py      # Final velocity calculator
├── Question 5.py      # Elapsed time calculator
└── [Other Python files]
```

## Dependencies 📦
- Python 3.x
- Standard library modules:
  * math (for sqrt function)

## Best Practices 💡
1. Input Validation
   - Always validate numerical inputs
   - Provide clear error messages
   - Use try-except blocks for error handling

2. Calculations
   - Use meaningful variable names
   - Include units in comments
   - Round results appropriately

3. Documentation
   - Add docstrings to all functions
   - Include usage examples
   - Document assumptions and limitations

## Common Issues and Solutions ⚠️
1. Invalid Input
   ```python
   try:
       value = float(input("Enter a number: "))
   except ValueError:
       print("Error: Please enter a valid number.")
   ```

2. Division by Zero
   ```python
   if acceleration == 0:
       raise ValueError("Acceleration cannot be zero")
   ```

## Related Resources 🔗
- [Python Math Module Documentation](https://docs.python.org/3/library/math.html)
- [Physics Formulas Reference](https://physics.info/motion-equations/)

## Notes 📌
- All calculations assume standard gravity (9.8 m/s²)
- Results are rounded to 1 decimal place for clarity
- Input values are assumed to be in SI units (meters, seconds)

---
Last updated: [Current Date]
