'''
Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your code should print out aceg.
'''
my_str = input("Enter a string: ")
even_indexes = ""
for i in range(len(my_str)):
    if i % 2 == 0:
        even_indexes += my_str[i]
# Another Way:
'''
for i in range(0, len(my_str), 2):
    s += my_str[i]
'''
print(even_indexes)
