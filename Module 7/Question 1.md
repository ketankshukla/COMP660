#### Question 1

```
Write a program to print and insert the value of tau in an available field width space 
of 8 characters (center aligned) , also print and insert the value of ½ tau to determine 
the value and insert / center align
```

```Python
import math


def format_tau():
    tau = 2 * math.pi
    half_tau = math.pi

    formatted_string = f"The value of Tau is {tau:^8.6f}, which is two times {half_tau:^8.6f}."

    print(formatted_string)


format_tau()
```

The program does the following:

Uses Python's math module for accurate pi value
Calculates tau by multiplying pi by 2
Uses string formatting to center-align the numbers

Format Specifications:

- Total width: 8 characters
- Center alignment
- 6 decimal places for floating-point numbers
- Extra spaces added equally on both sides

Explanation of {tau:^8.6f}:

- ^: Centers the value in the available space
- 8: Total field width of 8 characters
- .6f: Shows 6 decimal places for floating-point number

Same formatting applies to {half_tau:^8.6f}

You can run the above code in Question 1.py file
