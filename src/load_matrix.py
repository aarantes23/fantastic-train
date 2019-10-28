# -*- coding: utf-8 -*-

""" 
    Load a matrix file in the following format:
    u v (lines of the file)
    u v w 
    ...
    $
    u w
    ...

    where:  u = edges
            v = vertices
            w = weights
            $ = Delimiter from where the cost of install begins 

    First line (after the comments) are this 3 params, follow by the graph.
    After the caracter $ are the costs to install a station on that vertex.
    
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
    $
    0 1
    1 3
    2 5
    3 7
    4 5
    5 3
    6 1
    7 3
    8 5

    Developed by: aarantes23@outlook.com
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
    install_cost = list()
    flag = True
    flag_break = True
    f = open(path, "r")  # Associate file to variable.
    data = f.readlines()  # Read all lines of file.
    f.seek(0)  # Set the pointer to the beginning of file.
    for line in data:  # For each line on data.
        line = line.strip() # Remove \n in the end of line 
        # If its not in blak and not a meta.
        if not line.isspace() and not line.startswith('%'):  # Self explanatory
            if flag_break == False:
                install_cost.append([int(z) for z in line.split(" ")])
            if line.startswith("$"):
                flag_break = False
            if flag == False and flag_break == True:  # If the settings var is not empty
                matrix.append([int(x) for x in line.split(" ")])
            if flag == True and flag_break == True:                
                settings = [int(y) for y in line.split(" ")]
                flag = False
    f.close()  # Finally, close the file
    return settings, matrix, install_cost
