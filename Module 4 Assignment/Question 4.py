import math

def calculate_final_velocity(initial_velocity, distance):
    acceleration = 9.8
    velocity_squared = initial_velocity**2 + 2 * acceleration * distance
    final_velocity = math.sqrt(velocity_squared)
    return round(final_velocity, 1)

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

# Get user input
initial_velocity = get_valid_input("Enter the initial velocity (m/s): ")
distance = get_valid_input("Enter the distance (m): ")

# Calculate and display the final velocity
final_velocity = calculate_final_velocity(initial_velocity, distance)
print(f"The final velocity is {final_velocity} m/s.")