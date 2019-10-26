# -*- coding: utf-8 -*-

"""
    Minimum Spanning Tree (MST) Algorithms:

    1 - Prim
    2 - Kruskal

    # Developed by: aarantes23@outlook.com
"""

import math
import graph as _graph
import copy
from union_find import *


def prim(graph):
    """
    Construct MST using Prim's algorithm\n
    Return a List with the MST's path.

    Keyword arguments:\n
        graph : Graph obj from the class (import graph).

    Returns:\n
        result (List) : List with the MST's path.   
        #[[u, v, w], [u, v, w], ... until the MST is complete] 
        #Ex: [[0, 1, 4], [1, 2, 8], [2, 8, 2], [2, 5, 4], [5, 6, 2], [6, 7, 1], [2, 3, 7], [3, 4, 9]]

    """
    # Create a list n -1 times
    pai = [-1]*(graph.n)  
    # Current cost of reaching the vertex from the root
    cost = [math.inf]*graph.n
    # Edges that will be part of the tree in the result
    result = []
    u = 0  # root
    L = []

    aux = tuple(range(graph.n))
    for vertex in aux:
        L.append(vertex)

    while not len(L) == 0:
        # Verify that it is not yet on the tree and is currently achieved at the lowest cost.
        u = min(L, key=lambda x: cost[x])
        L.remove(u)
        index = -1

        # Update cost`s values
        for v, w in graph._graph[u]:
            if w < cost[v]:
                cost[v] = w
                pai[v] = u

        if not pai[u] == -1:  # "Removes root" from the result and add to the result
            result.append([pai[u], u, cost[u]])

    return(result)


def kruskal(graph):
    """       
    Construct MST using Kruskal's algorithm\n
    Return a List with the MST's path.

    Keyword arguments:\n
        graph : Graph obj from the class (import graph).

    Returns:\n
        result (List) : List with the MST's path.   
        #[[u, v, w], [u, v, w], ... until the MST is complete] 
        #Ex: [[6, 7, 1], [2, 8, 2], [5, 6, 2], [0, 1, 4], [2, 5, 4], [2, 3, 7], [0, 7, 8], [3, 4, 9]]

    """
    result = []  # This will store the resultant MST
    graphs_list = []  # Changed graph obj to a list :/
    i = 0

    # Step 0: Change the graph to a list to do the step 1
    while i < (graph.n):
        for v, w in graph._graph[i]:
            graphs_list.append([i, v, w])
        i = i + 1

    # Step 1:  Sort all the edges in non-decreasing
    # order of their weight.
    graphs_list = sorted(graphs_list, key=lambda item: item[2])

    parent = []
    rank = []

    # Create V subsets with single elements
    for node in range(graph.n):
        parent.append(node)
        rank.append(0)

    i = 0  # Index
    e = 0  # Index
    while e < ((graph.n)-1):
        # Step 2: Gets the vertex with less weight and increment
        # the index for next iteration
        u, v, w = graphs_list[i]
        i = i+1
        # Check parents
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does't cause cycle,
        # include it in result and increment the index
        # of result for next edge
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
        # Else discard the edge

    return(result)
