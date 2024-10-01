### What will the following Python program print out? Explain the output

```python
def name():
    print("- Albert Einstein")
def quote():
    print("Imagination is more important than ", end="")
def ofthe():
    print("For knowledge is limited, ", end="")
def day():
    print("knowledge. " , end="")
def famous():
    print("stimulating progress, giving birth to evolution ", end="")
def influencers():
    print("whereas imagination embraces the entire world, ", end="")

quote()
day()
ofthe()
influencers()
famous()
name()
```

### Answer

The given Python program will print:

```
Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution 
- Albert Einstein
```

## Explanation

1. The program defines six functions: 
`name()`, `quote()`, `ofthe()`, `day()`, `famous()`, and `influencers()`.

2. Each function prints a specific part of a quote:
    - `quote()`: "Imagination is more important than "
    - `day()`: "knowledge. "
    - `ofthe()`: "For knowledge is limited, "
    - `influencers()`: "whereas imagination embraces the entire world, "
    - `famous()`: "stimulating progress, giving birth to evolution "
    - `name()`: "- Albert Einstein"

3. Most of these functions use `end=""` in their `print()` statements. 
This prevents the default newline character from being added 
at the end of each print, allowing the next print to continue on the same line.

4. The functions are called in this order: `quote()`, `day()`, `ofthe()`, `influencers()`, `famous()`, `name()`.

5. As each function is called, it prints its part of the quote. 
Because of the `end=""` parameter, all parts (except the last) 
are printed on the same line.

6. The `name()` function is called last and doesn't use `end=""`, 
so it prints on a new line by default.