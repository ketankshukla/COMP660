# Module 6 Questions and Answers

## Question 1: ASCII Code Function

### Question
What function is used to get the ASCII code of a character?

### Answer
The function used to get the ASCII code of a character in Python is `ord()`.

### Example
```python
ascii_code = ord('A')
print(ascii_code)  # Output: 65
```

The `ord()` function takes a single character as input and returns its corresponding ASCII (or Unicode) code.

---

## Question 2: String Parsing

### Question
Take the following Python code that stores a string: str = 'inet addr:127.0.0.1  Mask:255.0.0.0'. Use find and string slicing to extract the portion of the string after the colon inet address character and then use the rstrip function to remove any trailing characters.

### Implementation
```python
# Input string containing IP address and mask information
str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

# Find the position of the first colon (for IP address)
start_position = str.find(':')

# Extract the IP address (everything after first colon until space)
ip_address = str[start_position + 1:].split()[0].rstrip()

# Find the position of the second colon (for mask)
mask_position = str.find(':', start_position + 1)

# Extract the mask (everything after second colon)
mask = str[mask_position + 1:].rstrip()

# Print the extracted information
print(f"The IP Address is - {ip_address}")
print(f"The Mask is - {mask}")
```

### Explanation
1. String Creation:
   - Creates a string variable containing IP address and mask information
   - Format is 'inet addr:[IP]  Mask:[MASK]'

2. Finding First Colon:
   - `start_position = str.find(':')` locates the first colon
   - This finds the colon after 'inet addr'

3. Extracting IP Address:
   - `str[start_position + 1:]` gets everything after the first colon
   - `.split()` breaks this into a list using whitespace as separator
   - `[0]` selects the first element (127.0.0.1)
   - `.rstrip()` removes any trailing whitespace

4. Finding Second Colon:
   - `str.find(':', start_position + 1)` finds the second colon
   - Starts searching after the first colon position

5. Extracting Mask:
   - `str[mask_position + 1:]` gets everything after the second colon
   - `.rstrip()` removes any trailing whitespace

---

## Question 3: String Analysis

### Part A: Counting IP Addresses Using Loop

#### Question
Using a for loop through a string, count the number of internet addresses in the string below by using the split method.

#### Implementation
```python
str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

# Split the string into lines and initialize counter
lines = str.splitlines()
ip_count = 0

# Process each line
for line in lines:
    if 'inet addr' in line:  # Check if line contains an IP address
        parts = line.split(':')
        if len(parts) > 1:  # Validate line format
            ip_address = parts[1].split()[0]
            ip_count += 1

# Output the total count
print(f"Number of internet addresses: {ip_count}")
```

### Part B: Counting Using String Method

#### Question
Use the count() method to return the number of occurrences of the substring in the given string.

#### Implementation
```python
str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

# Use the count() method to count the occurrences of 'inet addr'
occurrences = str.count('inet addr')

print(f"Number of occurrences of 'inet addr': {occurrences}")
```

---

## Question 4: HTML Tag Generator

### Question
Write a Python function to create the HTML string with tags around the word(s).

### Implementation
```python
def add_html_tags(tag, text):
    """
    Wrap the given text with HTML opening and closing tags.

    Args:
        tag (str): The HTML tag to use (e.g., 'h1', 'p', 'div')
        text (str): The text content to wrap with HTML tags

    Returns:
        str: The text wrapped with the specified HTML tags

    Example:
        >>> add_html_tags('h1', 'Hello')
        '<h1>Hello</h1>'
    """
    return f"<{tag}>{text}</{tag}>"

# Example usage with different HTML tags and content
print(add_html_tags('h1', 'My First Page'))
print(add_html_tags('p', 'This is my first page.'))
print(add_html_tags('h2', 'A secondary header.'))
print(add_html_tags('p', 'Some more text.'))
```

### Output
```html
<h1>My First Page</h1>
<p>This is my first page.</p>
<h2>A secondary header.</h2>
<p>Some more text.</p>
```

---

## Question 5: Name Case Converter

### Question
Write a Python script that takes input from the user and displays that input back in upper and lower cases.

### Implementation
```python
def get_name_input(prompt):
    """
    Get and validate a name input from the user.

    Args:
        prompt (str): The prompt message to display to the user

    Returns:
        str: The validated and properly capitalized name
    """
    while True:
        name = input(prompt).strip()
        if name:
            return name.capitalize()
        else:
            print("Input cannot be blank. Please try again.")

first_name = get_name_input("What is your first name? ")
last_name = get_name_input("What is your last name? ")

print(f"\nHi {first_name.title()} {last_name.title()}, welcome to my Python greet application!")
```

### Sample Output
```
What is your first name? alison
What is your last name? smith
Hi Alison Smith, welcome to my Python greet application!
```

---

## Question 6: Name Abbreviator

### Question
Write a program that takes your full name as input and displays the abbreviations of the middle name except the first and last name which is displayed as it is. For example, if your name is Elvis Aaron Presley, then the output should be Elvis A. Presley.

### Implementation
```python
def abbreviate_middle_name(full_name):
    """
    Format a full name by abbreviating middle names.

    Args:
        full_name (str): The full name to format (can contain multiple parts)

    Returns:
        str: Formatted name with abbreviated middle names

    Examples:
        >>> abbreviate_middle_name("john smith")
        "John Smith"
        >>> abbreviate_middle_name("john william smith")
        "John W. Smith"
    """
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

# Get user input and process
full_name = input("Enter your full name: ").lower()
print(f"Abbreviated name is: {abbreviate_middle_name(full_name)}")
```

### Sample Output
```
Enter your full name: Elvis Aaron Presley
Abbreviated name is: Elvis A. Presley

Enter your full name: John Ronald Reuel Tolkien
Abbreviated name is: John R. R. Tolkien
```

---

## Question 7: Famous People Checker

### Question
Create a program that checks if a given name appears in a predefined list of famous individuals.

### Implementation
```python
famous_list = '''\
Marilyn Monroe (1926 – 1962) American actress, singer, model
Abraham Lincoln (1809 – 1865) US President during American civil war
Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner
John F. Kennedy (1917 – 1963) US President 1961 – 1963
Martin Luther King (1929 – 1968)  American civil rights campaigner
Queen Elizabeth II (1926 – ) British monarch since 1954
Winston Churchill (1874 – 1965) British Prime Minister during WWII
Donald Trump (1946 – ) Businessman, US President.
Bill Gates (1955 – ) American businessman, founder of Microsoft
Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement
Margaret Thatcher (1925 – 2013) British Prime Minister 1979 – 1990
Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 – 1506) Italian explorer
Charles Darwin (1809 – 1882) British scientist, theory of evolution
Elvis Presley (1935 – 1977) American musician
Albert Einstein (1879 – 1955) German scientist, theory of relativity
Paul McCartney (1942 – ) British musician, member of Beatles
Queen Victoria ( 1819 – 1901) British monarch 1837 – 1901
Pope Francis (1936 – ) First pope from the Americas
'''

def check_famous_individual(name):
    """
    Check if a given name appears in the list of famous individuals.
    
    Args:
        name (str): The name of the person to check
        
    Returns:
        str: A message indicating whether the person is in the Top 20 list
        
    Raises:
        ValueError: If the name is empty or contains invalid characters
    """
    # Input validation
    if not name or name.isspace():
        raise ValueError("Name cannot be empty or just whitespace")
    
    if any(char.isdigit() for char in name):
        raise ValueError("Name should not contain numbers")
    
    # Clean and normalize the name
    name = ''.join(char for char in name if char.isalpha() or char.isspace())
    name = ' '.join(name.split())
    
    if not name:
        raise ValueError("Name contains no valid characters")
    
    name_normalized = name.lower()
    famous_list_normalized = famous_list.lower()

    if name_normalized in famous_list_normalized:
        return f"Yup, {name.title()} did make the Top 20 cut!"
    else:
        return f"Sorry, {name.title()} did not make the Top 20 cut!"

# Main program loop
while True:
    try:
        famous_person = input("\nPlease enter the name of the famous individual (or 'quit' to exit): ")
        
        if famous_person.lower() == 'quit':
            print("Thank you for using the Famous People Checker!")
            break
            
        result = check_famous_individual(famous_person)
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

### Sample Output
```
Please enter the name of the famous individual: Albert Einstein
Yup, Albert Einstein did make the Top 20 cut!

Please enter the name of the famous individual: leonardo Da vinci
Sorry, Leonardo Da Vinci did not make the Top 20 cut!
```
