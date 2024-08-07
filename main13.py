#coding:utf-8

# TUPLES

"""
Peut contenir n'importe quel type d'objets
/!\ Les tuples sont immuables, ils peuvent servir de constantes à moins d'affectations multiples

Création de tuple :

    tuple = () # Vide
    tuple = 17, ou (17,) # Une seule valeur
    tuple = (4, 6) # Plusieurs valeurs

Accès aux valeurs : tuple[X]  # Valeur d'indice X

2 raisons d'utiliser les tuples :
    - affectation multiple de varable
    - retour multiple de fonction
"""

# Exemple
"""
liste = [1, 2, 3, 4, 5, 6]

for chose in enumerate(liste):
    print(chose)

###

# Créer un tuple

mon_tuple = () # Creer un tuple vide avec des parenthèses
print(type(mon_tuple))

mon_tuple = (42,) # Sans virgule c'est un int et non un tuple
print(type(mon_tuple))


# Atteindre des valeurs
mon_tuple = (45, 64)
print(mon_tuple[0])

''' Utiliser try: exept: pour les erreurs '''

###

nombre1 = 14
nombre2 = 46

# OU

(nombre1, nombre2) = (14, 46) # L'affectation multiple permet les modifications, seul le conteneur est immuable

print(nombre1)
print(nombre2)
"""

###

def get_player_position():
    posx = 148
    posy = 86

    return posx, posy
    # return (posx, posy) retourne un tuple

# Programme principal
coordX = 0
coordY = 0

print ("Position du joueur : ({}/{})".format(coordX, coordY))

(coordX, coordY) = get_player_position() 

''' Coordonnées modifiables puisque multiples'''

print("Position du joueur : ({}/{})".format(coordX, coordY))