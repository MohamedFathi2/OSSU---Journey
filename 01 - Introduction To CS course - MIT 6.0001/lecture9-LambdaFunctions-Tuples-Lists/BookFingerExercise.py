"""Write a lambda expression that has two numeric
parameters. If the second argument equals zero, it should return
None. Otherwise it should return the value of dividing the first
argument by the second argument."""
n1 = 5.0
n2 = 5
test = lambda x1,x2 : None if x2 == 0 else x1/x2
print(test(n1, n2))
# Another neet way to use lambda functions
print((lambda x1, x2: None if x2 == 0 else x1/x2)(5.0,0))
# (5.0, 0) are the inputs x1 and x2