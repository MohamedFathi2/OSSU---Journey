# List comprehension:
# [expression for element in iterable if test]
# l = [1, 2, 3, 4, 5, 6]
# newL = [element**2 for element in l]
# print(newL)
# newEvenL = [element**2 for element in l if element % 2 == 0]
# print(newEvenL)

# l = [[[(x,y) for x in range(6) if x % 2 == 0]
#       for y in range(6) if y % 3 == 0]]
# print(l)

# -----
# Default Parameter

'''
def bisection_root(x : int, epsilon = 0.01):
    low = 0
    high = x
    guess = (low + high) / 2.0
    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        elif guess**2 > x:
            high = guess
        guess = (low + high) / 2.0
    return guess
print(bisection_root(123))
'''

# Functions Returning Functions
def make_prod(a):
    def g(b): # this function def is inside another function.
        return a * b
    return g # we are not doing a FUNCTION CALL, we are returning a function object.

# both of the following pieces of code are the same.
# ---
val = make_prod(2) (3)
print(val)
# ---
doubler = make_prod(2)
val = doubler(3)
print(val)
# ---