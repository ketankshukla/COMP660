#### 3b. Use the count() method to return the number of occurrences of the substring in the given string.

You can use the `count()` method to return the number of occurrences
of a substring within a string.

Here’s my solution using the example string provided earlier:

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

- `count('inet addr')` directly counts the number of times
  the substring `'inet addr'` appears in the string.

Running this code will output:

```
Number of occurrences of 'inet addr': 4
``` 

This method directly counts how many times the specified
substring appears in the entire string.

You can run the above code in Question 3b.py file
