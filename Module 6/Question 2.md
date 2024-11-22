#### Question 2 - Take the following Python code that stores a string: str = 'inet addr:127.0.0.1  Mask:255.0.0.0'. Use find and string slicing to extract the portion of the string after the colon inet address character and then use the rstrip function to remove any trailing characters.

Here’s my solution on how to achieve that:

```python
str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

start_position = str.find(':')

ip_address = str[start_position + 1:].split()[0].rstrip()

mask_position = str.find(':', start_position + 1)

mask = str[mask_position + 1:].rstrip()

print(f"The IP Address is - {ip_address}")
print(f"The Mask is - {mask}")
```

### What the code does:

String Creation:

Creates a string variable containing IP address and mask information
Format is 'inet addr:[IP]  Mask:[MASK]'

Finding First Colon:

start_position = str.find(':') locates the first colon
This finds the colon after 'inet addr'
Returns the index position where the colon is found

Extracting IP Address:

str[start_position + 1:] gets everything after the first colon
.split() breaks this into a list using whitespace as separator
[0] selects the first element (127.0.0.1)
.rstrip() removes any trailing whitespace

Finding Second Colon:

str.find(':', start_position + 1) finds the second colon
Starts searching after the first colon position
Returns the index position of colon after 'Mask'

Extracting Mask:

str[mask_position + 1:] gets everything after the second colon
.rstrip() removes any trailing whitespace

Output:

Prints "The IP Address is - 127.0.0.1"
Prints "The Mask is - 255.0.0.0"

You can run the above code in Question 2.py file
