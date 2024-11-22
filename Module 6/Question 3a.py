"""
IP Address Counter Module

This module counts the number of IP addresses in a multi-line string
containing network interface information. It demonstrates string
manipulation and parsing techniques in Python.

The module:
1. Splits the input string into lines
2. Counts lines containing 'inet addr'
3. Validates the format of each line
4. Provides a total count of valid IP addresses

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
