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
