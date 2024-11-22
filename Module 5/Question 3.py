'''
Question 3

Write a recursive Python function that returns the sum of the first n integers.
(Hint: The function will be similar to the factorial function!)
ie sum_nint(3) = 1 + 2 + 3 = 6 , sum_nint(4) = 1 + 2 + 3 + 4 = 10.

'''


def sum_nint(n):
    if n == 0:
        return 0
    return n + sum_nint(n - 1)


def main():
    while True:
        user_input = input("Enter a positive integer (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        if not user_input.isdigit() or int(user_input) == 0:
            print("Please enter a valid positive integer.")
        else:
            n = int(user_input)
            result = sum_nint(n)
            print(f"The sum of the first {n} integers is: {result}")

        print()


if __name__ == "__main__":
    main()