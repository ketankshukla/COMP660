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

    Raises:
        ValueError: If the input cannot be converted to a float
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

# Get user input
initial_velocity = get_valid_input("Enter the initial velocity (m/s): ")
distance = get_valid_input("Enter the distance (m): ")

# Calculate and display the final velocity
final_velocity = calculate_final_velocity(initial_velocity, distance)
print(f"The final velocity is {final_velocity} m/s.")