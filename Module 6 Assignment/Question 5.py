"""
Name Input and Greeting Module

This module provides a simple interactive greeting application that:
1. Prompts for and validates user's first and last name
2. Properly capitalizes the input names
3. Displays a formatted welcome message

The module demonstrates input validation, string manipulation,
and proper text formatting in Python.

Author: [Your Name]
Date: [Current Date]
"""

def get_name_input(prompt):
    """
    Get and validate a name input from the user.

    This function:
    1. Prompts the user for input using the provided prompt
    2. Removes leading/trailing whitespace
    3. Validates that the input is not empty
    4. Capitalizes the first letter of the name

    Args:
        prompt (str): The prompt message to display to the user

    Returns:
        str: The validated and properly capitalized name

    Note:
        The function will keep prompting until valid input is received
    """
    while True:
        name = input(prompt).strip()
        if name:
            return name.capitalize()
        else:
            print("Input cannot be blank. Please try again.")

first_name = get_name_input("What is your first name? ")
last_name = get_name_input("What is your last name? ")

print(f"\nHi {first_name.title()} {last_name.title()}, welcome to my Python greet application!")
