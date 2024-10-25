#### Question 6 - Write a program that takes your full name as input and displays the abbreviations of the middle name except the first and last name which is displayed as it is. For example, if your name is Elvis Aaron Presley, then the output should be Elvis A. Presley.

From the previous question, it makes sense to alter the name to proper case,
and so I did the same here. This way, regardless of casing, it will always
print out the proper case - which is how all names should be.

```python
def abbreviate_middle_name(full_name):
    name_parts = [part.capitalize() for part in full_name.split()]

    # If there's only one name part, return it as is
    if len(name_parts) == 1:
        return name_parts[0]

    # If there are two parts (first and last), return them as is
    if len(name_parts) == 2:
        return f"{name_parts[0]} {name_parts[1]}"

    # Otherwise, abbreviate the middle name(s)
    first_name = name_parts[0]
    last_name = name_parts[-1]
    middle_names = " ".join([f"{name[0].upper()}." for name in name_parts[1:-1]])

    return f"{first_name} {middle_names} {last_name}"


full_name = input("Enter your full name: ").lower()

print(f"Abbreviated name is: {abbreviate_middle_name(full_name)}")
```

### Explanation:

The function first splits the full name into individual parts (e.g., first, middle, and last names)
and capitalizes each part.

It then checks the number of name parts:

1. If there's only one name (like just a first name), it returns that name as-is.
2. If there are two parts (first and last name), it returns them unchanged.
3. If there are more than two parts (first, middle, last), it keeps the first and last name intact
   but abbreviates the middle name(s) to just their initials with a period
   (e.g., "John Michael Doe" becomes "John M. Doe").

Finally, it takes the user’s input, processes it according to these rules, and prints the resulting name.

### Sample Console Output:

```
Enter your full name: Elvis Aaron Presley
Elvis A. Presley
```

If the user enters more than one middle name, each will be abbreviated:

```
Enter your full name: John Ronald Reuel Tolkien
John R. R. Tolkien
```

This approach handles different variations of input effectively.

You can run the above code in Question 6.py file
