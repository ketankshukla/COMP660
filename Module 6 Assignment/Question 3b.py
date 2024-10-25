str = '''
inet addr :127.0.0.1 Mask:255.0.0.0
inet addr :127.0.0.2 Mask:255.0.0.0

inet addr :127.0.0.3 Mask:255.0.0.0
inet addr :127.0.0.4 Mask:255.0.0.0
'''

# Use the count() method to count the occurrences of 'inet addr'
occurrences = str.count('inet addr')

print(f"Number of occurrences of 'inet addr': {occurrences}")
