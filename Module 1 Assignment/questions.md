# Module 1 Questions and Answers

## Question 1: What is a program?

A program is basically a set of instructions given to a machine to perform a specific task or a series of tasks.

The program is written in a specific programming language, and in this course, that language is Python. 

A program is responsible for laying out or defining the various decisions that must be followed by a machine in order to 
be able to come up with a solution.

The solution could include manipulating data, or even controlling other pieces of hardware.

### Main parts of a program

A program has the following parts:

#### 1 - Instructions

This is a series of statements that are given to the computer so that the execution of those
statements can result in a solution. Example of these statements could include mathematical operations, processing data
or even interacting with the user. 

#### 2 - One or more programming languages

Programs are written in languages that very from low-level Assembly all the way to high-level Python. They are mostly
written in high-level languages, such as Python, because reading the syntax of high-level languages can be easily read
by a human being. 

#### 3 - A type of program

Programs can be classified in various categories, such as application programs, system programs, utility programs, 
just to name a few. 

Application programs or Apps, are primarily created for the end users to perform specific tasks, such as using Excel to 
work with spreadsheets and browsers to surf the internet, such as Chrome. 

Then you have System programs, which manage the underlying hardware and provide services to other programs such as
operating systems. 

Then you have utility programs, and these perform system maintenance tasks such as antivirus and disk management tools.

Examples of programs include web browsers, apps like the ones in the app stores as well as web apps and desktop apps
and even video games for entertainment, which are highly interactive.

---

## Question 2: What is the difference between an interpreter and a compiler?

The basic difference between an interpreter and a compiler lies in how they process and execute a program.

### The Interpreter

The interpreter reads and executes the code line-by-line and it translates the high level code directly into machine
code at runtime, which means at the time the program is actually run.

An interpreter executes each instruction as soon as it reads the instruction. This is done without producing any
intermediate files that contain machine code. 

Interpreters also stop execution when they encounter an error and this allows the programmer to fix the errors as the
program is still running. 

The speed of interpreted programs is generally slower compared to compiled programs because the code has not been
translated to machine code beforehand, but is instead being translated to machine code at the time that it actually
runs, or runtime. 

The thing that makes interpreters different than compilers is that they have no separate compilation step, they execute
code line by line and they are more flexible for dynamic languages and allow for faster testing. 

Examples of interpreted languages include Python, Javascript, Ruby, Perl and Bash shell scripts. 

### The Compiler

The compiler's job is to translate the entire source code into machine language before the code is executed. And this is
the main difference between the interpreter and the compiler. 

The compiler executes the whole program, does all the error checking and then ends up generating an executable file,
which is a file in machine code that can then be run and distributed as a stand-alone program.

Another key difference between the interpreter and the compiler is that the compiler has to make sure that the program
is successfully compiled, which means that it has to be error-free before the program actually runs. This forces the
developer to fix all the errors before the program is executed. 

The reason why compiled programs run faster than interpreted programs is because the code translation into an executable
file from high-level to machine code is done only once, and then that executable file can then be run repeatedly without 
having to be recompiled repeatedly. 

Examples of languages that use compilers are C, C++, and Java, which compiles to bytecode which is then interpreted by
the JVM.

---

## Question 3: What is wrong with the following code?

```
line 1:  pribt ()'Hello world!")
```

There are 3 things that are wrong with this line of code.

1 - The print command has a typo in it. It should be print, and not pribt.

2 - The way the quotes are used is incorrect because they are mismatched. In Python, the string literals should always
have matching quotes - which are either single quotes ' ' or double quotes " ".

3 - Finally, there is an extra closing parentheses immediately after the opening parentheses. The correct syntax of the
function call should have matching parentheses around the argument.

Therefore the correct code is either with the double quotes:

```
print("Hello, world!")
```

Or with the single quotes:

```
print('Hello, world!')
```

---

## Question 4: What will the following program print out below the figure?

![Graph for Question 4](./graph.png)

```
Line 1 :     x = 0
Line 2 :     y = (-1/4)*(x-1)+3
Line 3 :     print(y)
```

### Answer

The standard order of operations PEMDAS is used to figure out how we will evaluate `y = (-1/4)*(x-1)+3`

1 - The first line assigns the value of 0 to the variable x.

2 - Since x is 0, we can substitute that value of x into the equation `y = (-1/4)*(x-1)+3`.

3 - This gives us `y = (-1/4)*(0-1)+3`.

4 - Simplyfying this further gives us `y = (-1/4)*(-1)+3`

5 - Now, according to PEMDAS, we evaluate the brackets first and then do the multiplication and finally the addition.

5 - Final simplification step gives us the answer `y = (1/4) + 3` which is 3.25.

6 - The print statement will output the answer 3.25 to the console.

Running the Question4.py file will show the output.

### Implementation (Question4.py)
```python
x = 0
y = (-1 / 4) * (x - 1) + 3
print(y)
```

### Sample Output
```
3.25
```
