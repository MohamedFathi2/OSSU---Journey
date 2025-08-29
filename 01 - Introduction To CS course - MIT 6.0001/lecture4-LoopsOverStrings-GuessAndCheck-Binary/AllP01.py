# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 16:57:07 2025

@author: HP
"""

# even_nums = 0
# for i in range(5):
#     if i % 2 == 0:
#         even_nums += 1
# print(even_nums)

# Count the unique letters that are in a string

# s = "abca"
# seen = ""
# count = 0
# for char in s:
#     if char not in seen:
#         seen += char
#         count += 1        
# print(f"Number of unique letters in string s: {count}")


# Guess and check Square root with while loop

# guess = 0
# x = int(input("Enter an integer: "))
# while guess**2 < x: # Exit while loop when guess**2 >= x
#     guess = guess + 1

# if guess**2 == x:
#     print(f"Square root of {x} is {guess}")
# else:
#     print(f"{x} is not a perfect square")

secretNumber = 4
found = False
for i in range(1, 11):
    if i == secretNumber:
        print(secretNumber)
        found = True
        break
if not(found):
    print("Number not found.")


# Finger Exercise:
'''
Assume you are given a positive integer variable named N. Write a piece of Python code that finds the cube root of N.
The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
Hint: use a loop that increments a counter—you decide when the counter should stop.
'''


# N = int(input("Enter an integer: "))
# guess = 0
# while guess**3 < N:
#     guess += 1
# if guess**3 == N:
#     print(f"Cube root of {N} is {guess}")
# else:
#     print(f"{N} is not a perfect Cube")

# b = a - 2
# c = 2a
# a + b + c = 10
# a + a - 2 + 2 a = 10
# 4a - 2 = 10
# 4a = 12
# a = 3
# b = 1
# c = 6   