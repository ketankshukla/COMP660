"""
IP Address and Mask Extractor Module

This module demonstrates string manipulation in Python by extracting
an IP address and network mask from a formatted string. It uses string
methods like find(), split(), and rstrip() to parse the input string.

Example Input Format:
    'inet addr:127.0.0.1  Mask:255.0.0.0'

Author: [Your Name]
Date: [Current Date]
"""

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
