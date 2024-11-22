### Question 1 - Is a string method like a function? Does it run "on" an object?

A string method is similar to a function, but it is
specifically designed to operate "on" a string object.

In Python, methods are functions that are associated with
objects, and a string method operates directly on the
string it is called on.

So, specifically,

A function is a reusable block of code that you can call
with arguments to perform some action.

A method is a function that is associated with an object
and is called on that object.

String methods are invoked by using the dot '.' notation
on a string object. For example, "hello".upper() is a
method call where upper() is the method, and it operates
directly on the string "hello". This method returns
"HELLO" as it converts all the characters to uppercase.

So, string methods act like functions, but they are bound
to and operate on specific string objects, which means they
can directly modify or return transformed data related to
that string.

### Question 2 - Are Python strings “mutable” or "immutable"?

Python strings are immutable. This means that once a
string is created, it cannot be modified. You cannot
change individual characters or parts of the string
directly.

If you want to modify a string, you need to create a new
string based on the changes you want.
For example, if you have a string "hello" and want
to change it to "Hello", you cannot directly modify
the original string, but instead you must create a new one.

Here are some key implications of string immutability:

No In-Place Modification: You cannot directly alter the
characters in a string like you can with a mutable data
type, such as a list.

New String Objects: Methods that "modify" a string always
return a new string. The original string remains unchanged.

Immutable Benefits: The immutability of strings provides
some advantages:

Thread-Safety: Because strings cannot change, they are
inherently thread-safe.

Hashability: Strings can be used as dictionary keys
because their value cannot change, which ensures their
hash value is consistent.

In contrast, data types like lists are mutable, meaning their
contents can be altered after creation.

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
