'''
Question 6

Write a simple function (area_circle) that returns the area of a circle of a given radius.

'''

import math

def area_circle(radius):
    # The area of the circle is PI (3.14) multiplied by the square of the radius.
    return math.pi * radius ** 2

def main():
    while True:
        user_input = input("Enter the radius of the circle (or 'q' to quit): ").strip().lower()

        if user_input == 'q':
            break

        if not user_input or not user_input.replace('.', '', 1).isdigit() or float(user_input) <= 0:
            print("Please enter a valid positive number for the radius.")
        else:
            radius = float(user_input)
            area = area_circle(radius)
            print(f"The area of a circle with radius {radius} is: {area:.2f}")

        print()


if __name__ == "__main__":
    main()