""" 
----------------------------------------
Binary Search Algorithm 
----------------------------------------
The name is evident enough to give an overview of the project. 
The program requires you to create a list of numbers between 0 
to whatever range you prefer, with every succeeding number having 
a difference of 2 between them. 

When the user inputs a random number to be searched the program b
egins its search by dividing the list into two halves. The first 
half is searched for the required number and if found, the other half 
is rejected and vice versa. The search continues until the number is 
found or the subarray size becomes zero. This Python project idea could 
also help you write a program to search an element in the list. 
----------------------------------------
"""

# iterative implementation of binary search in Python
def binary_search(a_list, item):
    a_list = 'path/to/file/or/array'
    """
    Performs iterative binary search to find the position of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        i = (first + last) / 2
        if a_list[i] == item:
            return ' found at position '.format(item=item, i=i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            return ' not found in the list'.format(item=item)

# recursive implementation of binary search in Python
def binary_search_recursive(a_list, item):
    """
    Performs recursive binary search of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """
    first = 0
    last = len(a_list) - 1
    if len(a_list) == 0:
        return ' was not found in the list'.format(item=item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return ' found'.format(item=item)
        else:
            if a_list[i] < item:
                return binary_search_recursive(a_list[i+1:], item)
            else:
                return binary_search_recursive(a_list[:i], item)