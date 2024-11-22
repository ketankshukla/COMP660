### What is a ‘lambda’ function in Python? Please provide an example with code.

### Answer

A lambda function in Python is an anonymous, inline function defined using the `lambda` keyword. Unlike a regular function defined with `def`, a lambda function can have any number of arguments but only one expression.

It's often used when you need a small function for a short period of time and prefer not to formally define it.

### Example

```python
# Lambda function to add two numbers
add = lambda x, y: x + y

# Using the lambda function
result = add(3, 5)
print(result)  # Output: 8
```

In this example:
- The `lambda x, y: x + y` defines an anonymous function that takes two arguments `x` and `y` and returns their sum.
- The `add` variable is assigned this lambda function, so it can be called like a regular function.

Lambda functions are often used with higher order functions like `map()`, `filter()`, and `sorted()`. For instance:

```python
# Using lambda with sorted() to sort a list of tuples based on the second value
points = [(2, 3), (1, 2), (5, 1)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, 1), (1, 2), (2, 3)]
```

Here, `lambda point: point[1]` is used as a key function to sort the list of tuples by their second element.