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
