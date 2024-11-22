"""
IP Address Counter Using String Count Method

This module demonstrates an alternative approach to counting IP addresses
in a multi-line string using Python's built-in string count() method.
Unlike the previous version that used line-by-line parsing, this approach
directly counts occurrences of the 'inet addr' pattern.

Note: This method assumes that 'inet addr' appears exactly once per IP address
and that all occurrences indicate valid IP addresses.

Example Input Format:
    inet addr :127.0.0.1 Mask:255.0.0.0
    inet addr :127.0.0.2 Mask:255.0.0.0

Author: [Your Name]
Date: [Current Date]
"""

# Multi-line string containing network interface information
str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

# Use the count() method to count the occurrences of 'inet addr'
occurrences = str.count('inet addr')

# Output the total count
print(f"Number of occurrences of 'inet addr': {occurrences}")
