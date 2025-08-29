# def is_even(num):
#     # Specification, Docstring
#     """
#     Input: num -> a positive integer
#     Returns: True if num is even, otherwise False
#     """
#     return num % 2 == 0
# print(is_even(5))
# print(is_even(8))

# Write code that satisfies the following specs
# def div_by(n, d):
#     """ n and d are ints > 0
#         Returns True if d divides n evenly and False Otherwise"""
#     return n % d == 0
 
# # Test the code with:
# # n = 10 and d = 3
# # n = 195 and d = 13
# print(div_by(10, 3))
# print(div_by(195, 13))


# def is_odd(n):
#     return n % 2 != 0
# def sum_odd(a, b)-> int:
#     sum_of_odds = 0
#     for n in range(a, b + 1):
#         if is_odd(n) : sum_of_odds += n
#     return sum_of_odds
# print(sum_odd(2, 7))

def is_palindrome(s) -> bool:
    """
        s is a string
        Returns True if s is palindrome otherwise False
    """
    l = 0
    r = len(s) - 1
    flag = True
    while l <= r:
        if s[l] != s[r]:
            flag = False
            break
        l += 1
        r -= 1
    if flag:
        return True
    return False
print(is_palindrome('222'))
print(is_palindrome('2222'))
print(is_palindrome('abc'))
print(is_palindrome('aba'))