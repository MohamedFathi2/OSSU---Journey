
def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    flag = True
    for function in Lf:
        if not function(n): 
            flag = False
            break
    return flag

functions = [lambda x : True if x > 0 else False, lambda x : True if x % 2 == 0 else False]
print(all_true(6, functions))