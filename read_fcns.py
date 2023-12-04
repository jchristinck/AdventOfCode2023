import csv


def read_as_text(filename="input.txt"):
    """ reads csv delimited file using no delimiter, returns list of strings"""
    f = open(filename, "r")
    r = csv.reader(f)
    temp_array = []
    for row in r:
        if row:
            temp_array.append(row[0])
        else:
            temp_array.append("")
    return temp_array


def read_as_lols(filename="input.txt"):
    """ reads csv delimited file using comma as delimiter, returns list (rows) of lists (columns)"""
    f = open(filename, "r")
    r = csv.reader(f, delimiter=',')
    temp_array = []
    for i in r:
        temp_array.append(i)
    return temp_array


def read_as_lols_rep_chars(filename="input.txt", replaced_str=' -> ', new_str=','):
    """ reads file and replaces ' -> ' with ',' in each line, than appends line to list of lists"""
    with open(filename, "r") as f:
        temp_array = f.read().splitlines()  # list of lines containing a string
    for idx in range(len(temp_array)):
        temp_array[idx] = list(map(int, temp_array[idx].replace(replaced_str, new_str).split(new_str)))  # list of [x1, y1, x2, y2]'s
    return temp_array
