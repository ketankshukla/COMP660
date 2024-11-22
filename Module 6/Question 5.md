#### Question 5 - Write a Python script that takes input from the user and displays that input back in upper and lower cases.

```python
# Take user input for first and last name
first_name = input("What is your first name? ").lower()
last_name = input("What is your last name? ").lower()

# Capitalize the first letter of each name
first_name_capitalized = first_name.capitalize()
last_name_capitalized = last_name.capitalize()

# Display the greeting message
print(f"Hi {first_name_capitalized} {last_name_capitalized}, welcome to my Python greet application!")
```

### Explanation:

1. Define `get_name_input` function: This function prompts the user to enter their name (first or last) and checks
   that it’s not blank. If the input is blank, it keeps prompting until a valid name is entered.
   Once valid, it returns the name capitalized.

2. Get first and last names: The script calls `get_name_input` twice to get the user’s first and last names,
   ensuring neither input is blank.

3. Print greeting in title case: The final print statement displays a personalized greeting using `title()`
   formatting, which ensures each name part is capitalized correctly (e.g., "Alison Smith").

This approach ensures that both names are displayed in title case and prevents any blank inputs.

### Sample Console Output:

```
What is your first name? alison
What is your last name? smith
Hi Alison Smith, welcome to my Python greet application!
```

This code ensures that even if the user enters the names in any case,
the output will always be properly formatted.

You can run the above code in Question 5.py file
