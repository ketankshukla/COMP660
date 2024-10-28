def calculate_integer_range(num_bytes):

    num_bits = num_bytes * 8

    total_numbers = 2 ** num_bits

    # For signed integers:
    # - Maximum value is 2^(n-1) - 1 (where n is number of bits)
    # - Minimum value is -2^(n-1)
    max_value = (2 ** (num_bits - 1)) - 1
    min_value = -(2 ** (num_bits - 1))

    return total_numbers, min_value, max_value

def format_number(number, use_scientific):

    # use scientific notation for the output if the user enters a number greater than 10 because
    # the number gets too big to read.
    if use_scientific:
        return f"{number:.2e}"
    return f"{number:,}"

def main():

    while True:
        user_input = input("Enter number of Bytes you would like to determine the signed range of (or 'x' to exit): ")

        if user_input.lower() == 'x':
            print("Exiting program...")
            break

        try:
            num_bytes = int(user_input)

            if num_bytes <= 0:
                print("Please enter a positive number of bytes.")
                continue

            # Calculate the range
            total_numbers, min_value, max_value = calculate_integer_range(num_bytes)

            # Determine whether to use scientific notation (if bytes > 10)
            # because otherwise the numbers get too big to read.
            use_scientific = num_bytes > 10

            # Based on the above determination, this tells the format_number function
            # whether to use the scientific notation or not.
            total_formatted = format_number(total_numbers, use_scientific)
            min_formatted = format_number(min_value, use_scientific)
            max_formatted = format_number(max_value, use_scientific)

            output = (f"{num_bytes} Byte(s) integral type with 8 bits can encode {total_formatted} numbers.\n"
                      f"The signed range will be from {min_formatted} to {max_formatted}")

            print(f"{output}\n")

        except ValueError:
            print(f"Please enter a valid integer for the number of bytes.\n")

if __name__ == "__main__":
    main()
