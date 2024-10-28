#### Question 2

```
The data type integer signed range is from -2,147,483,648 to 2,147,483,648 (4 bytes). 
Write a program that determines the range of numbers for an integer based on the number 
of bytes it can encode (Hint integral type with n bits can encode 2n numbers).
```

My solution of what's happening in the program:

- Takes a number of bytes as a user input and shows possible integer ranges
- Switches to scientific notation for inputs > 10 bytes, because otherwise the numbers get too big to read

• Core Calculations:

1. Takes number of bytes from user
2. Converts to bits (multiply by 8)
3. Calculates:
    * Total numbers possible = 2^(bits)
    * Maximum value = 2^(bits-1) - 1
    * Minimum value = -2^(bits-1)

• Number Formatting:

- For inputs ≤ 10 bytes: Uses comma format (e.g., 1,234,567)
- For inputs > 10 bytes: Uses scientific notation (e.g., 1.23e+6)

• Program Flow:

1. Ask for byte count
2. Do calculations
3. Format based on input size
4. Display results
5. Repeat until 'x' entered

• Example:

- Input: 4 bytes
- 4 bytes = 32 bits
- Total: 4,294,967,296 numbers
- Range: -2,147,483,648 to 2,147,483,647
