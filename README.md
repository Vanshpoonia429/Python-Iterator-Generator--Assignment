# Python-Iterator-Generator--Assignment

Question 1:What is a function in Python? Explain how functions are created and called. Also
explain parameters, arguments, default parameters, *args, and **kwargs with suitable
examples.

Answer:

A function in python is a reusable block of code designed to perform a specific task. Functions helps make programs modular, readable, and reusable.

Creating and calling a function

A function is created using the def keyword.

Syntax: 
 
def function_name(parameters):
      # function body
      statements
      return value

Example:

def greet():
      print(“Hello, World!”)

# Calling the function
greet()

Output:-     Hello, World!

Here, greet is the function name, and greet() is used to call or execute the function.

Parameters and Arguments

A parameters is a variable written in the function definition. An argument is the actual value passed to the function when it is called.

Example:

def add(a, b):                       # a and b are parameters
      Return a + b                  

Result = add(10, 20)            # 10 and 20 are arguments
print(result)

Output:-     30

Default Parameters

A default parameters has a default value that is automatically used if the caller does not provide an argument.

Example:

Def greet(name=”Guest”):
       print(“Hello”, name)

greet(“Rahul”)
greet()

Output:-    Hello Rahul
                 Hello Guest

In this example, “Guest” is the default value of the name parameter.

*args

*args allows a function to accept any number of positional arguments. Inside the function, args is treated as a tuple.

Example:

def add_numbers(*args):
       Total = 0
        For number in args:
               Total += number
        Return total

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))

Output:-      30
                   100

The * collect multiple positional arguments into a tuple.

**kwargs

**kwargs allows a function to accept any number of keyword arguments. Inside the function, kwargs is treated as a dictionary.

Example:

Def student_info(**kwargs):
       For key, value in kwargs.items():
             print(key, “:”, value)

student_info(name=”Amit”, age=20, course=”Python”)

Output:-         name : Amit
                      age : 20
                      course : Python


Question 2: What is variable scope in Python? Explain local and global variables. Why should
excessive use of the global keyword be avoided? Also explain nested functions and closures

Answer:

Variable scope refers to the region of a program where a variable can be accessed or used. In Python, the scope of a variable depends on where it is defined.
Python mainly has local scope and global scope. It also supports enclosing and built-in-scopes.

Local Variable

A variable that is defined inside a function is a called a local variable. It can normally be accessed only within that function.

Example:

def display
      x = 10
      print(“Value of x;”, x)
display()

Output:-       Value of x: 10

Here, x is a local variable because it is created inside the display() function.
Global Variables

A variable that is defined outside all functions is called a global variable. It can be accessed from different parts of the program, including inside functions.

Example:

x = 20

def display():
       print(“Value of x:”, x)

display()
print(“Value of x:”, x)

Output:-    Value of x: 20
                 Value of x: 20

            Here, x is a global variable.

            Global Keyword

            If we want to modify a global variable inside a function, we use the global keyword.

           x = 10

           def change():
           global x
           x = 50

           change()
           print(x)

          Output:-      50

          The global keyword tells python that z refers to the global variable rather than creating a new
          local variable.         


Why should excessive use of global be avoided?

Excessive use of the global keyword should be avoided because:
It makes the program difficult to understand.
It makes debugging difficult, because a global variable can be changed from different function
It created dependencies between functions.
It may cause unexpected changes in program data.
It reduces the reusability and maintainability of the code.

          Therefore, it is generally better to use local variable, function parameters, and return   values whenever possible.

Nested Functions

A nested function is a function defined inside another function. The inner function can normally be called from within the outer function.

Example:

def outer():
      print(“This is outer function”)

      def inner():
             print(“This is inner function”)
inner()

outer()

Output:-      This is outer function
                    This is inner function

Here, inner() is a nested function because it is defined inside outer().

Nested function are useful when a function is needed only for a specific task inside another function


Closures


A Closure is created when an inner function remembers and uses a variable from its enclosing function, even after the enclosing function has finished executing.

Example:

def outer(x):
      def inner(y):
              return x + y
       
       return inner

add = outer(10)
print(add(5))
print(add(20))


Output:-      15
                   30


Question 3: What is recursion in Python? Explain how a recursive function works. What is a
base condition, and why is it important?
Explain recursion using the factorial of a number as an example.

Answer:

Recursion is a process in which a function calls itself to solve a problem. A recursive function breaks a problem into smaller parts of the same problem until it reaches a condition where no further calls are required.

How does a Recursive Function Works?

A recursive function generally has two important parts:

Base Condition :- It stops the recursion.
Recursive Call :- The function calls itself with a smaller or simpler input.

Base Condition

The base condition is the condition that tells the recursive function when to stop calling itself.
It is very important because it prevents infinite recursion and allows the function to return a final result.

Example: Factorial Using Recursion

The factorial of a positive integer n is defined as:

n! = n x (n - 1) x (n - 2) x (n - 3) x …. x 1

For example:

5! = 5 x 4 x 3 x 2 x 1  = 120

The factorial can be defined recursively as:

0! = 1  -> Base condition
n! = n x (n - 1)!  -> Recursive case

Python Program

def factorial(n):
       if n == 0:                                      # Base condition
            return 1
       else:
             return n * factorial(n - 1)         # Recursive call
       
print(factorial(5))

Output:-      120


Question 4:What is the difference between an iterable, an iterator, and a generator in Python?
Explain the purpose of iter(), next(), StopIteration, and yield

Answer:

In python, iterable, iterator, and generator are used to access elements one at a time, but they have different meanings and purposes.

Iterable

An iterable is an object whose elements can be accessed one by one. 
Examples include list, tuple, string, set and dictionary.

An iterable can be converted into an iterator using the iter() function.

Example:

numbers = [10, 20, 30]

For num in numbers:
       print(num)

Here, numbers is an iterable.

Iterator

An iterator is an object that produces values one at a time. It keeps track of its current position and uses the next() function to return the next value.

Example:

Numbers = [10, 20, 30]

It = iter( numbers)

print(next(it))
print(next(it))
print(next(it))

Output:-   10
                20
                30

Generator

A generator is a special type of iterator that is created using a function containing the yield keyword.

Generators produce values one at a time, which makes them useful for handling large amount of data efficiently.

Example:

def numbers():
       yield 10
       yield 20
       yield 30

For num in numbers():
      print(num)

Output:-   10
                20
                30

Purpose of iter()

The iter() function is used to create an iterator from an iterable.
         Numbers = [10, 20, 30]
         it = iter(numbers)

Here, numbers is an iterable and it is an iterator.

Purpose of next()

The next() function is used to get the next value from an iterator.

          it = iter([10, 20, 30])

          print(next(it))
          print(next(it))

       Output:-     Each time next() is called, the iterator moves to the next element.

Stoplteration

When an iterator has no more elements, calling next() raises the stoplteration exception.

it = iter([10, 20])

print(next(it))
print(next(it))
print(next(it))

The third next() call raises Stoplteration because there are no more elements.

A for loop handles this exception automatically.

Propose of yield

The yield keyword is used to create a generator. It produces a value and temporarily pauses the function. When the next value is requested, the function continues from where it stoped.

Def count():
       yield 1
       yield 2
       yield 3

c = count()

print(next(c))
print(next(c))
print(next(c))

Output:-    1
                 2
                 3


Question 5: What is a lambda function? Explain how map(), filter(), and reduce() work
in Python with suitable examples.

Answer:

Lambda Function

A lambda function is a small, anonymous function in python. It is created using the lambda keyword and is generally used when a simple function is required for a short period.

Syntax:-
              Lambda arguments: expression

Example:-

Square = lambda x: x * x
print(square(5))

Output:-      25

Here, lambda x : x * x takes x as an argument and returns its square.

map() Function

The map function is used to apply a function to every element of an iterable. It returns a map object, which is an iterator.

Syntax:-    map(function, iterable)

Example:-    

Numbers = [1, 2, 3, 4, 5]
Squares = map(lambda x : x * x, numbers)
print(list(squares))

Output:-    [1, 4, 9, 16, 25]
filter() Function

The filter() function is used to select elements from an iterable that satisfy a given condition. It returns only the elements for which the function returns True.

Syntax :-      filter(function, iterable)

Example:- 

Numbers = [1, 2, 3, 4, 5, 6]
Even_numbers = filter(lambda x : x % 2 == 0, numbers)
print(list(even_numbers))

Output:-     [2, 4, 6]

Here, filter() select only the even numbers.

reduce() Function

The reduce() function is used to apply a function cumulatively to the elements of an iterable, reducing them to a single value.

reduce() is available in the functools module.

Syntax:-     reduce(function, iterable)

Example:- 

from functools import reduce
            numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y : x * y, numbers)
print(result)

Output:-    120
