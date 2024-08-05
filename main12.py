#coding:utf-8

# LISTES

"""
help(list)                      : afficher l'aide à propos de la classe list

liste[X]                         : afficher l'élément d'indice X
liste[-X]                        : afficher le Xème élément en partant de la fin

liste[:]                         : afficher tout
liste[:X]                        : afficher les X premiers éléments
liste[X:]                        : afficher sauf les X premiers éléments

liste[A:B]                       : afficher entre l'index A et l'index B (exclus)

len(liste)                       : longueur de la liste (nombre d'éléments)

Méthodes : 
    liste.append(X)              : ajouter un élément à la fin
    liste.insert(index, X)       : ajouter un élément à l'index X

"""

# Création d'une liste

"""
inventaire = list() # ou inventaire = []

###

inventaire = [0] * 10

###

inventaire = ["arc"] * 10

###

inventaire = range(20)
i = 0

while i < len(inventaire):
    print(inventaire[i])

    i += 1

###

print(inventaire)

###

inventaire = range(20)

for valeur in inventaire:
    print(valeur)

###

inventaire = ["Arc", "Épée", "Bouclier"]  # Arc : indice 0, premier élément
for valeur in inventaire:
    print(valeur)
###
    
# Rechercher certains éléments

inventaire = ["Arc", "Épée", "Bouclier"]  
print(inventaire[1]) # indice 1, deuxième élément
###

inventaire = ["Arc", "Épée", "Bouclier"]
print(inventaire[:]) # Tout


###

inventaire = ["Arc", "Épée", "Bouclier"]  
print(inventaire[:2]) # Afficher les deux premiers

###

inventaire = ["Arc", "Épée", "Bouclier", "Potion", "Flêches", "Tunique"]  
print(inventaire[3:]) # Afficher après les trois premiers

###

inventaire = ["Arc", "Épée", "Bouclier", "Potion", "Flêches", "Tunique"]  
print(inventaire[-3]) # Afficher l'index 3 à partir de la fin != [3] est l'index 3

###

inventaire = ["Arc", "Épée", "Bouclier", "Potion", "Flêches", "Tunique"]  
print(inventaire[2:5]) # Afficher entre l'index 2 et l'index 5

###

# Modification d'une liste

inventaire = ["Arc", "Épée", "Bouclier", "Potion", "Flêches", "Tunique"]
print(inventaire[:])

inventaire[2] = "Hache" # Remplace Bouclier par Hache à l'index 2
print(inventaire[:])

###

inventaire = ["Arc", "Épée", "Bouclier", "Potion", "Flêches", "Tunique"]
print(inventaire[:])

inventaire[:2] = ["Hache"] * 2 # Remplace les deux premiers éléments par deux Haches
print(inventaire[:])

###

# Vérifier si un élément existe dans la liste

inventaire = ["Arc", "Épée", "Bouclier", "Potion", "Flêches", "Tunique"]

if "Potion" in inventaire:
    print("Oui")
else:
    print("Non")

###

## Méthodes

# Ajouter un élément à la liste
inventaire = []
print(inventaire[:])

inventaire.append("Arc") # Ajouter un élément à la liste
print(inventaire[:])


###

# Insérer un élément à la liste sur un index déterminé
inventaire = ["Arc", "Bouclier", "Potion"]
print(inventaire[:])

inventaire.insert(2, "Épée") # Ajouter à l'index 2, décale "Potion"
print(inventaire[:])

###

# Enlever un élément à partir de la valeur de l'élément
inventaire = ["Arc", "Bouclier", "Potion"]
print(inventaire[:])

inventaire.remove("Potion") # Enlever la valeur "Potion"
print(inventaire[:])

###

# Enlever un élément à partir de l'index
inventaire = ["Arc", "Bouclier", "Potion"]
print(inventaire[:])

del inventaire[1] 
print(inventaire[:])

###

# Afficher l'index de la valeur "Potion"
inventaire = ["Arc", "Bouclier", "Potion"]
print(inventaire[:])

print("Indice :", inventaire.index("Potion")) 

# OU
inventaire = ["Arc", "Bouclier", "Potion"]
print(inventaire[:])

objet_a_supprimer = inventaire.index("Bouclier")
del inventaire[objet_a_supprimer]
print(inventaire[:]) 

###


# Trier la liste par ordre alphabétique 
inventaire = ["Arc", "Épée", "Bouclier", "Potion", "Flêches", "Tunique"]
print(inventaire[:])

inventaire.sort()
print(inventaire[:])

###

# Trier la liste par ordre croissant
inventaire = [23, 1, 73, 8, 49]
inventaire.sort()
print(inventaire[:])

###

# Trier la liste par ordre decroissant
inventaire = [23, 1, 73, 8, 49]

inventaire.sort()
print(inventaire[:])

inventaire.reverse()
print(inventaire[:])

###

# Compter le nombre d'éléments
inventaire = ["Arc", "Épée", "Potion", "Bouclier", "Potion", "Flêches", "Potion", "Tunique"]

print("Nombre de potions :", inventaire.count("Potion"))

###

# Supprimer tous les éléments d'une liste
inventaire = ["Arc", "Épée", "Potion", "Bouclier", "Potion", "Flêches", "Potion", "Tunique"]
print(inventaire[:])

inventaire.clear()
print(inventaire[:])

# OU
inventaire = ["Arc", "Épée", "Potion", "Bouclier", "Potion", "Flêches", "Potion", "Tunique"]
print(inventaire[:])

inventaire[:] = []
print(inventaire[:])

###

# Séparer une liste en passant en argument le point de séparation (ici un espace)
chaine = "Bonjour a tous"
print(chaine[:])

chaine = chaine.split(" ")
print(chaine)

###


# Faire une chaîne à partir d'une liste
inventaire = ["Arc", "Épée", "Potion", "Bouclier", "Flêches", "Tunique"]

phrase = "-".join(inventaire)
print(phrase)

###

# On ne travaille pas sur une copie quand on travaille avec une liste, si on modifie le clone on modifie également la liste initiale
liste1 = ["Arc", "Épée", "Potion"]
liste2 = liste1

print("Liste 1 :", liste1[:])
print("Liste 2 :", liste2[:]) 

liste2.append("Couteau")

print("Liste 1 :", liste1[:])
print("Liste 2 :", liste2[:]) 

# ALORS
liste1 = ["Arc", "Épée", "Potion"]
# liste2 = liste1
liste2 = list(liste1)

print("Liste 1 :", liste1[:])
print("Liste 2 :", liste2[:]) 

liste2.append("Couteau")

print("Liste 1 :", liste1[:])
print("Liste 2 :", liste2[:]) 

###

# Concaténation de deux listes
liste1 = ["Arc", "Épée", "Potion"]
liste2 = ["Couteau", "Tunique"]

liste3 = liste1 + liste2 # OU liste1 =+ liste2
print(liste3)

# OU

liste1 = ["Arc", "Épée", "Potion"]
liste2 = ["Couteau", "Tunique"]

liste1.extend(liste2)
print(liste1)

###

# Parcourir une liste et en afficher la valeur et l'index des éléments
inventaire = ["Arc", "Épée", "Potion", "Bouclier", "Flêches", "Tunique"]
for objet in inventaire:
    print(objet)
    
for objet in enumerate(inventaire):
    print(objet)

"""
# ET 
inventaire = ["Arc", "Épée", "Potion", "Bouclier", "Flêches", "Tunique"]
for index_objet, valeur_objet in enumerate(inventaire):
    print("Element d'indice {} -> {}".format(index_objet, valeur_objet))








