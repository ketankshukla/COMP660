str = 'inet addr:127.0.0.1  Mask:255.0.0.0'

start_position = str.find(':')

ip_address = str[start_position + 1:].split()[0].rstrip()

mask_position = str.find(':', start_position + 1)

mask = str[mask_position + 1:].rstrip()

print(f"The IP Address is - {ip_address}")
print(f"The Mask is - {mask}")
