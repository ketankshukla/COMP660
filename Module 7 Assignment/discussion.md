Question 1 - Explain the //, %, and ** operators in Python. Please provide an example.

The //, %, and ** operators serve different purposes:

1. // (Floor Division Operator):

    - This operator divides two numbers and rounds down the result to the nearest integer.
    - It returns the integer quotient after division, discarding any remainder.

   Example: result = 10 // 3

   The result is 3, because 10 divided by 3 is 3.333, and the floor division rounds it down to 3


2. % (Modulo Operator):

    - This operator returns the remainder after dividing the first number by the second.
    - It’s useful for determining if a number is divisible by another or for cyclical patterns.

   Example: remainder = 10 % 3

   The remainder is 1, because 10 divided by 3 leaves a remainder of 1


3. ** (Exponentiation Operator):

    - This operator raises the first number to the power of the second number.

   Example: result = 2 ** 3

   The result is 8, because 2 raised to the power of 3 is 8

Question 2 - How would you work with numbers other than those in the decimal number system? Please provide at least
three examples.

Other number systems used in Python are binary, octal, and hexadecimal.

1. Binary (Base 2)

   Binary numbers use only 0s and 1s and are represented with a 0b or 0B prefix in Python.

   Example:

   binary_num = 0b1010 # Binary for decimal 10
   print(binary_num)  # Output: 10

To convert a decimal number to binary use the bin() function:

decimal_number = 10
binary_representation = bin(decimal_number)  # Output: 0b1010

2. Octal (Base 8)

   Octal numbers use digits from 0 to 7 and are represented with a 0o or 0O prefix.

   Example:

   octal_num = 0o12 # Octal for decimal 10
   print(octal_num)  # Output: 10

To convert a decimal number to octal use the oct() function:

decimal_number = 10
octal_representation = oct(decimal_number)  # Output: 0o12

3. Hexadecimal (Base 16)

   Hexadecimal numbers use digits 0-9 and letters A-F, and are represented with a 0x or 0X prefix.

   Example:

   hex_num = 0xA # Hexadecimal for decimal 10
   print(hex_num)  # Output: 10

You can convert a decimal number to hexadecimal using the hex() function:

decimal_number = 10
hex_representation = hex(decimal_number)  # Output: 0xa
