import datetime
import debug
import sys
from math import sqrt,ceil
from copy import deepcopy

def dist(tup_1, tup_2):
    return sqrt((tup_1[0]-tup_2[0])**2 + (tup_1[1]-tup_2[1])**2)


def neighbor_tab(tab, i, j):
    # Index Voisin en croix
    n = len(tab)
    m = len(tab[0])

    l = []
    for k in {-1, 1}:
        if (i + k) % n == i + k:
            l += [(i + k, j)]

        if (j + k) % m == j + k:
            l += [(i, j + k)]
    return l


def identifie(tab):
    new_table = deepcopy(tab)
    n = len(tab)
    for i in range(n):
        for j in range(n):
            if tab[i][j] == '#':
                for tup in neighbor_tab(new_table,i,j):

                    if tab[tup[0]][tup[1]] in {'1','2'}:
                        new_table[i][j] =  tab[tup[0]][tup[1]]
    return new_table


def elem_tab(tab, elem):
    "Ensemble des index des élement elem dans tab"
    p = list()
    n = len(tab)
    for i in range(n):
        for j in range(n):
            if tab[i][j] == elem:
                p.append((i,j))
    return p

def main():

    # Lecture de Table
    N = int(input())
    table = list()
    for i in range(N):
        table.append(list(input()))

    table[0][N-1] = '1'
    table[N-1][0] = '2'

    while True :
        new_tab = identifie(table)
        if all([new_tab[i] == table[i] for i in range(N)]):
            break
        table = new_tab

    tab1 = elem_tab(table, '1')
    tab2 = elem_tab(table, '2')
    print(ceil(min([min([dist(te, ta) for te in tab1]) for ta in tab2])))
