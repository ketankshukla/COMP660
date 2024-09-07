## What is the difference between an interpreter and a compiler?

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







