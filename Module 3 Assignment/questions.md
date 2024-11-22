# Module 3 Questions and Answers

## Question 1: Understanding Pass vs Continue

### Question
What is the difference between "pass" and "continue" in Python?

### Answer
The "pass" and "continue" statements in Python serve different purposes in control flow:

1. pass:
    - "pass" is really a null operation - it doesn't do anything.
    - It's used as a placeholder where syntactically some code is required, but no action is desired.
    - It allows you to have empty code blocks without causing syntax errors.
    - It's often used in places where code will eventually be added, or to create minimal classes or functions.

2. continue:
    - "continue" is used inside loops (for or while).
    - It skips the rest of the current iteration and moves to the next iteration of the loop.
    - When "continue" is encountered, the program jumps to the next iteration without executing any remaining code in the current iteration.

### Example Code
```python
# Using pass
for i in range(5):
    if i == 2:
        pass  # Does nothing, continues with the next line
    print(i)

# Using continue
for i in range(5):
    if i == 2:
        continue  # Skips the rest of the loop for this iteration
    print(i)
```

### Sample Output
For pass statement:
```
0
1
2
3
4
```

For continue statement:
```
0
1
3
4
```

### Key Differences
- Use "pass" when you need a placeholder for future code or to create empty structures.
- Use "continue" when you want to skip the rest of the current loop iteration and move to the next one.

---

## Question 2: String Manipulation with Pass Statement

### Question
What is the output of the following code and explain what happened?

### Implementation (Question2.py)
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

### Sample Output
```
Hi there, This is how a pass statement works!
```

### Screenshot
![Question 2 Output](./Question%202%20Screenshot.png)

### Explanation
1. The string `letter` is defined with 'z' characters used as separators.

2. The code loops through each character in the `letter` string.

3. For each character, it checks three conditions:
   a. If the character is "mn":
      - This condition is never met because "mn" are two characters, and we're checking one character at a time. 
      - The `pass` statement here does nothing and is never executed.

   b. If the character is "z":
      - When a 'z' is encountered, it prints a space instead of the 'z'. 
      - This effectively replaces all 'z' characters with spaces.

   c. For any other character:
      - It prints the character as is, without adding a new line (due to `end=""`)

4. The `end=""` parameter in the `print()` function ensures that all characters are printed on the same line.

The code replaces all 'z' characters with spaces and prints all other characters as they are, resulting in a readable sentence.

---

## Question 3: Temperature-Based Clothing Recommendation

### Implementation (Question3.py)
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

### Sample Outputs

For temperature less than 70°F:
```
What shall I wear today?

Please Enter Your First Name: John
What is Today's Temperature: 65

Hi John, You should probably bring a sweater
```

For temperature equal to 70°F:
```
What shall I wear today?

Please Enter Your First Name: Alice
What is Today's Temperature: 70

Hi Alice, It will be a warm day, T-shirt time!
```

For temperature greater than 70°F:
```
What shall I wear today?

Please Enter Your First Name: Bob
What is Today's Temperature: 75

Hi Bob, It will be a warm day, T-shirt time!
```

### Screenshots
- Less than 70 degrees:
![Temperature Less Than 70](./Question%203%20-%20Less%20Than%2070%20Degrees.png)

- Equal to 70 degrees:
![Temperature Equal To 70](./Question%203%20-%20Equal%20To%2070%20Degrees.png)

- Greater than 70 degrees:
![Temperature Greater Than 70](./Question%203%20-%20Greater%20Than%2070%20Degrees.png)

### Explanation
The program:
1. Prompts the user for their name and the current temperature
2. Uses conditional logic to determine appropriate clothing recommendation:
   - If temperature is 70°F or higher: suggests wearing a T-shirt
   - If temperature is below 70°F: suggests bringing a sweater
3. Demonstrates:
   - User input handling
   - Type conversion (string to float)
   - Conditional statements (if/else)
   - String formatting with f-strings
   - Comparison operators
