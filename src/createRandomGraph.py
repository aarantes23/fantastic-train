# -*- coding: utf-8 -*-

from random import *

"""
    Creates n random graphs in the outputPath

    Developed by: aarantes23@outlook.com
"""

outputPath = "../input/random/"  # Output path


def main(filename):
    x = 1  # Random Start point
    y = 100  # Random End point
    m = int(y * 0.80)  # Max recharge install cost for vertice
    u = 50
    edges = 300
    edges_ = edges  # Backup for check after

    result = []  # Partial result
    cost_install = []  # Partial result
    temp_result = []
    v_ = 0  # Index
    i = 0  # Index

    # Create a list with installation cost for each vertice
    for i in range(u):
        aux = ([i, randint(x+1, m)])  # Can't do randint() in append
        cost_install.append(aux)

    # Ensures that there is a complete path in the graph
    for i in range(u-1):
        v_ += 1
        aux = ([i, v_, randint(x, y)])  # Can't do randint() in append
        result.append(aux)
        edges -= 1

    # Add the rest of edges
    for i in range(edges):
        flag = True
        while flag == True:
            aux = ([randint(x, u-1), randint(x, u-1), randint(x, y)])
            aux_inv = (aux[1], aux[0], aux[2])
            temp = (aux[0], aux[1])
            temp_inv = (aux[1], aux[0])

            if (temp not in temp_result) and (temp_inv not in temp_result) and (temp[0] != temp[1]):
                temp_result.append(temp)
                # Ensures that won't be a edge repeated
                if (aux not in result) and (aux_inv not in result) and (aux[0] != aux[1]):
                    result.append(aux)
                    flag = False

    # Save results in a file
    file_ = open(filename, "w")  # Associate file to variable.
    file_.seek(0)

    # Write first line (u,v,lines)
    file_.write(str(u) + " " + str(edges) + " " + str(len(result)) + " \n")
    # Write the Graph (u,v,w)
    for v in result:
        file_.write(str(v).replace("[", "").replace("]", "").replace(
            "'", "").replace(" ", "").replace(",", " ")+"\n")
    # Write a delimiter
    file_.write("$\n")
    # Write the cost of install (v,w)
    for v in cost_install:
        file_.write(str(v).replace("[", "").replace("]", "").replace(
            "'", "").replace(" ", "").replace(",", " ")+"\n")

    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file


# Begin
flag = False
while not flag:
    print("\nHow much graphs should be generate? ")
    n = input()
    try:
        n = int(n)
        flag = True
    except ValueError:
        print("That's not an valid number!")

for i in range(n):
    filename = outputPath + "r" + str(i) + ".txt"
    main(filename=filename)

print("%d graphs created in the folder %s" % (n, outputPath))
