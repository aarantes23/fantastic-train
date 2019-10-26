# -*- coding: utf-8 -*-

"""
    Check if adding a new edge to the tree will generate a looping.

    # Developed by: aarantes23@outlook.com
"""

def union(parent, rank, x, y):
    """ 
    A function that does union of two sets of x and y
    (Union two separete roots)
    """
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def find(parent, i):
    """
    Give a elemente, find the root it belongs
    Uses path compression
    """
    if parent[i] == i:
        return i
    return find(parent, parent[i])
