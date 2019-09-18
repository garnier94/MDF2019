"""Manipulation de table Python"""


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


def neighbor_diag(tab, i, j):
    # Index Voisin en diagonale
    n = len(tab)
    m = len(tab[0])

    l = []
    for k in {-1, 1}:
        for il in {-1, 0, 1}:
            if (i + k) % n == i + k and (j + il) % m == j + il:
                l += [(i + k, j + il)]

        if (j + k) % m == j + k:
            l += [(i, j + k)]

    return l

def index_elem(tab, value):
    "Ensemble des index de la table tab de valeur value "
    p = list()
    n = len(tab)
    m = len(tab[0])

    for i in range(m):
        for j in range(n):
            if tab[i][j] == value:
                p.append((i,j))
    return p