# -*- coding: utf-8 -*-

import graph as _graph

"""
    Iterative Deepening Depth First Search (IDDFS) Algorithm

    IDDFS calls a DFS for different depths starting from the initial value. 
    In every call, DFS can`t go beyond given depth. 
    So basically it`s a DFS in a BFS way.

    Developed by: aarantes23@outlook.com
"""


def scope(g):
    def do_global():
        global result
        result = []
        global graph
        graph = g
    do_global()


def IDDFS(g, src, target, maxDepth):
    """
    Iterative Deepening Depth First (IDDFS) search if target is reachable from v. 
    It uses recursive Depth-Limited Search (DLS).
    
    Keyword arguments:\n
        g (Graph) : graph from the class Graph\n
        src (int) : point in the graph \n
        target (int) : point in the graph\n
        maxDepth (int) : max steps in the graph allowed\n

    Returns:\n
        True or False: If find or not a path with the maxDepth provided

    """
    scope(g)  # Global varibles
    # Do repeatedly the depth-limit search till the maximum depth.
    for i in range(0, maxDepth):
        if (DLS(src, target, i)):
            return (True, result)
    return (False, result)


def DLS(src, target, maxDepth):
    """
    A function to perform a Depth-Limited search
    from given source 'src'

    Keyword arguments:\n
        src (int) : point in the graph \n
        target (int) : point in the graph\n
        maxDepth (int) : max steps in the graph allowed\n

    Returns:\n
        True or False: If find or not a path with the maxDepth provided
    """
    if src == target:
        return True

    # If reached the maximum depth, stop recursing.
    if maxDepth <= 0:
        return False

    # Recur for all the vertices adjacent to this vertex.
    for i in range(0, len(graph._graph[src])):
        if(DLS(graph._graph[src][i][0], target, maxDepth-1)):
            result.append([src, graph._graph[src][i][0],
                           graph._graph[src][i][1]])
            return True
    return False
