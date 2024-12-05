# COMP660

## Overview

This repository contains Python code for various modules and assignments.

## 📁 Module 1

### 📄 Question 4.py

#### Complete Code
```python
x = 0
y = (-1 / 4) * (x - 1) + 3
print(y)

```


## 📁 Module 2

### 📄 Question 1.py

#### Complete Code
```python
# Prompt the user for their first name
name = input("Enter your first name: ")

# Print the welcome message
print(f"Welcome {name} to Comp 660!")

```


### 📄 Question 2.py

#### Complete Code
```python
# The initial values of length and width in the question.

length = 10.0
width = 7

# Expressions and their evaluations stored in variables, as given in the question

expr1 = width // 2
expr2 = length / 2.0
expr3 = length / 2
expr4 = 1 + 4 * 5

# My answer:

# I decided to use the __name__ property of the type function at the end of the type function
# that then shows the proper English name of the type
# For instance, instead of Type: <class 'int'>, it shows Type: int
# I've used the f string to avoid manual concatenation and formatted each line in the group
# to be in a new line by using the newline character "\n"

# The // operator is used for floor division (integer division).
# It divides width by 2 and returns the largest whole number less than or equal to the result.
print(f"Expression: width // 2\nValue: {expr1}\nType: {type(expr1).__name__}\n")
# The / operator performs floating-point division.
# This means that it divides the two numbers and returns the result as a float,
# even if the division results in a whole number, the result is always a float.
print(f"Expression: length / 2.0\nValue: {expr2}\nType: {type(expr2).__name__}\n")
# Once again, the / operator performs floating-point division.
# It divides length by 2 and returns the result as a float.
print(f"Expression: length / 2\nValue: {expr3}\nType: {type(expr3).__name__}\n")
# This expression involves both addition and multiplication and according to PEMDAS rules,
# multiplication is performed before addition.
print(f"Expression: 1 + 4 * 5\nValue: {expr4}\nType: {type(expr4).__name__}\n")

```


### 📄 Question 3.py

#### Complete Code
```python
# First, prompt the user to enter the mass in pounds and convert it to a float.
mass_lb = float(
    input("Please enter the mass in lb that you would like to convert to kg: ")
)

# Next, convert the mass to kilograms where 1 kg = 2.20462 lbs
mass_kg = mass_lb / 2.20462

# Next, calculate the weight on Earth in Newtons by multiplying the mass by the
# gravitation acceleration on Earth.
weight_earth = mass_kg * 9.807

# Next calculate the weight on the Moon in Newtons, this time by using the gravitational
# acceleration on the Moon.
weight_moon = mass_kg * 1.62

# Next, calculate the percentage of the weight on the Moon compared to Earth
percentage_moon_earth = (weight_moon / weight_earth) * 100

# Finally, convert the percentage to an integer.
# If I had used the int() function to for integer conversion, the output would have been 16, because int simply
# truncates decimal without rounding.
# I used the round() function for integer conversion because it rounds the floating point number to the
# nearest whole number, which is 17 in this case.

percentage_moon_earth_int = round(percentage_moon_earth)

# Results displayed in my PyCharm console:
print(f"The converted mass in kg is: {mass_kg}")
print(f"Your weight on Earth is: {weight_earth} Newtons")
print(f"Your weight on the Moon is: {weight_moon} Newtons")
print(
    f"The percentage of the weight on the Moon in comparison to what is experienced on Earth: {percentage_moon_earth} %"
)
print(
    f"The percentage of the weight on the Moon in comparison to what is experienced on Earth as an integer is {percentage_moon_earth_int} %"
)

```


## 📁 Module 3

### 📄 Question 2.py

#### Complete Code
```python
letter = "Hizthere,zThisziszhowzazpasszstatementzworks!"
for i in letter:
    if i == "mn":
        pass
    elif i == "z":
        print(" ", end="")
    else:
        print(i, end="")

```


### 📄 Question 3.py

#### Complete Code
```python
print("What shall I wear today?\n")

name = input("Please Enter Your First Name: ")
temperature = float(input("What is Today's Temperature: "))

if temperature >= 70:
    recommendation = f"Hi {name}, It will be a warm day, T-shirt time!"
else:
    recommendation = f"Hi {name}, You should probably bring a sweater"

print(f"\n{recommendation}")

```


## 📁 Module 4

### 📄 Question 4.py

#### Complete Code
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
```

#### File Description
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

#### Imports
```python
import math
```


### 📄 Question 5.py

#### Complete Code
```python
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
```

#### File Description
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


## 📁 Module 5

### 📄 Question 2.py

#### Complete Code
```python
'''
Question 2

In mathematics, the factorial of a number n is defined as
n! = 1 ⋅ 2 ⋅ ... ⋅ n (as the product of all integer numbers from 1 to n).
For example, 4! = 1 ⋅ 2 ⋅ 3 ⋅ 4 = 24.
Write a recursive function for calculating n!

'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    while True:
        user_input = input("Enter a positive integer (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        if not user_input.isdigit():
            print("Please enter a valid non-negative integer.")
        else:
            n = int(user_input)
            result = factorial(n)
            print(f"The factorial of {n} is: {result}")

        print()


if __name__ == "__main__":
    main()
```

#### File Description
Question 2

In mathematics, the factorial of a number n is defined as
n! = 1 ⋅ 2 ⋅ ... ⋅ n (as the product of all integer numbers from 1 to n).
For example, 4! = 1 ⋅ 2 ⋅ 3 ⋅ 4 = 24.
Write a recursive function for calculating n!


### 📄 Question 3.py

#### Complete Code
```python
'''
Question 3

Write a recursive Python function that returns the sum of the first n integers.
(Hint: The function will be similar to the factorial function!)
ie sum_nint(3) = 1 + 2 + 3 = 6 , sum_nint(4) = 1 + 2 + 3 + 4 = 10.

'''


def sum_nint(n):
    if n == 0:
        return 0
    return n + sum_nint(n - 1)


def main():
    while True:
        user_input = input("Enter a positive integer (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        if not user_input.isdigit() or int(user_input) == 0:
            print("Please enter a valid positive integer.")
        else:
            n = int(user_input)
            result = sum_nint(n)
            print(f"The sum of the first {n} integers is: {result}")

        print()


if __name__ == "__main__":
    main()
```

#### File Description
Question 3

Write a recursive Python function that returns the sum of the first n integers.
(Hint: The function will be similar to the factorial function!)
ie sum_nint(3) = 1 + 2 + 3 = 6 , sum_nint(4) = 1 + 2 + 3 + 4 = 10.


### 📄 Question 4.py

#### Complete Code
```python
'''
Question 4

Explain what happens when the following recursive function is called with
the value “alucard” and 0 as arguments:

I have answered the above question in the markdown file and made this program interactive.

'''

def semordnilap(aString, index):
    if index < len(aString):
        semordnilap(aString, index + 1)
        print(aString[index], end="")

def main():
    while True:
        user_input = input("Enter a word to reverse (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("Thank you for using the word reverser. Goodbye!")
            break

        if not user_input or not user_input.isalpha():
            print("Error: Please enter a non-empty word containing only letters.")
        else:
            print("Reversed word: ", end="")
            semordnilap(user_input, 0)
            print()  # New line after the reversed word

        print()  # Add a blank line for readability

if __name__ == "__main__":
    main()
```

#### File Description
Question 4

Explain what happens when the following recursive function is called with
the value “alucard” and 0 as arguments:

I have answered the above question in the markdown file and made this program interactive.


### 📄 Question 5.py

#### Complete Code
```python
'''
Question 5

Create a lambda function that takes one parameter (a) and returns it.

'''

mirror_lambda = lambda a: a

# Example usage
print(mirror_lambda(5))  # Output: 5
print(mirror_lambda("hello"))  # Output: hello
print(mirror_lambda([1, 2, 3]))  # Output: [1, 2, 3]
```

#### File Description
Question 5

Create a lambda function that takes one parameter (a) and returns it.


### 📄 Question 6.py

#### Complete Code
```python
'''
Question 6

Write a simple function (area_circle) that returns the area of a circle of a given radius.

'''

import math

def area_circle(radius):
    # The area of the circle is PI (3.14) multiplied by the square of the radius.
    return math.pi * radius ** 2

def main():
    while True:
        user_input = input("Enter the radius of the circle (or 'q' to quit): ").strip().lower()

        if user_input == 'q':
            break

        if not user_input or not user_input.replace('.', '', 1).isdigit() or float(user_input) <= 0:
            print("Please enter a valid positive number for the radius.")
        else:
            radius = float(user_input)
            area = area_circle(radius)
            print(f"The area of a circle with radius {radius} is: {area:.2f}")

        print()


if __name__ == "__main__":
    main()
```

#### File Description
Question 6

Write a simple function (area_circle) that returns the area of a circle of a given radius.

#### Imports
```python
import math
```


### 📄 Question 7.py

#### Complete Code
```python
'''
Question 7

Write a lambda function (area_circle_lambda) that returns the area of a circle of a given radius.
'''

import math

# Using the lambda function to return the area of a circle.
area_circle_lambda = lambda radius: math.pi * radius ** 2


def main():
    while True:
        user_input = input("Enter the radius of the circle (or 'q' to quit): ").strip().lower()

        if user_input == 'q':
            break

        if not user_input or not user_input.replace('.', '', 1).isdigit() or float(user_input) <= 0:
            print("Please enter a valid positive number for the radius.")
        else:
            radius = float(user_input)
            area = area_circle_lambda(radius)
            print(f"The area of a circle with radius {radius} is: {area:.2f}")

        print()  # Add a blank line for readability


if __name__ == "__main__":
    main()
```

#### File Description
Question 7

Write a lambda function (area_circle_lambda) that returns the area of a circle of a given radius.

#### Imports
```python
import math
```


### 📄 Question 8.py

#### Complete Code
```python
import math

'''
Answer to question 8a
'''
annual_rate = 0.0185 #1.85%
monthly_rate = annual_rate / 12

# we have been asked to use the monthly rate for all the questions
double_time = math.log(2) /math.log(1 + monthly_rate) / 12

print("\nAnswer to Question 8a")
print(f"Time in years it would take to double the money at 1.85 APR compounded monthly is: {round(double_time,1)} years")

# For the value of 1.85% APR, the answer is 37.5 years or 450 months, which is pretty close to the graph.

'''
Answer to question 8b
Using a lambda function to calculate the doubling time in years, and also using log base 10 instead of natural log.
'''

double_time_years_log_10 = lambda ar: (math.log10(2) /math.log10(1 + (ar / 12))) / 12
print("\nAnswer to Question 8b")
print(f"Doubling time for 1.85% APR in years using log 10 is: {round(double_time_years_log_10(0.0185),1)} years")

'''
Answer to question 8c

'''
double_time_years = lambda ar: (math.log(2) /math.log(1 + (ar / 12))) / 12
print("\nAnswer to Question 8c")
print(f"Doubling time for 3% APR in years is : {round(double_time_years(0.03),1)} years")

```

#### Imports
```python
import math
```


## 📁 Module 6

### 📄 Question 1.py

#### Complete Code
```python
"""
ASCII Code Demonstration Module

This module demonstrates the use of Python's ord() function to get
the ASCII code of a character. In this case, it shows the ASCII
code for the uppercase letter 'A'.

Author: [Your Name]
Date: [Current Date]
"""

ascii_code = ord('A')
print(ascii_code)  # Output: 65

```

#### File Description
ASCII Code Demonstration Module

This module demonstrates the use of Python's ord() function to get
the ASCII code of a character. In this case, it shows the ASCII
code for the uppercase letter 'A'.

Author: [Your Name]
Date: [Current Date]


### 📄 Question 2.py

#### Complete Code
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

#### File Description
IP Address and Mask Extractor Module

This module demonstrates string manipulation in Python by extracting
an IP address and network mask from a formatted string. It uses string
methods like find(), split(), and rstrip() to parse the input string.

Example Input Format:
    'inet addr:127.0.0.1  Mask:255.0.0.0'

Author: [Your Name]
Date: [Current Date]


### 📄 Question 3a.py

#### Complete Code
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

#### File Description
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


### 📄 Question 3b.py

#### Complete Code
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

#### File Description
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


### 📄 Question 4.py

#### Complete Code
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

#### File Description
HTML Tag Generator Module

This module provides functionality to wrap text content with HTML tags.
It demonstrates string formatting and basic HTML generation in Python.

Author: [Your Name]
Date: [Current Date]


### 📄 Question 5.py

#### Complete Code
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

#### File Description
Name Input and Greeting Module

This module provides a simple interactive greeting application that:
1. Prompts for and validates user's first and last name
2. Properly capitalizes the input names
3. Displays a formatted welcome message

The module demonstrates input validation, string manipulation,
and proper text formatting in Python.

Author: [Your Name]
Date: [Current Date]


### 📄 Question 6.py

#### Complete Code
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

    # Otherwise, abbreviate the middle name(s)
    first_name = name_parts[0]
    last_name = name_parts[-1]
    middle_names = " ".join([f"{name[0].upper()}." for name in name_parts[1:-1]])

    return f"{first_name} {middle_names} {last_name}"

# Get user input and convert to lowercase for consistent processing
full_name = input("Enter your full name: ").lower()

# Display the formatted name
print(f"Abbreviated name is: {abbreviate_middle_name(full_name)}")

```

#### File Description
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


### 📄 Question 7.py

#### Complete Code
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
        
    Raises:
        ValueError: If the name is empty, contains only whitespace, contains numbers,
                  or contains no valid characters after cleaning
    """
    # Input validation
    if not name or name.isspace():
        raise ValueError("Name cannot be empty or just whitespace")
    
    if any(char.isdigit() for char in name):
        raise ValueError("Name should not contain numbers")
    
    # Remove extra whitespace and special characters, keeping only letters and spaces
    name = ''.join(char for char in name if char.isalpha() or char.isspace())
    name = ' '.join(name.split())  # Normalize whitespace
    
    if not name:  # Check if name is empty after cleaning
        raise ValueError("Name contains no valid characters")
    
    name_normalized = name.lower()
    famous_list_normalized = famous_list.lower()

    if name_normalized in famous_list_normalized:
        return f"Yup, {name.title()} did make the Top 20 cut!"
    else:
        return f"Sorry, {name.title()} did not make the Top 20 cut!"

# Main program loop
"""
Main execution block that:
1. Continuously prompts for user input
2. Processes the input using check_famous_individual()
3. Handles various exceptions that might occur
4. Provides a way to exit the program
"""
while True:
    try:
        famous_person = input("\nPlease enter the name of the famous individual (or 'quit' to exit): ")
        
        if famous_person.lower() == 'quit':
            print("Thank you for using the Famous People Checker!")
            break
            
        result = check_famous_individual(famous_person)
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

```

#### File Description
Famous People Checker Module

This module provides functionality to check if a given person's name appears in a predefined
list of 20 famous individuals from history. It includes data validation, name normalization,
and case-insensitive matching.

Author: [Your Name]
Date: [Current Date]


## 📁 Module 7

### 📄 Question 1.py

#### Complete Code
```python
import math

def format_tau():
    tau = 2 * math.pi
    half_tau = math.pi

    formatted_string = f"The value of Tau is {tau:^8.3f}, which is two times {half_tau:^8.3f}."

    print(formatted_string)

format_tau()

```

#### Imports
```python
import math
```


### 📄 Question 2.py

#### Complete Code
```python
def calculate_integer_range(num_bytes):

    num_bits = num_bytes * 8

    total_numbers = 2 ** num_bits

    # For signed integers:
    # - Maximum value is 2^(n-1) - 1 (where n is number of bits)
    # - Minimum value is -2^(n-1)
    max_value = (2 ** (num_bits - 1)) - 1
    min_value = -(2 ** (num_bits - 1))

    return total_numbers, min_value, max_value

def format_number(number, use_scientific):

    # use scientific notation for the output if the user enters a number greater than 10 because
    # the number gets too big to read.
    if use_scientific:
        return f"{number:.2e}"
    return f"{number:,}"

def main():

    while True:
        user_input = input("Enter number of Bytes you would like to determine the signed range of (or 'x' to exit): ")

        if user_input.lower() == 'x':
            print("Exiting program...")
            break

        try:
            num_bytes = int(user_input)

            if num_bytes <= 0:
                print("Please enter a positive number of bytes.")
                continue

            # Calculate the range
            total_numbers, min_value, max_value = calculate_integer_range(num_bytes)

            # Determine whether to use scientific notation (if bytes > 10)
            # because otherwise the numbers get too big to read.
            use_scientific = num_bytes > 10

            # Based on the above determination, this tells the format_number function
            # whether to use the scientific notation or not.
            total_formatted = format_number(total_numbers, use_scientific)
            min_formatted = format_number(min_value, use_scientific)
            max_formatted = format_number(max_value, use_scientific)

            output = (f"{num_bytes} Byte(s) integral type with 8 bits can encode {total_formatted} numbers.\n"
                      f"The signed range will be from {min_formatted} to {max_formatted}")

            print(f"{output}\n")

        except ValueError:
            print(f"Please enter a valid integer for the number of bytes.\n")

if __name__ == "__main__":
    main()

```


### 📄 Question 3.py

#### Complete Code
```python
from decimal import Decimal, getcontext, InvalidOperation

def calculate_rms_velocity(temp_celsius):

    # Check if temperature is below absolute zero
    if temp_celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15 Celsius)")

    # Set precision for decimal calculations for answer to come to 6 significant figures
    # for example 435.321 m/s
    getcontext().prec = 6

    try:
        # Convert constants to Decimal objects
        gas_constant_r = Decimal('8.3145')  # Gas constant in (kg·m2/sec2)/K·mol
        molar_mass_m = Decimal('3.2E-2')  # Molar mass of O2 in kg/mol

        # Convert temperature to Kelvin
        kelvin_temp_t = Decimal(str(temp_celsius + 273))

        # Calculate μrms = sqrt(3RT/M)
        rt_product = gas_constant_r * kelvin_temp_t
        three_rt = Decimal('3') * rt_product
        fraction = three_rt / molar_mass_m
        rms_velocity = fraction.sqrt()

        # Create a pattern for formatting (3 decimal places)
        pattern = Decimal('1.000')

        # Return the formatted result
        return rms_velocity.quantize(pattern)

    except InvalidOperation as e:
        raise ValueError("Error in decimal calculation. Please check input values.") from e

def get_temperature_input(prompt):

    # instead of getting input from the user from the main program,
    # I thought creating a function to get the input would be a better way of
    # handling user input because all the input checks and error handling
    # is handled here, and all the main program has to do is test against what's
    # returned.
    value = input(prompt).strip().lower()

    # Check for exit command
    if value == 'x':
        return None

    # Try to convert to float
    try:
        temp = float(value)
        return temp
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value.")

def main():

    while True:
        try:
            temperature_input = get_temperature_input("Enter temperature in Celsius or 'x' to exit program: ")

            # if the user presses 'x'
            if temperature_input is None:
                print("\nExiting program...")
                break

            # Calculate RMS velocity
            velocity = calculate_rms_velocity(temperature_input)

            print("\nThe average velocity or root mean square velocity of a molecule in a sample of oxygen")
            print(f"at {temperature_input} degrees Celsius is {velocity} m/sec\n")

        except ValueError as e:
            print(f"\nError: {str(e)}\n")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}\n")
            print("Please try again.\n")

if __name__ == "__main__":
    main()

```

#### Imports
```python
from decimal import Decimal, getcontext, InvalidOperation
```

