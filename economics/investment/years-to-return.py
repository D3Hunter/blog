#!/usr/bin/env python
import math


def get_number_of_years(growth, pe):
    return math.log(growth * pe + 1) / math.log(1 + growth)

GROWTH_MAX = 100
PE_MAX = 14
matrix = []
for i in range(GROWTH_MAX):
    matrix.append([])
    growth = (i + 1) / 100.0
    for j in range(PE_MAX):
        pe = (j + 1) * 5
        matrix[i].append(get_number_of_years(growth, pe))

str = "PE/Growth "
for i in range(PE_MAX):
    pe = (i + 1) * 5
    str += "%6d" % (pe, )
print str
for i in range(GROWTH_MAX):
    str = "%9d%%" % (i + 1,)
    for j in range(PE_MAX):
        str += "%6.2f" % (matrix[i][j],)
    print str