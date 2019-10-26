# -*- coding: utf-8 -*-

"""
    Main class to call the MST Algorithms.
    
    # Developed by: aarantes23@outlook.com
"""

from graph import Graph
from load_matrix import loadFile
import algorithms as alg

s, m = loadFile("../input/created/m0.txt")
graph = Graph(m, s[1], directed=False)

print("----- ----- -----")

print("Check conections between edges: \n")  # Test
print("0->4 : ", graph.exist_edge(0, 4))
print("1->2 : ", graph.exist_edge(1, 2))

print("\n----- ----- -----")
print("\n   MST Algorithms\n")
print("----- ----- -----")

prim_result = alg.prim(graph)
print("Prim:")
print("\n Path: ")
for u, v, w in prim_result:
    print("      %d - %d = %d" % (u, v, w))
print("\n Cost: ", sum([item[2] for item in prim_result]))

print("----- ----- -----")

kruskal_result = alg.kruskal(graph)
print("Kruskal")
print("\n Path:")
for u, v, w in kruskal_result:
    print("      %d - %d = %d" % (u, v, w))
print("\n Cost: ", sum([item[2] for item in kruskal_result]))
