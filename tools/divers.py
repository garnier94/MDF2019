### Plein de petit bout de code que je replace ici pour m'en souvenir

#Créer un dictionnaire à partir de deux liste
dict_rotor = dict(zip(index,elem))

a = [3,3,3,4,2,3,3,4]

# index plus petit élément
a.index(min(a))
list(filter(lambda x: x==min(a),a))

def calculate_median(l):
    """Médiane d'une liste"""
    l = sorted(l)
    l_len = len(l)
    if l_len < 1:
        return None
    if l_len % 2 == 0 :
        return ( l[(l_len-1)//2] + l[(l_len+1)//2] ) / 2.0
    else:
        return l[(l_len-1)//2]


#Fonction utiles :

#Arrondi supérieur
from math import ceil

#Copie récursive
from copy import deepcopy