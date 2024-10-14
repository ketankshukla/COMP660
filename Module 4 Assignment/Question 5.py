def calculate_elapsed_time(final_velocity, initial_velocity, acceleration):
    """
    Calculate the elapsed time using the equation: t = (v - u) / a
    where v is final velocity, u is initial velocity, and a is acceleration.
    """
    elapsed_time = (final_velocity - initial_velocity) / acceleration
    return round(elapsed_time, 1)

def get_valid_input(prompt):
    """Get valid numerical input from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    print("Calculate elapsed time for an object in free fall")
    print("Equation: t = (v - u) / a")
    print("where t is elapsed time, v is final velocity, u is initial velocity,")
    print("and a is acceleration due to gravity (9.8 m/s²).")

    initial_velocity = get_valid_input("Enter the initial velocity (m/s): ")
    final_velocity = get_valid_input("Enter the final velocity (m/s): ")

    ACCELERATION = 9.8  # Constant acceleration due to gravity in m/s²

    elapsed_time = calculate_elapsed_time(final_velocity, initial_velocity, ACCELERATION)
    print(f"The elapsed time is {elapsed_time} seconds.")

if __name__ == "__main__":
    main()