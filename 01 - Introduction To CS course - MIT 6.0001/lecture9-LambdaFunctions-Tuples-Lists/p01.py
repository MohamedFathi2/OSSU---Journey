def char_counts(s):
    """s is a string of lowercase chars
    Return a tuple where the first element is the number of vowels in s and the second element
    is the number of consonants in s
    """
    #  vowels: a, e, i, o, u
    #  consonants [any other letter]: b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y and z
    vowels = "aeiou"
    countConsonants = 0
    for char in s:
        if char not in vowels:
            countConsonants += 1
    return (len(s) - countConsonants, countConsonants)

# vowels, consonants = char_counts("qwertyuiopasdfghjklzxcvbnm")
# print(vowels, consonants)

# print(char_counts("abcd")) # prints(1,3)
# print(char_counts("zcght")) # prints(0,5)
# print(char_counts(""))
# print(char_counts("aeiou"))

def sum_and_prod(L):
    """L is a list of numbers
    Return a tuple where the first value is the 
    sum of all elements in L and the second value is the
    product of all element in L"""
    sum = 0
    product = 1
    for n in L:
        sum += n
        product *= n
    return (sum, product)

print(sum_and_prod([5,2,10]))