# def make_ordered_list(n):
#     """n is a positive int
#     Returns a list containing all ints in order
#     from 0 to n (inclusive)
#     """
#     l = []
#     for i in range(n + 1):
#         l.append(i)
#     return l

# print(make_ordered_list(6)) # prints [0, 1, 2, 3, 4, 5, 6]



# # -----------------
# def remove_elem(L : list, e):
#     """
#     L is a list
#     e is an object 
#     Returns a new list with elements in the same order as L
#     but without any elements equal to e.
#     """
#     newList = []
#     for item in L:
#         if item != e:
#             newList.append(item)
#     return newList

# L = [1,2,2,2]
# print(remove_elem(L, 2)) # prints [1]

# # -----------------
# s = "I<3 cs &u?"

# L = list(s) # L is → ['I', '<', '3', ' ', 'c', 's', ' ', '&', 'u', '?']
# L1 = s.split(' ') # L1 is → ['I<3', 'cs', '&u?']
# L2 = s.split('<') # L2 is → ['I', '3 cs &u?'] 
# print(L1, L2)

# def count_words(sen : str):
#     """sen is a string representing a sentence
#     Returns how many words are in s (i.e. a word is a 
#     sequence of characters between spaces.)"""
#     L = sen.split()
#     return len(L)


# print(count_words("Hello it's me!"))

# # -----------------
# def sort_words(sen):
#     """sen is a string representing a sentence
#     Returns a list containing all the words in sen but sorted in 
#     alphabetical order."""
#     L = sen.split()
#     L.sort()
#     return L
# print(sort_words("look at this photograph"))

l = [4,5,6]
print(id(l))
l.append(8)
print(id(l))
l.clear()
print(id(l))

l1 = [4,5,6]
print(id(l1))
l1.append(8)
print(id(l1))
# different, we lose the binding to the original l1 and create a new object with binding l1
l1 = []
print(id(l1)) 