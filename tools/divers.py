### Plein de petit bout de code que je replace ici pour m'en souvenir

#Créer un dictionnaire à partir de deux liste
dict_rotor = dict(zip(index,elem))

a = [3,3,3,4,2,3,3,4]

# index plus petit élément
a.index(min(a))
list(filter(lambda x: x==min(a),a))