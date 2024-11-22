#### Question 3a:

```
Using a for loop through a string, count the number of 
internet addresses in the string below by using 
the split method.

Line 1      str = \
Line 2      '''
Line 3      inet addr :127.0.0.1 Mask:255.0.0.0
Line 4      inet addr :127.0.0.2 Mask:255.0.0.0

Line 5      inet addr :127.0.0.3 Mask:255.0.0.0
Line 6      inet addr :127.0.0.4 Mask:255.0.0.0
Line 7      '''
```

You can count the number of internet addresses (IP addresses)
in the string by using a `for` loop to iterate through each
line of the string. The `split()` method can then be used to
isolate the portions of each line where the IP addresses are located.

Here’s my solution to this problem:

```python
str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

lines = str.splitlines()
ip_count = 0

for line in lines:
    if 'inet addr' in line:
        parts = line.split(':')
        if len(parts) > 1:
            ip_address = parts[1].split()[0]
            ip_count += 1

print(f"Number of internet addresses: {ip_count}")
```

### Explanation:

1. `splitlines()` splits the multi-line string into individual lines.
2. The `for` loop iterates over each line.
3. If a line contains `'inet addr'`, it splits the line by `':'` to isolate the IP address section.
4. The code then extracts the IP address using further splitting (`split()` by space) and increments the `ip_count`
   counter.
5. Finally, it prints the total count of internet addresses.

Running this code will output:

```
Number of internet addresses: 4
```

You can run the above code in Question 3a.py file
