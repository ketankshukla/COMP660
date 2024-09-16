# The initial values of length and widthen in the question.

length = 10.0
width = 7

# Expressions and their evaluations stored in variables, as given in the question

expr1 = width // 2
expr2 = length / 2.0
expr3 = length / 2
expr4 = 1 + 4 * 5

# My answer:

# I decided to use the __name__ property of the type function at the end of the type function
# that then shows the proper English name of the type
# For instance, instead of Type: <class 'int'>, it shows Type: int
# I've used the f string to avoid manual concatenetion and formatted each line in the group
# to be in a new line by using the newline characyer "\n"

# The // operator is used for floor division (integer division).
# It divides width by 2 and returns the largest whole number less than or equal to the result.
print(f"Expression: width // 2\nValue: {expr1}\nType: {type(expr1).__name__}\n")
# The / operator performs floating-point division.
# This means that it divides the two numbers and returns the result as a float,
# even if the division results in a whole number, the result is always a float.
print(f"Expression: length / 2.0\nValue: {expr2}\nType: {type(expr2).__name__}\n")
# Once again, the / operator performs floating-point division.
# It divides length by 2 and returns the result as a float.
print(f"Expression: length / 2\nValue: {expr3}\nType: {type(expr3).__name__}\n")
# This expression involves both addition and multiplication and according to PEMDAS rules,
# multiplication is performed before addition.
print(f"Expression: 1 + 4 * 5\nValue: {expr4}\nType: {type(expr4).__name__}\n")
