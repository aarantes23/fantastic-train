# -*- coding: utf-8 -*-

import collections

"""
    Breadth first search algorithm:

    Developed by: aarantes23@outlook.com
"""


def bfs(graph, root):
    """
    A standard BFS implementation puts each vertex of the graph into one of two categories:

    1 - Visited
    2 - Not Visited
    The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

    The algorithm works as follows:

    1 - Start by putting any one of the graph's vertices at the back of a queue.
    2 - Take the front item of the queue and add it to the visited list.
    3 - Create a list of that vertex's adjacent nodes. 
        Add the ones which aren't in the visited list to the back of the queue.
    4 - Keep repeating steps 2 and 3 until the queue is empty.

    The graph might have two different disconnected parts so to make sure that we cover every vertex,
    we can also run the BFS algorithm on every node

    Keyword arguments:\n
        graph : Graph obj from the class (import graph).
        root: [start point] Point in the graph to set where to start

    Returns:\n
        result (List) : List with the finded path.   
        #[[u, v, w], [u, v, w], ... until is complete] 
        #Ex: [[0, 1, 4], [1, 2, 8], [2, 8, 2], [8, 5, 4], [5, 6, 2], [6, 7, 1]]

    """
    # The code is self explanatory with initial comment
    result = []
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbour in graph._graph[vertex]:
            if neighbour[0] not in visited:
                visited.add(neighbour[0])
                queue.append(neighbour[0])

    return(result)
