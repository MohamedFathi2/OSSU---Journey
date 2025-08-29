# Fix the code
'''
def is_triangular(n):
    """n is an int > 0
    Returns true if n is triangular, i.e Equals a continued summation of natural numbers
    (1+2+3+...+k), False Otherwise
    """
    total = 0
    for i in range(n):
        total += i
        if total == n:
            print(True)
    print(False)
'''

# def is_triangular(n):
#     """n is an int > 0
#     Returns true if n is triangular, i.e Equals a continued summation of natural numbers
#     (1+2+3+...+k), False Otherwise
#     """
#     total = 0
#     for i in range(n + 1):
#         total += i
#         if total == n:
#             return True
#     return False


# print(is_triangular(4))
# print(is_triangular(6))
# print(is_triangular(1))


# -----------------------
def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (low + high) / 2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 > x:
            high = ans
        else:
            low = ans
        ans = (low + high) / 2.0
    return ans

# print(bisection_root(4))
# print(bisection_root(123))

# ----------------
# def count_nums_with_sqrt_close_to(n, epsilon):
#     """n is an int > 2
#         epsilon is a positive number < 1
#     Returns how many integers have a square root within +ve or -ve epsilon interval
#     """
#     counter = 0
#     for i in range(n**3):
#         # take the square root of i
#         sqrt = bisection_root(i)
#         if abs(n - sqrt) <= epsilon:
#             # we know that sqrt is within epsilon
#             print(i, sqrt)
#             counter += 1
#     return counter

# print(count_nums_with_sqrt_close_to(10, 1))

def apply(criteria, n):
    """
    * criteria is a function that takes in a number and returns a bool
    * n is an int
    Returns how many ints from 0 to n (inclusive) match
    the criteria (i.e. return True when run with criteria)
    """
    count = 0
    for i in range(n + 1):
        if criteria(i):
            count += 1
    return count
def is_even(x):
    return x % 2 == 0
def is_odd(x):
    return x % 2 != 0

how_many_even = apply(is_even, 10)
print(how_many_even)

how_many_odd = apply(is_odd, 10)
print(how_many_odd)
