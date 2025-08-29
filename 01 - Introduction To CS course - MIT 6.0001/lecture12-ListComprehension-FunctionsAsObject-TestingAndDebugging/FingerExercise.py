def count_sqrts(nums_list : list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here
    nums_list.sort()
    count = 0
    # using list comprehension: 
    '''
    for curr in nums_list:
        if [True for item in nums_list if curr**2 == item]:
            count += 1
    return count
    '''
    # Simple Solution:    
    for item in nums_list:
        if item**2 in nums_list:
            count += 1
    return count


# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3