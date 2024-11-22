"""
Elapsed Time Calculator Module

This module calculates the elapsed time for an object in free fall using
the equation: t = (v - u) / a, where:
- t is elapsed time
- v is final velocity
- u is initial velocity
- a is acceleration due to gravity (9.8 m/s²)

The module provides functions for:
1. Calculating elapsed time given velocities and acceleration
2. Validating user input
3. Running the main calculation program

Author: [Your Name]
Date: [Current Date]
"""

def calculate_elapsed_time(final_velocity, initial_velocity, acceleration):
    """
    Calculate the elapsed time for an object under constant acceleration.

    Uses the equation: t = (v - u) / a, where:
    - t is elapsed time
    - v is final velocity
    - u is initial velocity
    - a is acceleration

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

    Raises:
        ValueError: If the input cannot be converted to a float
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    """
    Main program function that:
    1. Displays program information
    2. Gets user input for velocities
    3. Calculates and displays elapsed time
    
    Uses constant acceleration due to gravity (9.8 m/s²)
    """
    print("Calculate elapsed time for an object in free fall")
    print("Equation: t = (v - u) / a")
    print("where t is elapsed time, v is final velocity, u is initial velocity,")
    print("and a is acceleration due to gravity (9.8 m/s²).")

    initial_velocity = get_valid_input("Enter the initial velocity (m/s): ")
    final_velocity = get_valid_input("Enter the final velocity (m/s): ")

    ACCELERATION = 9.8  # Constant acceleration due to gravity in m/s²

    elapsed_time = calculate_elapsed_time(final_velocity, initial_velocity, ACCELERATION)
    print(f"The elapsed time is {elapsed_time} seconds.")

if __name__ == "__main__":
    main()