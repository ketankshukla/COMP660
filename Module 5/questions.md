[Back to README](../README.md)

# Module 5 Questions and Answers

## Question 1: Base Case in Recursion

### Question
What is the Base Case in Recursion?

### Answer
The base case in recursion defines when the recursive process should stop. It's essentially the simplest scenario or condition that doesn't require further recursive calls to solve the problem.

Key points about base cases:
1. Prevents infinite recursion by providing a termination point
2. Usually checked at the beginning of the recursive function
3. Returns a value immediately without making more recursive calls

### Example
```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)
```

### Sample Output
```
>>> factorial(4)
24
>>> factorial(0)
1
>>> factorial(5)
120
```

---

## Question 2: Factorial Calculator

### Question
Write a recursive function for calculating n! (factorial).
In mathematics, the factorial of a number n is defined as n! = 1 ⋅ 2 ⋅ ... ⋅ n.
For example, 4! = 1 ⋅ 2 ⋅ 3 ⋅ 4 = 24.

### Implementation
```python
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

### Sample Output
```
Enter a positive integer (or 'q' to quit): 5
The factorial of 5 is: 120

Enter a positive integer (or 'q' to quit): 0
The factorial of 0 is: 1

Enter a positive integer (or 'q' to quit): abc
Please enter a valid non-negative integer.

Enter a positive integer (or 'q' to quit): q
```

---

## Question 3: Sum of First N Integers

### Question
Write a recursive Python function that returns the sum of the first n integers.
For example: sum_nint(3) = 1 + 2 + 3 = 6, sum_nint(4) = 1 + 2 + 3 + 4 = 10.

### Implementation
```python
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

### Sample Output
```
Enter a positive integer (or 'q' to quit): 4
The sum of the first 4 integers is: 10

Enter a positive integer (or 'q' to quit): 0
Please enter a valid positive integer.

Enter a positive integer (or 'q' to quit): 3
The sum of the first 3 integers is: 6

Enter a positive integer (or 'q' to quit): q
```

---

## Question 4: String Reversal Using Recursion

### Question
Explain what happens when the following recursive function is called with the value "alucard" and 0 as arguments.

### Implementation
```python
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

### Sample Output
```
Enter a word to reverse (or 'q' to quit): alucard
Reversed word: dracula

Enter a word to reverse (or 'q' to quit): hello123
Error: Please enter a non-empty word containing only letters.

Enter a word to reverse (or 'q' to quit): python
Reversed word: nohtyp

Enter a word to reverse (or 'q' to quit): q
Thank you for using the word reverser. Goodbye!
```

### Explanation
When we call `semordnilap("alucard", 0)`, here's what happens:

1. First call: `semordnilap("alucard", 0)`
   - 0 < 7, proceeds to recursive call
   - Calls `semordnilap("alucard", 1)`

2. Second call: `semordnilap("alucard", 1)`
   - 1 < 7, proceeds to recursive call
   - Calls `semordnilap("alucard", 2)`

3. Process continues through:
   - `semordnilap("alucard", 2)`
   - `semordnilap("alucard", 3)`
   - `semordnilap("alucard", 4)`
   - `semordnilap("alucard", 5)`
   - `semordnilap("alucard", 6)`

4. Final call: `semordnilap("alucard", 7)`
   - 7 is not < 7, returns without printing

5. Stack unwinds, printing characters:
   - Prints "d" (index 6)
   - Prints "r" (index 5)
   - Prints "a" (index 4)
   - Prints "c" (index 3)
   - Prints "u" (index 2)
   - Prints "l" (index 1)
   - Prints "a" (index 0)

Final output: "dracula"

Note: The function name "semordnilap" is "palindromes" spelled backwards!

---

## Question 5: Simple Lambda Function

### Question
Create a lambda function that takes one parameter (a) and returns it.

### Implementation
```python
mirror_lambda = lambda a: a

# Example usage
print(mirror_lambda(5))  # Output: 5
print(mirror_lambda("hello"))  # Output: hello
print(mirror_lambda([1, 2, 3]))  # Output: [1, 2, 3]
```

### Sample Output
```
5
hello
[1, 2, 3]
```

---

## Question 6: Circle Area Calculator

### Question
Write a simple function (area_circle) that returns the area of a circle of a given radius.

### Implementation
```python
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

### Sample Output
```
Enter the radius of the circle (or 'q' to quit): 5
The area of a circle with radius 5 is: 78.54

Enter the radius of the circle (or 'q' to quit): 2.5
The area of a circle with radius 2.5 is: 19.63

Enter the radius of the circle (or 'q' to quit): -1
Please enter a valid positive number for the radius.

Enter the radius of the circle (or 'q' to quit): abc
Please enter a valid positive number for the radius.

Enter the radius of the circle (or 'q' to quit): q
```

---

## Question 7: Circle Area Lambda Function

### Question
Write a lambda function (area_circle_lambda) that returns the area of a circle of a given radius.

### Implementation
```python
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

        print()

if __name__ == "__main__":
    main()
```

### Sample Output
```
Enter the radius of the circle (or 'q' to quit): 5
The area of a circle with radius 5 is: 78.54

Enter the radius of the circle (or 'q' to quit): 2.5
The area of a circle with radius 2.5 is: 19.63

Enter the radius of the circle (or 'q' to quit): -1
Please enter a valid positive number for the radius.

Enter the radius of the circle (or 'q' to quit): q
```

---

## Question 8: Doubling Time Calculator

### Question
The Doubling Time formula is used in Finance to calculate the length of time required to double an investment:

Doubling Time = log(2) / log(1 + r)

Where r is the rate of return (monthly rate = annual rate / 12)

### Implementation
```python
import math

# Question 8a: Calculate doubling time for 1.85% APR
annual_rate = 0.0185  # 1.85%
monthly_rate = annual_rate / 12
double_time = math.log(2) / math.log(1 + monthly_rate) / 12

print("\nAnswer to Question 8a")
print(f"Time in years it would take to double the money at 1.85 APR compounded monthly is: {round(double_time,1)} years")

# Question 8b: Lambda function using log base 10
double_time_years_log_10 = lambda ar: (math.log10(2) / math.log10(1 + (ar / 12))) / 12
print("\nAnswer to Question 8b")
print(f"Doubling time for 1.85% APR in years using log 10 is: {round(double_time_years_log_10(0.0185),1)} years")

# Question 8c: Calculate doubling time for 3% APR
double_time_years = lambda ar: (math.log(2) / math.log(1 + (ar / 12))) / 12
print("\nAnswer to Question 8c")
print(f"Doubling time for 3% APR in years is : {round(double_time_years(0.03),1)} years")
```

### Sample Output
```
Answer to Question 8a
Time in years it would take to double the money at 1.85 APR compounded monthly is: 37.5 years

Answer to Question 8b
Doubling time for 1.85% APR in years using log 10 is: 37.5 years

Answer to Question 8c
Doubling time for 3% APR in years is : 23.1 years
```

### Results
1. For BMO's 1.85% APR (compounded monthly): ~37.5 years
2. Using log base 10 gives the same result: ~37.5 years
3. For a 3% APR money market account: ~23.1 years

Note: The results are the same whether using natural log or log base 10, with slight differences only due to rounding.

---

# Discussion

An entity or concept is said to be recursive when simpler or smaller self-similar instances form part of its constituents. Provide an example in nature or art where we can observe this property.

A simple example of where we can observe recursion in nature, is a tree. The branches split into smaller branches, and
those smaller branches split again, just like the bigger ones. It's the same pattern, just repeating in a smaller way.

Another example is a snowflake. When you look closely, each arm of the snowflake has a similar pattern repeating itself,
just getting smaller and smaller. Same goes for seashells like the nautilus. They spiral in on themselves, and if you
zoom in, the spiral shape keeps repeating in a smaller way. It's that same idea of the bigger shape containing smaller
versions of itself.
