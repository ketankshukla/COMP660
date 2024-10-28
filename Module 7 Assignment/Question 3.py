from decimal import Decimal, getcontext, InvalidOperation

def calculate_rms_velocity(temp_celsius):

    # Check if temperature is below absolute zero
    if temp_celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15 Celsius)")

    # Set precision for decimal calculations
    getcontext().prec = 10

    try:
        # Convert constants to Decimal objects
        R = Decimal('8.3145')  # Gas constant in (kg·m2/sec2)/K·mol
        M = Decimal('3.2E-2')  # Molar mass of O2 in kg/mol

        # Convert temperature to Kelvin
        T = Decimal(str(temp_celsius + 273))

        # Calculate μrms = sqrt(3RT/M)
        rt_product = R * T
        three_rt = Decimal('3') * rt_product
        fraction = three_rt / M
        rms_velocity = fraction.sqrt()

        # Create a pattern for formatting (3 decimal places)
        pattern = Decimal('1.000')

        # Return the formatted result
        return rms_velocity.quantize(pattern)

    except InvalidOperation as e:
        raise ValueError("Error in decimal calculation. Please check input values.") from e

def get_temperature_input(prompt):

    # instead of getting input from the user from the main program,
    # I thought creating a function to get the input would be a better way of
    # handling user input because all the input checks and error handling
    # is handled here, and all the main program has to do is test against what's
    # returned.
    value = input(prompt).strip().lower()

    # Check for exit command
    if value == 'x':
        return None

    # Try to convert to float
    try:
        temp = float(value)
        return temp
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value.")

def main():

    while True:
        try:
            temperature_input = get_temperature_input("Enter temperature in Celsius or 'x' to exit program: ")

            # if the user presses 'x'
            if temperature_input is None:
                print("\nExiting program...")
                break

            # Calculate RMS velocity
            velocity = calculate_rms_velocity(temperature_input)

            print("\nThe average velocity or root mean square velocity of a molecule in a sample of oxygen")
            print(f"at {temperature_input} degrees Celsius is {velocity} m/sec\n")

        except ValueError as e:
            print(f"\nError: {str(e)}\n")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}\n")
            print("Please try again.\n")

if __name__ == "__main__":
    main()
