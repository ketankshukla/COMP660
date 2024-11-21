# Module 7: Number Systems and Scientific Calculations 📚

[← Back to Main Documentation](../../README.md)

## Overview 🎯
Module 7 focuses on number systems, mathematical constants, and scientific calculations in Python. Students learn to work with different number formats, implement scientific formulas, and handle precise calculations.

## Learning Objectives 🎓
- Format mathematical constants
- Calculate integer ranges
- Implement scientific formulas
- Handle precise calculations
- Work with different number systems

## Assignments 📝

### Question 1: Mathematical Constants
Format and display mathematical constants like π (pi) and τ (tau).

**Implementation:**
```python
import math

def format_tau():
    tau = 2 * math.pi
    half_tau = math.pi

    formatted_string = f"The value of Tau is {tau:^8.3f}, which is two times {half_tau:^8.3f}."

    print(formatted_string)

format_tau()
```

### Question 2: Integer Range Calculator
Calculate the range of signed integers for a given number of bytes.

**Implementation:**
```python
def calculate_integer_range(num_bytes):
    """
    Calculate the range of signed integers for a given number of bytes.
    """
    num_bits = num_bytes * 8
    total_numbers = 2 ** num_bits

    # For signed integers:
    # - Maximum value is 2^(n-1) - 1 (where n is number of bits)
    # - Minimum value is -2^(n-1)
    max_value = (2 ** (num_bits - 1)) - 1
    min_value = -(2 ** (num_bits - 1))

    return total_numbers, min_value, max_value

def format_number(number, use_scientific):
    """
    Format large numbers using scientific notation if needed.
    """
    if use_scientific:
        return f"{number:.2e}"
    return f"{number:,}"

def main():
    while True:
        user_input = input("Enter number of Bytes (or 'x' to exit): ")

        if user_input.lower() == 'x':
            print("Exiting program...")
            break

        try:
            num_bytes = int(user_input)
            if num_bytes <= 0:
                print("Please enter a positive number of bytes.")
                continue

            # Calculate range and format output
            total_numbers, min_value, max_value = calculate_integer_range(num_bytes)
            use_scientific = num_bytes > 10

            # Format numbers
            total_formatted = format_number(total_numbers, use_scientific)
            min_formatted = format_number(min_value, use_scientific)
            max_formatted = format_number(max_value, use_scientific)

            print(f"\nTotal possible numbers: {total_formatted}")
            print(f"Range: {min_formatted} to {max_formatted}")

        except ValueError:
            print("Please enter a valid number.")
```

### Question 3: Root Mean Square Velocity
Calculate the root mean square velocity of oxygen molecules at a given temperature.

**Implementation:**
```python
from decimal import Decimal, getcontext, InvalidOperation

def calculate_rms_velocity(temp_celsius):
    """
    Calculate the root mean square velocity of oxygen molecules at a given temperature.

    Args:
        temp_celsius (float): Temperature in Celsius

    Returns:
        Decimal: Root mean square velocity in m/s, formatted to 3 decimal places

    Raises:
        ValueError: If temperature is below absolute zero or if decimal calculation fails
    """
    # Check if temperature is below absolute zero
    if temp_celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15 Celsius)")

    # Set precision for decimal calculations for answer to come to 6 significant figures
    # for example 435.321 m/s
    getcontext().prec = 6

    try:
        # Convert constants to Decimal objects
        gas_constant_r = Decimal('8.3145')  # Gas constant in (kg·m2/sec2)/K·mol
        molar_mass_m = Decimal('3.2E-2')  # Molar mass of O2 in kg/mol

        # Convert temperature to Kelvin
        kelvin_temp_t = Decimal(str(temp_celsius + 273))

        # Calculate μrms = sqrt(3RT/M)
        rt_product = gas_constant_r * kelvin_temp_t
        three_rt = Decimal('3') * rt_product
        fraction = three_rt / molar_mass_m
        rms_velocity = fraction.sqrt()

        # Create a pattern for formatting (3 decimal places)
        pattern = Decimal('1.000')

        # Return the formatted result
        return rms_velocity.quantize(pattern)

    except InvalidOperation as e:
        raise ValueError("Error in decimal calculation. Please check input values.") from e

def get_temperature_input(prompt):
    """
    Get and validate temperature input from the user.

    Args:
        prompt (str): The prompt message to display

    Returns:
        float or None: Temperature value or None if user wants to exit

    Raises:
        ValueError: If input is not a valid number
    """
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
    """Main program loop for calculating root mean square velocity."""
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
```

## Implementation Details 🔧

### Number Systems
- Binary calculations
- Scientific notation
- Decimal precision

### Mathematical Operations
- Constants (π, τ)
- Integer arithmetic
- Scientific formulas

### Input/Output
- Number formatting
- Unit conversion
- Precision handling

## Best Practices 📝
1. Use appropriate number types
2. Handle precision correctly
3. Validate numerical input
4. Document calculations

## Common Issues and Solutions 🤔
1. **Precision Errors**
   - Issue: Floating point inaccuracy
   - Solution: Use Decimal type

2. **Large Numbers**
   - Issue: Number formatting
   - Solution: Scientific notation

3. **Input Validation**
   - Issue: Invalid numerical input
   - Solution: Type checking

## Related Resources 📚
1. [Python Decimal Module](https://docs.python.org/3/library/decimal.html)
2. [Python Math Module](https://docs.python.org/3/library/math.html)
3. [Number Systems in Python](https://docs.python.org/3/library/numbers.html)

## Assessment Criteria 📝
1. **Accuracy (40%)**
   - Correct calculations
   - Proper precision handling
   - Accurate range calculations
   - Valid results

2. **Code Quality (25%)**
   - Clean and organized code
   - Proper documentation
   - Efficient implementation
   - Good variable naming

3. **Error Handling (20%)**
   - Input validation
   - Range checking
   - Exception handling
   - User feedback

4. **Output Formatting (15%)**
   - Clear presentation
   - Appropriate precision
   - Consistent formatting
   - Professional output

## Advanced Topics 🔥
1. **Binary Arithmetic**
   - Two's complement representation
   - Bit manipulation
   - Integer overflow handling

2. **Scientific Computing**
   - High-precision calculations
   - Physical constants
   - Unit conversions
   - Error propagation

3. **Performance Optimization**
   - Efficient algorithms
   - Memory usage
   - Calculation speed
   - Precision trade-offs
