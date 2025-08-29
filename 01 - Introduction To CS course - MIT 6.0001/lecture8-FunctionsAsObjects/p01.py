def is_even_with_return(i):
    """
    Input: i, a positive int
    Returns True Or False
    """
    remainder = i % 2
    print("With return")
    return remainder == 0

def is_even_without_return(i):
    """
    Input: i, a positive int
    Returns None
    """
    remainder = i % 2
    print("Without return")

# is_even_with_return(3)# False
# print(is_even_with_return(3)) # print(False)

is_even_without_return(3)
print(is_even_without_return(3)) # print(None) 