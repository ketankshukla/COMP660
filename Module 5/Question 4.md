### Explain what happens when the following recursive function is called with the value “alucard” and 0 as arguments:

### Answer

```python
def semordnilap(aString, index):
    if index < len(aString):
        semordnilap(aString, index + 1)
        print(aString[index], end="")
```

Here's what happens when we call `semordnilap("alucard", 0)`:

1. First call: `semordnilap("alucard", 0)`
    - 0 < 7 (length of "alucard"), so it proceeds.
    - It calls `semordnilap("alucard", 1)` before printing anything.

2. Second call: `semordnilap("alucard", 1)`
    - 1 < 7, so it proceeds.
    - It calls `semordnilap("alucard", 2)` before printing anything.

3. This process continues for the remaining numbers ...
    - `semordnilap("alucard", 2)`
    - `semordnilap("alucard", 3)`
    - `semordnilap("alucard", 4)`
    - `semordnilap("alucard", 5)`
    - `semordnilap("alucard", 6)`

4. Final recursive call: `semordnilap("alucard", 7)`
    - 7 is not < 7, so this call immediately returns without doing anything.

5. Now, the stack starts unwinding, and the `print` statements execute:
    - Prints "d" (index 6)
    - Prints "r" (index 5)
    - Prints "a" (index 4)
    - Prints "c" (index 3)
    - Prints "u" (index 2)
    - Prints "l" (index 1)
    - Prints "a" (index 0)

The final output will be: "dracula"

This function effectively prints the string in reverse order.

So basically the recursion allows the function to reach the end of the
string before starting to print, then it prints each character from
last to first.

It's clever that the name of the function is reversed too - palindromes :-)
