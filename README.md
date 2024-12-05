# COMP660

## Overview

This repository contains Python code for various modules and assignments.

## Development

This section provides a detailed explanation of the codebase.

#### 📄 .pylintrc

### 📁 .git

#### 📄 HEAD

#### 📄 config

#### 📄 description

#### 📄 packed-refs

### 📁 .git\hooks

#### 📄 applypatch-msg.sample

#### 📄 commit-msg.sample

#### 📄 fsmonitor-watchman.sample

#### 📄 post-update.sample

#### 📄 pre-applypatch.sample

#### 📄 pre-commit.sample

#### 📄 pre-merge-commit.sample

#### 📄 pre-push.sample

#### 📄 pre-rebase.sample

#### 📄 pre-receive.sample

#### 📄 prepare-commit-msg.sample

#### 📄 push-to-checkout.sample

#### 📄 sendemail-validate.sample

#### 📄 update.sample

### 📁 .git\info

#### 📄 exclude

### 📁 .git\logs

#### 📄 HEAD

### 📁 .git\logs\refs\heads

#### 📄 master

### 📁 .git\logs\refs\remotes\origin

#### 📄 HEAD

### 📁 .git\refs\heads

#### 📄 master

### 📁 .git\refs\remotes\origin

#### 📄 HEAD

### 📁 Module 1

#### 📄 Question 4.py

#### 📄 questions.md

### 📁 Module 2

#### 📄 Question 1.py

#### 📄 Question 2.py

#### 📄 Question 3.py

#### 📄 questions.md

### 📁 Module 3

#### 📄 Question 2.py

#### 📄 Question 3.py

#### 📄 questions.md

### 📁 Module 4

#### 📄 Question 4.py

<span style="color: #ffff00;">Description:</span>
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

<span style="color: #00ffff;">Imports:</span>
```python
import math
```

#### 📄 Question 5.py

<span style="color: #ffff00;">Description:</span>
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

#### 📄 questions.md

### 📁 Module 5

#### 📄 Question 2.py

<span style="color: #ffff00;">Description:</span>
Question 2

In mathematics, the factorial of a number n is defined as
n! = 1 ⋅ 2 ⋅ ... ⋅ n (as the product of all integer numbers from 1 to n).
For example, 4! = 1 ⋅ 2 ⋅ 3 ⋅ 4 = 24.
Write a recursive function for calculating n!

#### 📄 Question 3.py

<span style="color: #ffff00;">Description:</span>
Question 3

Write a recursive Python function that returns the sum of the first n integers.
(Hint: The function will be similar to the factorial function!)
ie sum_nint(3) = 1 + 2 + 3 = 6 , sum_nint(4) = 1 + 2 + 3 + 4 = 10.

#### 📄 Question 4.py

<span style="color: #ffff00;">Description:</span>
Question 4

Explain what happens when the following recursive function is called with
the value “alucard” and 0 as arguments:

I have answered the above question in the markdown file and made this program interactive.

#### 📄 Question 5.py

<span style="color: #ffff00;">Description:</span>
Question 5

Create a lambda function that takes one parameter (a) and returns it.

#### 📄 Question 6.py

<span style="color: #ffff00;">Description:</span>
Question 6

Write a simple function (area_circle) that returns the area of a circle of a given radius.

<span style="color: #00ffff;">Imports:</span>
```python
import math
```

#### 📄 Question 7.py

<span style="color: #ffff00;">Description:</span>
Question 7

Write a lambda function (area_circle_lambda) that returns the area of a circle of a given radius.

<span style="color: #00ffff;">Imports:</span>
```python
import math
```

#### 📄 Question 8.py

<span style="color: #00ffff;">Imports:</span>
```python
import math
```

#### 📄 questions.md

### 📁 Module 6

#### 📄 Question 1.py

<span style="color: #ffff00;">Description:</span>
ASCII Code Demonstration Module

This module demonstrates the use of Python's ord() function to get
the ASCII code of a character. In this case, it shows the ASCII
code for the uppercase letter 'A'.

Author: [Your Name]
Date: [Current Date]

#### 📄 Question 2.py

<span style="color: #ffff00;">Description:</span>
IP Address and Mask Extractor Module

This module demonstrates string manipulation in Python by extracting
an IP address and network mask from a formatted string. It uses string
methods like find(), split(), and rstrip() to parse the input string.

Example Input Format:
    'inet addr:127.0.0.1  Mask:255.0.0.0'

Author: [Your Name]
Date: [Current Date]

#### 📄 Question 3a.py

<span style="color: #ffff00;">Description:</span>
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

#### 📄 Question 3b.py

<span style="color: #ffff00;">Description:</span>
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

#### 📄 Question 4.py

<span style="color: #ffff00;">Description:</span>
HTML Tag Generator Module

This module provides functionality to wrap text content with HTML tags.
It demonstrates string formatting and basic HTML generation in Python.

Author: [Your Name]
Date: [Current Date]

#### 📄 Question 5.py

<span style="color: #ffff00;">Description:</span>
Name Input and Greeting Module

This module provides a simple interactive greeting application that:
1. Prompts for and validates user's first and last name
2. Properly capitalizes the input names
3. Displays a formatted welcome message

The module demonstrates input validation, string manipulation,
and proper text formatting in Python.

Author: [Your Name]
Date: [Current Date]

#### 📄 Question 6.py

<span style="color: #ffff00;">Description:</span>
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

#### 📄 Question 7.py

<span style="color: #ffff00;">Description:</span>
Famous People Checker Module

This module provides functionality to check if a given person's name appears in a predefined
list of 20 famous individuals from history. It includes data validation, name normalization,
and case-insensitive matching.

Author: [Your Name]
Date: [Current Date]

#### 📄 questions.md

### 📁 Module 7

#### 📄 Question 1.py

<span style="color: #00ffff;">Imports:</span>
```python
import math
```

#### 📄 Question 2.py

#### 📄 Question 3.py

<span style="color: #00ffff;">Imports:</span>
```python
from decimal import Decimal, getcontext, InvalidOperation
```

#### 📄 questions.md

## Setup

1. Clone the repository
2. Install the required dependencies
3. Run the Python scripts as needed

## License

MIT