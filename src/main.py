# -*- coding: utf-8 -*-

import bfs as bfs
import iddfs as iddfs
from random import *
import os

"""
    Main class to call all the Algorithms.

    Developed by: aarantes23@outlook.com
"""

from graph import Graph
from load_matrix import loadFile
import algorithms as alg

totals_ok = []
totals_error = []
total_files = 0
prints = 0

myFolder = "../input/tests/"
sep = "----- ----- -----"
sep_n = "\n"+sep


def main(path):
    s, m, c = loadFile(path)
    graph = Graph(edges=m, vertexs_qnt=s[0],
                  edges_qnt=s[2], stations_=c, directed=False)

    # Initial test of vertices conections
    if prints:
        print(sep+"Check if exists edges between two vertices: \n")
        print("0->4 : ", graph.exist_edge(0, 4))
        print("1->2 : ", graph.exist_edge(1, 2))

    # MST algorithsm
    if prints:
        print(sep_n+"\n   MST Algorithms"+sep_n)

    # Prim's
    prim_result = alg.prim(graph)
    if prints:
        print("Prim: \nPath: ")
        for u, v, w in prim_result:
            print("      %d - %d = %d" % (u, v, w))
        print("\n Cost: ", sum([item[2] for item in prim_result]))
        print(sep)

    # Kruskal's
    kruskal_result = alg.kruskal(graph)
    if prints:
        print("Kruskal: \nPath:")
        for u, v, w in kruskal_result:
            print("      %d - %d = %d" % (u, v, w))
        print("\n Cost: ", sum([item[2] for item in kruskal_result]))
        print(sep)

    # Check if Prim and Kruskal results are equal
    if prints:
        print("Prim = Kruskal?")
    if sum([item[2] for item in prim_result]) == sum([item[2] for item in kruskal_result]):
        if prints:
            print("      Yes")
        totals_ok[0] += 1
    else:
        if prints:
            print("      No")
        totals_error[0] += 1

    # Recreate the graph obj by
    # Change the mst from list to a Graph obj
    mst = Graph(edges=prim_result, vertexs_qnt=len(kruskal_result)+1,
                edges_qnt=s[2], stations_=c, directed=False)

    # Search Algorithms
    if prints:
        print(sep_n+"\n   Search Algorithms"+sep_n)

    # BFS
    if prints:
        print("      BFS"+sep_n)

    bfs_result = bfs.bfs(mst, 0)
    if bfs_result:  # If works, and the bfs isn't empty
        if prints:
            print("\nFrom MST's root: \n", bfs_result)
        totals_ok[3] += 1
    else:
        if prints:
            print("\n>>>>>> ERROR BSF Fail!")
        totals_error[3] += 1

    if prints:
        print(sep)

    bfs_result = bfs.bfs(graph, 0)
    if bfs_result:  # If works, and the bfs isn't empty
        if prints:
            print("\nFrom Original Graph's root: \n", bfs_result)
        totals_ok[4] += 1
    else:
        if prints:
            print("\n>>>>> ERROR BSF Fail!")
        totals_error[4] += 1

    if prints:
        print(sep)

    # Create the target and src points for the Search Algorithms
    end = len(mst._graph)-1
    src = randint(0, end)
    target = randint(0, end)

    # Ensure that the points aren't equals
    while src == target:   # If they always are, while runs forever
        src = randint(0, end)
        target = randint(0, end)

    # MaxDepth allow for IDDF Search Algoritm
    maxDepth = len(kruskal_result)+1  # math.inf

    # IDDF
    if prints:
        print("      IDDFS"+sep_n)
        print("\nIts possible go from %d to %d with maxDepth %d ?" %
              (src, target, maxDepth))
        print(sep)

    for i in range(2):
        iddfs_result = []
        if i == 0:
            iddfs_boolean, iddfs_result = iddfs.IDDFS(
                mst, src, target, maxDepth)
            iddfs_result.reverse()
            # Save if it works or not
            if iddfs_boolean == True:
                totals_ok[5] += 1
            else:
                totals_error[5] += 1

        if i == 1:
            iddfs_boolean, iddfs_result = iddfs.IDDFS(
                graph, src, target, maxDepth)
            iddfs_result.reverse()
            # Save if it works or not
            if iddfs_boolean == True:
                totals_ok[6] += 1
            else:
                totals_error[6] += 1

        if prints:
            if iddfs_boolean == True:
                print("      Yes")
                print("\nIDDFS path found from %d to %d : " % (src, target))
            else:
                print("      No")
                print(
                    "\n>>>>> ERROR - IDDFS did not find a complete path from %d to %d" % (src, target))
                print("\nPartial path found from %d -> %d" % (src, target))

            for i in range(len(iddfs_result)):
                print(iddfs_result[i][0], end=" -> ")
            if len(iddfs_result) > 1:
                print(iddfs_result[-1][1])

            print("\n Cost: ", sum([item[2] for item in iddfs_result]))
            print("\n Detailed cost: ", iddfs_result)
            print(sep_n)


# Begin
flag = False
while not flag:
    print("\nShow full output prints ? \n0 -> No\n1 -> Yes")
    prints = input()
    try:
        prints = int(prints)
        if prints == True or prints == False:
            flag = True
        else:
            raise ValueError
    except ValueError:
        print("That's not an valid option!")

print(sep)

# Runs for every file in the input folder
for dirname, dirnames, filenames in os.walk(myFolder):
    rel_dir = os.path.relpath(myFolder)  # Use relative path

    event_count = 7  # qnt of positive and negative hits
    totals_ok = [0]*(event_count)
    totals_error = [0]*(event_count)
    total_files = 0

    for filename in filenames:
        path = os.path.join(rel_dir, filename)
        total_files += 1
        print("file: ", filename)
        main(path=path)

# Final results are printed even prints == False
print(sep+" "+sep+"\nFinal results: ")
print("Path folder: ", myFolder)
print(sep)

for i in range(len(totals_ok)):
    if i == 0:
        print("Prim = Kruskal?")
    if i == 1:
        continue  # Not implemented
        print("Did DFS find a path?"+sep_n)
        print("In MST's:")
    if i == 2:
        continue  # Not implemented
        print("In Original Graph's:")
    if i == 3:
        print("Did BFS find a path?"+sep_n)
        print("From MST's root:")
    if i == 4:
        print("From Original Graph's root:")
    if i == 5:
        print("Did IDDFS find a path?"+sep_n)
        print("In MST's:")
    if i == 6:
        print("In Original Graph's:")
    print("\nYes: %d/%d" % (totals_ok[i], total_files))
    print("No: %d/%d" % (totals_error[i], total_files))
    print(sep)
