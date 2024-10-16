'''
Question 2

In mathematics, the factorial of a number n is defined as
n! = 1 ⋅ 2 ⋅ ... ⋅ n (as the product of all integer numbers from 1 to n).
For example, 4! = 1 ⋅ 2 ⋅ 3 ⋅ 4 = 24.
Write a recursive function for calculating n!

'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    while True:
        user_input = input("Enter a positive integer (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        if not user_input.isdigit():
            print("Please enter a valid non-negative integer.")
        else:
            n = int(user_input)
            result = factorial(n)
            print(f"The factorial of {n} is: {result}")

        print()


if __name__ == "__main__":
    main()