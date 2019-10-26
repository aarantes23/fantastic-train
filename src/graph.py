# -*- coding: utf-8 -*-

"""
    A Class to represent a graph object.
    
    # Developed by: aarantes23@outlook.com
"""
from collections import defaultdict


class Graph(object):
    """ 
        Graph object. 
    """

    def __init__(self, edges, vertexs_qnt, directed=False):
        self._graph = [[] for _ in range(vertexs_qnt)]
        self._directed = directed
        self.add_edges(edges)
        self.n = len(self._graph)
        # Removes first position of the graph if its empty
        if len(self._graph[0]) == 0:
            del self._graph[0]

    def get_vertexs(self):
        """ Return vertex list from graph. """
        return list(range(len(self._graph)))

    def get_edges(self):
        """ Return edges list from graph """
        return [(k, v, w) for k in range(len(self._graph)) for v, w in self._graph[k]]

    def add_edges(self, edges):
        """ Add edges to graph. """
        for u, v, w in edges:
            self.add(u, v, w)

    def add(self, u, v, w):
        """  Add a conection (edge) between nodes 'u' and 'v'. """
        self._graph[u].append((v, w))
        if not self._directed:
            self._graph[v].append((u, w))

    def exist_edge(self, u, v):
        """ Check if there's a edge between 2 vertex """
        return v in [i for i, w in self._graph[u]] if len(self._graph) > u else -1

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, str(self._graph))
