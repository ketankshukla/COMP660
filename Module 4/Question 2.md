### What is the difference between an argument and a parameter?

### Answer

While the terms "argument" and "parameter" are often used 
interchangeably, they have distinct meanings in programming:

### Parameters

- **Definition**: Parameters are the variables listed in the 
function definition.
- **Where they appear**: In the function declaration or definition.
- **Purpose**: They define what kind of input a function can accept.

### Arguments

- **Definition**: Arguments are the actual values passed to the 
function when it is called.
- **Where they appear**: In the function call.
- **Purpose**: They provide the actual data to be used by the function.

### Example

```python
def greet(name, greeting="Hello"):  # 'name' and 'greeting' are parameters
    return f"{greeting}, {name}!"

# Function calls with arguments
print(greet("Alice"))  # "Alice" is an argument
print(greet("Bob", "Hi"))  # "Bob" and "Hi" are arguments

# Using variables as arguments
user = "Charlie"
custom_greeting = "Good morning"
print(greet(user, custom_greeting))
```

In this example:
- `name` and `greeting` are parameters in the function definition.
- `"Alice"`, `"Bob"`, `"Hi"`, `user`, and `custom_greeting` are arguments used when calling the function.

### Key Distinction

- Parameters are part of the function's definition.
- Arguments are the actual values supplied to these parameters 
when the function is called.

We define functions with parameters and call functions with arguments.