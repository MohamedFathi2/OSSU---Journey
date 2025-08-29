def f(expr, old_list, test = lambda x : True):
    new_list = []
    for e in iter:
        if test(e):
            new_list.append(expr(e))
    return new_list

# For Example
# [expression for element in iterable {ex: range(n)} if test (condition)]
new = [e**2 for e in range(6)]
print(new)
new2 = [element**2 for element in range(9) if element % 2 == 0]
print(new2)

# list comprehension provides a convenient way to initialize list.
# For Example: [[] for _ in range(10)] → generates a list containing 10 distinct [i.e., non-aliased] empty lists.
# The variable _ indicates that the values of that variable are not used in generating the elements of the lits, i.e., it is merely a PLACEHOLDER for the loop.
# This convention is common in python programs.
new3 = [0 for _ in range(10)]
print(new3)


# Python allows multiple for statements [nested loops] within a list comprehension. Consider the code:
L = [(x, y)
     for x in range(6) if x % 2 == 0
     for y in range(6) if y % 3 == 0
]
print(L) # [(0,0), (0,3), (2,0), (2,3), (4, 0), (4,3)]

print([[(x,y) for x in range(6) if x % 2 == 0] # only if x is dividable by 2
    for y in range(6) if y % 3 == 0 # only if y is dividable by 3 
    ]) # add both x and y then

# Detailed explanation:
# This line creates a list of lists using a nested list comprehension.
# Outer list: for each y in range(6) (i.e., y = 0, 1, 2, 3, 4, 5), but only if y is divisible by 3 (so y = 0 and y = 3).
# For each such y, the inner list comprehension runs:
#   It loops over x in range(6) (x = 0, 1, 2, 3, 4, 5), but only includes x if x is divisible by 2 (so x = 0, 2, 4).
#   For each valid x, it creates a tuple (x, y).
# The result is a list with one sublist for each valid y (0 and 3), and each sublist contains all (x, y) pairs for valid x.
# So the output is:
# [[(0, 0), (2, 0), (4, 0)], [(0, 3), (2, 3), (4, 3)]]


print([[(x,y) for x in range(6) if x % 2 == 0] # the elements of this would be lists of elements (tuples) (x, y) and works when x is dividable by 2 (the inner loop) and when y is dividable by 3 (the outer loop)
       for y in range(6) if y % 3 == 0
       ])

'''
The outer loop iterates over y in range(6), but only includes y values divisible by 3 (so y = 0 and y = 3).
For each such y, the inner list comprehension iterates over x in range(6), but only includes even x values (x = 0, 2, 4).
For each valid x, it creates a tuple (x, y).
The result is a list of lists: each sublist contains all (x, y) pairs for a specific valid y.
The output is:
[[(0, 0), (2, 0), (4, 0)], [(0, 3), (2, 3), (4, 3)]]
'''



'''
use nested list comprehensions to generate a list of all prime numbers less than 100. 
The basic idea is to use one comprehension to generate a list of all of the candidate numbers 
(i.e., 2 through 99), 
a second comprehension to generate a list of the remainders of dividing a
candidate prime by each potential divisor, and the built-in function
all to test if any of those remainders is 0.
'''


'''
This line of code creates a list called primeNumbers2To100 that is intended to contain all prime numbers between 2 and 99. It uses a list comprehension to iterate through each integer x in the range from 2 up to (but not including) 100. For each x, it checks whether all numbers y in the range from 3 up to (but not including) x do not divide x evenly (i.e., x % y != 0). The all() function returns True only if every value in the generator expression is True, meaning that x is not divisible by any y in that range.

If this condition is met, x is considered a prime number and is included in the resulting list. However, there is a subtle issue: the code does not check divisibility by 2 for numbers greater than 2, so even numbers greater than 2 will be incorrectly included as primes. For example, 4 will be included because the range range(3, 4) is empty, so all() returns True by default. To fix this, the range for y should start at 2 instead of 3.

Despite this flaw, the code demonstrates how to use list comprehensions and the all() function to filter numbers based on a condition involving all elements in another range. This approach is concise and leverages Python's expressive syntax for generating filtered lists.
'''
primeNumbers2To100 = [x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))]
# this is the same as implementing this function:
'''
def gen_primes():
    primes = []
    for x in range(2, 100):
        is_prime = False
        for y in range(2, x):
            if x % y == 0:
                is_prime = False
        if is_prime:
            primes.append(x)
    return primes
'''
print(primeNumbers2To100)