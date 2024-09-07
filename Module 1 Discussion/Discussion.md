## Question 1 - What is Python?

Python is a programming language that is categorized as a high-level language, in that the instructions that are given to Python when writing code, are given with statements that are legible to a human being. 

For instance, a statement like print("Hey there!") is a one line instruction that prints out "Hey There" in the console when the program is run. 

Unlike other languages like Assembly, writing code in Python does not require the programmer to have knowledge at the machine level using bits and bytes and registers directly. 

Also unlike other languages, the syntax of Python is very easy to read and understand by a human being because the instructions really look as though one is communicating in the English language and therefore that makes it appealing to most programmers, especially beginners that have never coded before. It is probably the least intimidating programming syntax out of all the programming languages ones that I have written code in. 

To get the line "Hello, World!" printed out in Java or C# and may other languages, the syntax that one needs to type is way more cryptic and not as legibly straight forward to read as we would read an instruction in the English language. 

For instance, here is an example of a "Hello, World!" program in Java:
```
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

And here is one in C#

```
using System;

class HelloWorld {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}
```

And here is one in C++

```
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

Here's the code in Assembly language, which absolutely nobody would use today for a very simple program like this, but this is how everything started way back when
```
section .data
    hello db 'Hello, World!',0xA  ; The message, with a newline at the end

section .text
    global _start                 ; Entry point for the program

_start:
    ; Write the message to stdout
    mov eax, 4                    ; syscall number for sys_write
    mov ebx, 1                    ; file descriptor 1 is stdout
    mov ecx, hello                ; pointer to the message
    mov edx, 13                   ; message length (13 bytes)
    int 0x80                      ; make the syscall

    ; Exit the program
    mov eax, 1                    ; syscall number for sys_exit
    xor ebx, ebx                  ; return 0 status
    int 0x80                      ; make the syscall
```

And finally, here is the program that outputs exactly the same thing in Python

```python
print("Hello, World!")
```

Notice all the cryptic syntax that the other three languages use, just to print out a simple greeting? 

With Python, it's a simple one-liner, and when you get to write bigger programs, the simplicity of Python's legibility is maintained and much easier to debug Python code than if that exact same code were to be written in the syntax of some of the languages shown above. 

These things are what made Python one of the most, if not THE most popular programming languages in the world over time, and as it stands today according to the TIOBE index, it is the number one programming language in the world.

You can see the numbers here - https://www.tiobe.com/tiobe-index/

There is also the PYPL Index, which stands for "Popularity of Programming Language" and that website also lists Python as the number one language of choice in the world as of September, 2024. You can see the stats here - https://pypl.github.io/PYPL.html

If you scroll down and look at the "Very Long Term History", you will notice that since its inception in 1991, it has consistently moved up the rankings except for 2014, where it dropped two places, but then started gaining again over the last ten years right up to 2024, where it stands at number one. 

No surprise there! Why would anyone who is getting started as a programmer, voluntarily choose any one of the other three languages shown above, if they had a choice to make on which syntax they found most appealing? 

The choice is clear to me and that's one of the reasons why I have enrolled in this course and decided to make Python THE language of choice in my career going forth. 

So here's what I like about Python:

It is simple! - Python is simple to code, as in, unlike other languages, you don't need to tell it more than you really need to, for it to do the work that it has to. Like in the case of "Hello, World!", just a one-liner is sufficient enough for it to give you what you want. You don't have to write a mini paragraph to do the same thing. I kinda like that!

It is readable! - I like that you can read it as if you're reading something naturally in the English language, and be able to grasp the logic of the code way faster than other syntax. 

And finally, Python is versatile - This means that Python can be used for a wide variety of tasks and in many areas of programming. It has libraries and frameworks, such as Django (my favourite) as well as Flask, for backend coding. It is cross platform, meaning that it can be used on Windows, macOS and Linux. It can also be integrated with other languages. 

## Question 2 - Why do people use Python?

Well, as I have stated in the first question, there are a few reasons why Python is an extremely appealing programming language, to both complete beginners as well as seasoned experts. They are, simplicity, readability and versatility. 

But there are other factors that makes Python appealing.

It is easy to learn! When a programmer is not intimidated by the syntax of the language, that then gives them a peace of mind, especially when they don't have to worry about extra lines of code to get a very simple thing done, like printing out "Hello, World!". When something becomes easy to learn, then it also becomes comforting to actually WANT to code in that language.

I have to be honest with you, out of all the programming languages I have ever written code in, Python is the ONLY programming language where I actually smile while writing code. Imagine that! The simplicity, readability and versatility all make me feel good. I try to make it a habit to write code in such a way, that if I were to pass the code off to someone else, they would understand it faster than in any other language out there - and when I use Python to write that code, it's a breeze for them to understand what's going on. I know so many people who have switched from other languages to Python, because in the end, why not work with a language where the syntax is almost human-like. It's a natural appeal! 

Now having said that, because Python is not a compiled language, but instead an interpreted language, it may not boast the fastest execution times. But for what it's worth, most tasks can be accomplished relatively quickly with Python albeit not in the fastest way, as compiled code might allow. But the hardware these days is so incredibly amazing, that executing interpreted code today is way faster than when I used to code decades ago. I remember using Visual Basic 3 back in the early 90s had no compiler, and it crawled back then. Today it's much different. 

Another reason why people use Python is because it has such a rich ecosystem, meaning that it has libraries and frameworks that can be used to speed up development significantly. There used to be a time when I had a fascination of writing every line of code by myself to feed my developer's ego of having ownership of that code. Then I realized that I was re-inventing the wheel by doing that instead of using libraries that someone else had already written and that I can simply use by plugging it into my existing code within seconds. I realized I was wasting time. From that day onwards, I learnt that writing code is not about feeding my ego, it's about getting things done in the most efficient way possible - and when you use a codebase that has been working and tested for years and years, then why bother writing it from scratch? 

So back to my point - Python libraries are very easy to use and can significantly speed up your programming. 99% of the code that you will ever need already exists in a library out there. The 1% is code that is specific to your company's business rules, and that is the code that most developers are actually writing. Because that code is unique to their needs and it doesn't exist anywhere else. 

Another reason why people use Python is because of its cross platform compatibility. When you can use a language that is supported by multiple operating sytems, then you will not need to learn another programming language just because you are switching from say, Linux to Windows. Back in the day, we could only code C# on a Windows platform because you needed the .NET framework and that did not exist for Linux and Mac. However that changed over the years.

Python, on the other hand, has always been designed be cross-platform from the early days and then over time it has also been refined to work on platform-specific tasks, such as libraries that have to deal directly with the workings of a specific operating system.

Another reason is that Python abstracts system-level programming that developers directly deal with in languages such as C or C++, and that makes Python programs largely independent of the underlying operating system. The proper installation of the Python interpreter will make sure of this so that we as developers don't have to worry about it. 

## Question 3 - What can I do with Python?

Python can be used for web development, data science and analysis of data, machine learning and artificial intelligence, automation and scripting, game development, desktop application development, scientific computing, cybersecurity, networking, DevOps, internet of things, education and learning, cloud computing, robotics, blockchain development, audio and video processing, testing - amongst many other things!

I'm not going to go into every one of these, but suffice it to say that this is a vast arena of possibilities where Python can be used to create and implement solutions. Entire careers, industries and technology-specific job descriptions have been created on some of these things listed above and from my basic research of a few searches over the internet, it is apparently obvious that Python is the choice of languages in many of these areas because it can get the job done without unnecessary complicated extra code that other languages might require a programmer to know. 

You can also do something really special with Python - and that is to have little kids learn the language quickly because the syntax is intuitive. 

Python has something called the REPL, which stands for Read-Eval-Print Loop. It is an interactive programming environment that allows users to enter one line of code (or an expression) at a time, which is then immediately read by the interpreter, evaluated (executed), the result is printed, and the system returns to the input prompt to allow further input, hence the loop. It gives instant feedback when kids type code into the REPL. This instant feedback can help reinforce learning, but also makes coding fun as they can quickly see what their code does. Python is great for beginners, as I have already stated, it has lots of learning resources for kids and for pretty much everyone else too! 

With Python, you can easily transition to more complex projects like web development, game design, AI and robotics without having to switch languages. 
 
With Python, you can also get things done fast because unlike other languages like C and C++ that require understanding of memory management and pointers, which can confuse new learners (I have first hand experience with this!), Python abstracts away these complexities so that you as a developer, don't have to worry about explicitly managing the underlying functionality and that allows you to focus on what you need to get done. 

Python can also be used to create prototypes really fast because of it's simplicity and clean syntax. It doesn't require code to be compiled and therefore allowing for faster iterations. You can write, run and test your code almost instantly without complicated setups, thus making it really easy to experiment with new ideas in a jiffy. 

Of course, third party libraries make a world of difference as I mentioned above, reusability of code in python is really a joy compared to other languages. 

And finally, Python can be used for integration with API services, which in my experience, is easier than with other languages. You can create the APIs with the Django framework, which is also built in Python, and then consume the API with Python code in your front-end applications. 