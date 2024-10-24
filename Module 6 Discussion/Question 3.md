### Question 3 - What happens when the two strings ‘Hello’ and ‘World’ are concatenated? Is a new string constructed or deconstructed?

When the two strings 'Hello' and 'World' are concatenated,
a new string is constructed. This is because strings
in Python are immutable; they cannot be changed once
they are created.

Here's what happens step-by-step:

1. You have two strings: 'Hello' and 'World'.
2. You use concatenation to join them, either with the
   '+' operator or a similar approach
3. A new string object is created to hold the result
   'HelloWorld'. Python allocates memory for this new string,
   copies the characters from both the original strings
   into this new space, and returns it as the result.
4. The original strings 'Hello' and 'World' remain unchanged.

Thus, when concatenation occurs, a completely new string
object is constructed that contains the combined characters
from both original strings. The process involves creating
a new memory allocation to store this new string since the
original strings themselves cannot be modified.

This behavior ensures that strings remain immutable.
Therefore, concatenating strings repeatedly, such as in a
loop, can be inefficient since each concatenation
constructs a new string. For such scenarios, using a
more efficient approach like joining a list of strings
is preferable:

Using .join() is often more efficient because it
constructs the final string in a single operation rather
than repeatedly creating and discarding intermediate
string objects.
