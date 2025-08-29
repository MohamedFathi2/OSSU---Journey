# def remove_all(L : list, e):
#     """
#     L is a list
#     Mutates L to remove all elements in L that are equal to e
#     Returns None
#     """
#     # Hint: Make a copy to save the elements Then use L.clear() to empty out the list
#     # and repopulate it with the ones you're keeping.
    
#     # Making a copy.
#     newL = L[:]
    
#     # Emptying original list.
#     L.clear()
    
#     # Repopulating original list with the elements that are not equal to e.
#     for item in newL:
#         if item != e:
#             L.append(item)


# Another Implementation:


def remove_all(L : list, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Return
    """
    while e in L:
        L.remove(e)
L = [1,2,2,2]
remove_all(L,2)
print(L)
