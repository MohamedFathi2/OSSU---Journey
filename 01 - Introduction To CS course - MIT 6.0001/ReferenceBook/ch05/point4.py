'''
Finger exercise: Implement a function satisfying the following
specification. Hint: it will be convenient to use lambda in the body of
the implementation.
'''
def f(L1, L2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    # 1 + 8 = 9
    sum = 0
    for curr in map(lambda x, y : x**y, L1, L2):
        sum += curr
        
    # for i in range(len(L1)):
    #     sum += L1[i]**L2[i]
    return sum

print(f([1,2],[2,3])) # prints 9
print(f([3,2],[2,3])) # prints 17


print('My favorite professor–John G.–rocks'.split(' '))
print('My favorite professor–John G.–rocks'.split('-'))
print('My favorite professor–John G.–rocks'.split('–'))