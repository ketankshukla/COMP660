"""
Name Abbreviation Module

This module provides functionality to format full names by abbreviating
middle names while keeping the first and last names intact. It handles
various cases including single names, two-part names, and names with
multiple middle components.

Example:
    Input: "john william james smith"
    Output: "John W. J. Smith"

Author: [Your Name]
Date: [Current Date]
"""

def abbreviate_middle_name(full_name):
    """
    Format a full name by abbreviating middle names.

    This function:
    1. Splits the input name into parts
    2. Capitalizes each part
    3. Handles different cases:
       - Single name: returns as is
       - Two names: returns both parts
       - Three or more names: abbreviates middle names

    Args:
        full_name (str): The full name to format (can contain multiple parts)

    Returns:
        str: Formatted name with abbreviated middle names

    Examples:
        >>> abbreviate_middle_name("john smith")
        "John Smith"
        >>> abbreviate_middle_name("john william smith")
        "John W. Smith"
        >>> abbreviate_middle_name("john william james smith")
        "John W. J. Smith"
    """
    name_parts = [part.capitalize() for part in full_name.split()]

    # If there's only one name part, return it as is
    if len(name_parts) == 1:
        return name_parts[0]

    # If there are two parts (first and last), return them as is
    if len(name_parts) == 2:
        return f"{name_parts[0]} {name_parts[1]}"

    # Otherwise, abbreviate the middle name(s)
    first_name = name_parts[0]
    last_name = name_parts[-1]
    middle_names = " ".join([f"{name[0].upper()}." for name in name_parts[1:-1]])

    return f"{first_name} {middle_names} {last_name}"

# Get user input and convert to lowercase for consistent processing
full_name = input("Enter your full name: ").lower()

# Display the formatted name
print(f"Abbreviated name is: {abbreviate_middle_name(full_name)}")
