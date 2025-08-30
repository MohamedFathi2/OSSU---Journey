def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here  
    assert len(L) != 0, "list is empty."
    for item in L:
        if type(item) != str and type(item) != list:
            raise ValueError("Element is not a string or list.")
    total = 0
    for item in L:
        if type(item) == list:
            for e in item:
                if type(e) != str:
                    raise ValueError("Element is not a string.")
                else:
                    total += len(e)
        else: total += len(item)
    return total
# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError
print(sum_str_lengths(["absdab", ["adfd", "afav", "acc"]])) # prints 17
