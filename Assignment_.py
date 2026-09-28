Question 6:  Write a Python function called calculate_total() that:

1. Accepts any number of marks using *args.
2. Calculates the total marks.
3. Uses a default bonus value of 5.
4. Adds the bonus to the total.
5. Returns the final result

Answer:

Def calculate_total(*args, bonus = 5):

       Total = sum(args)
       final_result = total + bonus
       return final_result

print(calculate_total(80, 75, 90))

Output:-    250

Question 7:  Write a recursive Python function to reverse a string.
Use the string:

"Python"

Display both the original and reversed strings...

Answer:

Def reverse_string(s):
    
    if len(s) == 0:
       return s

    Return reverse_string(s[1:]) + s[0]

text = “Python”

reversed_text = reverse_string(text)

print(“Orignai string:”, text)
print(“Reversed string:”, reversed_text)

Output:- 

Original string:  Python
Reversed String:  nohtyp


Question 8: Create a custom iterator class called EvenNumbers that generates even
numbers from 2 to 10.

Use __iter__(), __next__(), and StopIteration

Answer: 
 
class EvenNumbers:

       def __init__(self):
                 self.sum = 2

       def __iter__(self):
                 return self

       def __next__(self):
             if self.num <= 10:
                   value = self.num
                   self.num += 2
             else:
                   raise StopIteration

even = EvenNumbers()

for num in even:
     print(num)

Output:-

2
4
6
8
10
          

Question 9:  Write a generator function that accepts a number n and generates all even
numbers from 1 to n.

Use yield instead of returning a list.

Answer:

def even_numbers(n):
      for i in range(1, n + 1):
             if i % 2 == 0:
                  yield i
n = 10

for num in even_numbers(n):
      print(num)

Output:-

2
4
6
8
10

Question 10:  Consider the following list:

numbers = [1, 2, 3, 4, 5, 6]

Write a Python program to:
1. Use map() to calculate the square of every number.
2. Use filter() to select only even numbers.
3. Use reduce() to calculate the sum of all numbers.
4. Display all three results.

Answer:

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. Calculate square of every number using map()

square = list(map(lambda x : x ** 2, numbers))

# 2. Select even numbers using filter()

Even_numbers = list(filter(lambda x : x % 2 == 0, numbers))

# 3. Calculate sum all numbers using reduce()

total = reduce(lambda x, y : x + y, numbers)

# 4. Display all results

print(“squares:”, squares)
print(“Even numbers:”, even_numbers)
print(“Sum:”, total)

Output:- 

Squares : [1, 4, 9, 16, 26, 36]
Even numbers : [2, 4, 6]
Sum : 21
