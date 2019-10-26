# -*- coding: utf-8 -*-

""" 
    Load a matrix file in the following format:
    u v (lines of the file)
    u v w 

    where:  u = edges
            v = vertices
            w = weights

    First line (after the comments) are this 3 params, follow by the graph.
    
    Exemple:
    % Comments
    14 9 14
    0 1 4
    0 7 8
    1 2 8
    1 7 11
    2 3 7
    2 5 4
    2 8 2
    3 4 9
    3 5 14
    4 5 10
    5 6 2
    6 7 1
    6 8 6
    7 8 7

    # Developed by: aarantes23@outlook.com
"""


def loadFile(path):
    """  
    Join train, valid and test files to create one full file.\n
    Return 2 list splited, one with each attribute from the matrix, such as rows, colums, entries.\n
    The other is the full matrix loaded from the file in path var.

    Keyword arguments:\n
        path (string) : full or relative strings name with file path.\n
    Returns:\n
        settings (list) : List with [rows, colums, entries];
        matrix (list) : Full matrix loaded from the file in path var.
    """
    matrix = list()
    settings = []
    flag = True
    f = open(path, "r")  # Associate file to variable.
    data = f.readlines()  # Read all lines of file.
    f.seek(0)  # Set the pointer to the beginning of file.
    for line in data:  # For each line on data.
        # If its not in blak and not a meta.
        if not line.isspace() and not line.startswith('%'):  # Self explanatory
            if not flag:  # If the settings var is not empty
                matrix.append([int(y) for y in line.split(" ")])
            else:
                settings = [int(y) for y in line.split(" ")]
                flag = False
    f.close()  # Finally, close the file
    return settings, matrix
