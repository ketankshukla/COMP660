### What is a function in Python ?

### Answer

A function in Python is a reusable block of code that 
performs a specific task. 
Here are the key points about functions:

1. Definition: Functions are defined using the `def` keyword, 
followed by the function name and parentheses.

2. Purpose: They allow you to organize code into logical units, 
making it more readable and reusable.

3. Basic structure:

```python
def function_name(parameters):
    # Function body
    # Code to perform the task
    return result  # Optional
```

4. Parameters: Functions can accept inputs, called arguments.

5. Return value: Functions can then send back a result using the 
`return` statement.

6. Calling a function: You use the function name followed by 
parentheses to execute it.

Here's a simple example:

```python
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```