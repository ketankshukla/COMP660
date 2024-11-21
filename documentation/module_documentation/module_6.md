# Module 6: String Manipulation and Text Processing 📚

[← Back to Main Documentation](../../README.md)

## Overview 🎯
Module 6 focuses on string manipulation and text processing in Python. Students learn to work with strings, implement text parsing, and handle various string operations.

## Learning Objectives 🎓
- Understand string operations in Python
- Implement text parsing algorithms
- Handle string formatting
- Process and validate text input
- Work with ASCII values
- Create text processing tools

## Assignments 📝

### Question 1: ASCII Code
Demonstrate the use of Python's `ord()` function to get ASCII codes.

**Implementation:**
```python
def get_ascii_code(char):
    """
    Get the ASCII code for a given character.
    
    Args:
        char (str): Single character to convert
        
    Returns:
        int: ASCII code of the character
    """
    return ord(char)

# Example usage
print(get_ascii_code('A'))  # Output: 65
```

### Question 2: IP Address Parser
Create a program to extract IP address and mask from a formatted string.

**Implementation:**
```python
"""
IP Address and Mask Extractor Module

This module demonstrates string manipulation in Python by extracting
an IP address and network mask from a formatted string. It uses string
methods like find(), split(), and rstrip() to parse the input string.

Example Input Format:
    'inet addr:127.0.0.1  Mask:255.0.0.0'

Author: [Your Name]
Date: [Current Date]
"""

# Input string containing IP address and mask information
str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

# Find the position of the first colon (for IP address)
start_position = str.find(':')

# Extract the IP address (everything after first colon until space)
ip_address = str[start_position + 1:].split()[0].rstrip()

# Find the position of the second colon (for mask)
mask_position = str.find(':', start_position + 1)

# Extract the mask (everything after second colon)
mask = str[mask_position + 1:].rstrip()

# Print the extracted information
print(f"The IP Address is - {ip_address}")
print(f"The Mask is - {mask}")
```

### Question 3a: IP Address Counter
Count the number of IP addresses in a multi-line string using line-by-line parsing.

**Implementation:**
```python
"""
IP Address Counter Module

This module counts the number of IP addresses in a multi-line string
containing network interface information. It demonstrates string
manipulation and parsing techniques in Python.

The module:
1. Splits the input string into lines
2. Counts lines containing 'inet addr'
3. Validates the format of each line
4. Provides a total count of valid IP addresses

Example Input Format:
    inet addr :127.0.0.1 Mask:255.0.0.0
    inet addr :127.0.0.2 Mask:255.0.0.0

Author: [Your Name]
Date: [Current Date]
"""

# Multi-line string containing network interface information
str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

# Split the string into lines and initialize counter
lines = str.splitlines()
ip_count = 0

# Process each line
for line in lines:
    if 'inet addr' in line:  # Check if line contains an IP address
        parts = line.split(':')
        if len(parts) > 1:  # Validate line format
            ip_address = parts[1].split()[0]
            ip_count += 1

# Output the total count
print(f"Number of internet addresses: {ip_count}")
```

### Question 3b: IP Address Counter (Alternative)
Count IP addresses using the string count() method.

**Implementation:**
```python
"""
IP Address Counter Using String Count Method

This module demonstrates an alternative approach to counting IP addresses
in a multi-line string using Python's built-in string count() method.
Unlike the previous version that used line-by-line parsing, this approach
directly counts occurrences of the 'inet addr' pattern.

Note: This method assumes that 'inet addr' appears exactly once per IP address
and that all occurrences indicate valid IP addresses.

Example Input Format:
    inet addr :127.0.0.1 Mask:255.0.0.0
    inet addr :127.0.0.2 Mask:255.0.0.0

Author: [Your Name]
Date: [Current Date]
"""

# Multi-line string containing network interface information
str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

# Use the count() method to count the occurrences of 'inet addr'
occurrences = str.count('inet addr')

# Output the total count
print(f"Number of occurrences of 'inet addr': {occurrences}")
```

### Question 4: HTML Tag Generator
Create a function to wrap text with HTML tags.

**Implementation:**
```python
"""
HTML Tag Generator Module

This module provides functionality to wrap text content with HTML tags.
It demonstrates string formatting and basic HTML generation in Python.

Author: [Your Name]
Date: [Current Date]
"""

def add_html_tags(tag, text):
    """
    Wrap the given text with HTML opening and closing tags.

    Args:
        tag (str): The HTML tag to use (e.g., 'h1', 'p', 'div')
        text (str): The text content to wrap with HTML tags

    Returns:
        str: The text wrapped with the specified HTML tags

    Example:
        >>> add_html_tags('h1', 'Hello')
        '<h1>Hello</h1>'
    """
    return f"<{tag}>{text}</{tag}>"

# Example usage with different HTML tags and content
print(add_html_tags('h1', 'My First Page'))
print(add_html_tags('p', 'This is my first page.'))
print(add_html_tags('h2', 'A secondary header.'))
print(add_html_tags('p', 'Some more text.'))
```

### Question 5: Name Input and Greeting
Create an interactive greeting application with name validation.

**Implementation:**
```python
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
```

### Question 6: Name Abbreviation
Format full names by abbreviating middle names.

**Implementation:**
```python
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

    # For names with middle components, abbreviate them
    first = name_parts[0]
    last = name_parts[-1]
    middle = ' '.join(f"{part[0]}." for part in name_parts[1:-1])
    
    return f"{first} {middle} {last}"

# Get user input and convert to lowercase for consistent processing
full_name = input("Enter your full name: ").lower()

# Display the formatted name
print(f"Formatted name: {abbreviate_middle_name(full_name)}")
```

### Question 7: Famous People Checker
Create a program to check if a person's name appears in a list of famous individuals.

**Implementation:**
```python
"""
Famous People Checker Module

This module provides functionality to check if a given person's name appears in a predefined
list of 20 famous individuals from history. It includes data validation, name normalization,
and case-insensitive matching.

Author: [Your Name]
Date: [Current Date]
"""

famous_list = '''\
Marilyn Monroe (1926 – 1962) American actress, singer, model
Abraham Lincoln (1809 – 1865) US President during American civil war
Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner
John F. Kennedy (1917 – 1963) US President 1961 – 1963
Martin Luther King (1929 – 1968)  American civil rights campaigner
Queen Elizabeth II (1926 – ) British monarch since 1954
Winston Churchill (1874 – 1965) British Prime Minister during WWII
Donald Trump (1946 – ) Businessman, US President.
Bill Gates (1955 – ) American businessman, founder of Microsoft
Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement
Margaret Thatcher (1925 – 2013) British Prime Minister 1979 – 1990
Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 – 1506) Italian explorer
Charles Darwin (1809 – 1882) British scientist, theory of evolution
Elvis Presley (1935 – 1977) American musician
Albert Einstein (1879 – 1955) German scientist, theory of relativity
Paul McCartney (1942 – ) British musician, member of Beatles
Queen Victoria ( 1819 – 1901) British monarch 1837 – 1901
Pope Francis (1936 – ) First pope from the Americas
'''

def check_famous_individual(name):
    """
    Check if a given name appears in the list of famous individuals.
    
    This function performs the following operations:
    1. Validates the input name for emptiness and numeric characters
    2. Normalizes the name by removing special characters and extra whitespace
    3. Performs a case-insensitive search in the famous_list
    
    Args:
        name (str): The name of the person to check
        
    Returns:
        str: A message indicating whether the person is in the Top 20 list
    """
    # Input validation
    if not name or name.isspace():
        raise ValueError("Name cannot be empty")
    if any(char.isdigit() for char in name):
        raise ValueError("Name cannot contain numbers")

    # Convert to lowercase for case-insensitive comparison
    name = name.lower().strip()

    # Check if name is in the list
    if name in famous_list.lower():
        return f"{name.title()} is in the Top 20 list!"
    else:
        return f"{name.title()} is not in the Top 20 list."

## Implementation Details 🔧
### String Operations
- String methods (find, split, strip)
- Case conversion
- String formatting
- Text parsing

## Best Practices 💡
1. Validate input strings
2. Use appropriate string methods
3. Handle edge cases
4. Document string operations

## Common Issues and Solutions ⚠️
1. **String Formatting**
   - Issue: Inconsistent output format
   - Solution: Use f-strings

2. **Input Validation**
   - Issue: Invalid input handling
   - Solution: Add input validation

3. **Case Sensitivity**
   - Issue: Case-sensitive comparisons
   - Solution: Convert to lowercase

## Related Resources 📚
1. [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
2. [Python String Formatting](https://docs.python.org/3/library/string.html#formatstrings)
3. [Regular Expressions in Python](https://docs.python.org/3/library/re.html)

## Assessment Criteria 📋
1. **Functionality (40%)**
   - Correct implementation of required features
   - Proper handling of edge cases
   - Accurate string manipulation

2. **Code Quality (30%)**
   - Clean and efficient code
   - Proper error handling
   - Effective use of string methods

3. **Testing (20%)**
   - Comprehensive test cases
   - Edge case testing
   - Input validation testing

4. **Style and Documentation (10%)**
   - Consistent coding style
   - Clear comments and documentation
   - Adherence to Python conventions

## Advanced Topics 🔮
