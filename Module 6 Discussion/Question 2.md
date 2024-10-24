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
