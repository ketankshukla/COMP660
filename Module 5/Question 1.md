### What is the Base Case in Recursion?

### Answer

The base case in recursion defines when the recursive
process should stop.
It's essentially the simplest scenario or condition that
doesn't require further recursive calls to solve the problem.
It prevents infinite recursion by providing a termination
point for the recursive process.
The base case is usually a condition that's checked
at the beginning of the recursive function.
Once the base case is met, the function immediately returns a value
and no more recursive calls are made.

Here is an example:

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)
```