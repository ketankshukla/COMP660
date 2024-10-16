'''
Question 7

Write a lambda function (area_circle_lambda) that returns the area of a circle of a given radius.
'''

import math

# Using the lambda function to return the area of a circle.
area_circle_lambda = lambda radius: math.pi * radius ** 2


def main():
    while True:
        user_input = input("Enter the radius of the circle (or 'q' to quit): ").strip().lower()

        if user_input == 'q':
            break

        if not user_input or not user_input.replace('.', '', 1).isdigit() or float(user_input) <= 0:
            print("Please enter a valid positive number for the radius.")
        else:
            radius = float(user_input)
            area = area_circle_lambda(radius)
            print(f"The area of a circle with radius {radius} is: {area:.2f}")

        print()  # Add a blank line for readability


if __name__ == "__main__":
    main()