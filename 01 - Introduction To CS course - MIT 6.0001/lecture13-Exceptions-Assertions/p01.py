# def sum_digits(s):
#     """s is a non empty string containing digits
#     Returns sum of all chars that are digits
#     """
#     total = 0
#     for n in list(s):
#         try:
#             val = int(n)
#             total += val
#         except:
#             print("can't convert:", n)
#     return total

# print(sum_digits('123'))
# print(sum_digits('123abc'))


# def divide_number1():
#     a = int(input("Enter a number:"))
#     b = int(input("Enter another number:"))
#     print(a/b)
    
# def divide_number2():
#     try:
#         a = int(input("Enter a number:"))
#         b = int(input("Enter another number:"))
#         print(a/b)
#     except:
#         print("Bug in user input")
# divide_number1()
# divide_number2()


# def divide_number3():
#     try:
#         a = int(input("Enter a number:"))
#         b = int(input("Enter another number:"))
#         print("a / b =",a/b)
#         print("a + b =",a+b)
#     except ValueError:
#         print("Couldn't convert to a number.")
#     except ZeroDivisionError:
#         print("Can't divide by zero")
#         print("a / b = infinity")
#         print("a + b =", a)
#     except:
#         print("Something went very wrong.")
        
# divide_number3()


# def sum_digits_raise(s):
#     """s is a non-empty string containing digits
#     Returns sum of all characters that are digits"""
#     total = 0
#     for char in s:
#         try:
#             total += int(char)
#         except:
#             raise ValueError("string contained a character.")            
#     return total

# print(sum_digits_raise("123abc"))


# def pairwise_div(Lnum, Ldenom):
#     """Lnum and Ldenomn are non-empty lists of equal lengths containing numbers
    
#     Returns a new list whose elements are the pairwise
#     division of an element in Lnum by an element in Ldenom.
    
#     Raise a ValueError if Ldenom contains 0.
#     """
#     toReturn = []
#     for i in range(len(Lnum)):
#         try:
#             val = Lnum[i] / Ldenom[i]
#             toReturn.append(val)
#         except:
#             raise ValueError("Can't divide by 0.")
#     return toReturn

# L1 = [4,5,6]
# L2 = [1,2,3]
# print(pairwise_div(L1, L2)) # prints [4.0, 2.5, 2.0]

# L1 = [4,5,6]
# L2 = [1, 0, 3]
# print(pairwise_div(L1, L2)) # raises a ValueError



# def sum_digits(s):
#     """s is a non empty string containing digits.
#     Returns sum of all chars that are digits
#     """
#     assert len(s) != 0, "s is empty."
#     total = 0
#     for n in list(s):
#         try:
#             val = int(n)
#             total += val
#         except:
#             raise ValueError("string contained a character.")
#     return total

# # print(sum_digits(""))
# print(sum_digits("123"))
# print(sum_digits("123abc"))



# def pairwise_div(Lnum, Ldenom):
#     """Lnum and Ldenomn are non-empty lists of equal lengths 
#         containing numbers
    
#     Returns a new list whose elements are the pairwise
#     division of an element in Lnum by an element in Ldenom.
#     Raise a ValueError if Ldenom contains 0.
#     """
#     assert len(Lnum) == len(Ldenom), "lengths are different."
#     assert len(Lnum) != 0 and len(Ldenom) != 0, "Empty lists."
#     toReturn = []
#     for i in range(len(Lnum)):
#         try:
#             val = Lnum[i] / Ldenom[i]
#             toReturn.append(val)
#         except:
#             raise ValueError("Can't divide by 0.")
#     return toReturn

# L1 = [4,5,6]
# L2 = [1,2,3]
# print(pairwise_div(L1, L2)) # prints [4.0, 2.5, 2.0]

# L1 = [4,5,6]
# L2 = [1, 0, 3]
# # print(pairwise_div(L1, L2)) # raises a ValueError


# L1 = []
# L2 = []
# print(pairwise_div(L1, L2)) # raises a AssertionError
