
# Un exemple de graphe

noeuds = [0,1,2,3,4,5]
aretes = [(1,2),(3,4),(1,4),(4,5),(0,3),(0,4),(0,2),(2,3)]
weights = [4,5,6,4,3,7,6,1]

def degré(j0, aretes):
    """Degré d'un noeuds j_0"""
    ct = 0
    for ar in aretes:
        if ar[0] == j0 or ar[1] == j0:
            ct += 1
    return ct


def comp_conn(j0, aretes):
    """Composante connexe associées à j0"""
    curr = {j0}
    ct = 1
    new = 0
    while new != ct:
        ct = len(curr)
        for ar in aretes:
            if ar[0] in curr:
                curr.add(ar[1])
            if ar[1] in curr:
                curr.add(ar[0])
        new = len(curr)
    return curr


print(comp_conn(0, aretes))


def sort_aretes(aretes, weight):
    """Tri des aretes par ordre croissant"""
    ar_cp = aretes.copy()
    wh_cp = weight.copy()

    new_aretes = []
    new_weight = []
    for i in range(len(weight)):
        ind_min = wh_cp.index(min(wh_cp))
        new_weight.append(wh_cp.pop(ind_min))
        new_aretes.append(ar_cp.pop(ind_min))
    return new_aretes, new_weight


def kruskal(arete, weight):
    """Algorithme de Kruskal pour l'arbre couvrant minimum"""
    arete_cp, weight_cp = sort_aretes(arete, weight)

    cur_tr = []
    cur_wh = 0
    for i, ar in enumerate(arete_cp):
        if comp_conn(ar[0], cur_tr) != comp_conn(ar[1], cur_tr):
            cur_tr.append(ar)
            cur_wh += weight_cp[i]
    return cur_tr, cur_wh

# Importation par liste de voisin

import sys

sys.setrecursionlimit(1000000000)
n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u] += [v]
    g[v] += [u]
