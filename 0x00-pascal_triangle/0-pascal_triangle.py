#!/usr/bin/python3
'''
Create a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n
'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    '''
    lists = []
    if n == 0:
        return lists
    for u in range(n):
        lists.append([])
        lists[u].append(1)
        if (u > 0):
            for j in range(1, u):
                lists[u].append(lists[u - 1][j - 1] + lists[u - 1][j])
            lists[u].append(1)
    return lists
