#coding:utf-8

# FONCTIONS

"""
fonction(paramètre)

Fonctions natives :
    print() (afficher)
    input() (saisir)
    type() (verifier le type d'une variable)
    int(), float(), str(), bool() (caster)

Fonctions personnalisées :
    def nom_fonction(paramètre):
        instructions

"""

"""

# Fonction sans paramètre

def dire_bonjour():
    print("Bonjour")

# En revenant au début de la ligne, je ne suis plus dans la fonction

dire_bonjour()

###

# Fonction avec paramètres

def dire(nom_personne, message_personne):
    print("{} : {}".format(nom_personne, message_personne))

dire("Toto", "Bonjour")
dire("Tata", "Au revoir")

###

# Fonction avec paramètres par défaut

def dire(nom_personne="Tom", message_personne="Salut", age_personne=18):
    print("{} ({} ans) : {}".format(nom_personne, age_personne, message_personne))

dire(message_personne="Yo !", age_personne=25, nom_personne="Roger")

###


def show_inventory(*list_items):
    for item in list_items:
        print(item)

show_inventory("potion")
show_inventory("potion", "bouclier", "potion", "arc", "cape")

###

def calculer_somme(nb1, nb2):
    resultat = nb1 + nb2
    return resultat

print(calculer_somme(2, 3))

###

def comparer_nombres(nb1, nb2):
    if nb1 > nb2:
        print("Le premier nombre est plus grand")
    elif nb1 < nb2:
        print("Le deuxième est plus grand")
    else:
        print("Les deux nombres sont identiques")

comparer_nombres(5, 5)
comparer_nombres(5, 6)
comparer_nombres(6, 5)

###

"""

def le_plus_grand(nb1, nb2):
    if nb1 > nb2:
        return nb1
    else:
        return nb2

print(le_plus_grand(5, 6))

###