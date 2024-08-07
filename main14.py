#coding:utf-8

# DICTIONNAIRES

"""
Dictionnaire : tableau associatif qui accepte tout type d'objets

Documentation : help(dict)

Création d'un dictionnaire : dico = {} # Vide
                             dico = {<cle>:<valeur>, <cle2>:<valeur>}
                             
''' LES CLÉS DOIVENT ÊTRE UNIQUES '''

Accès aux valeurs : dico[<cle>]

Ajout et modification : dico[<cle>] = <valeur>

Suppression : dico.pop[<cle>] ou del dico[<cle>]

Vérifier l'existence d'une clé : print(<cle> in dico)

Parcourir : for <cle> in dico OU for <cle, valeur> in dico.items() -> clés et leurs valeurs
            for <cle> in dico.keys() -> seulement les clés
            for <valeur> in dico.values() -> seulement les valeurs
            
Copier le dictionnaire : dico2 = dico.copy()
            
Erreur typique : KeyError

"""

"""
# Création d'un dictionnaire / Récupération d'une valeur
dico = {}
dico1 = {1:145, "prenom":"Agnes"}

print(dico1["prenom"])
print(dico1[1])

''' On appelle toujours la clé '''

# Ajout et modification 

dico = {}

dico[1] = 145
dico["nom"] = "Doe"

print(dico)
print(dico[1])
print(dico["nom"])


# Suppression

dico = {"Chat":"Gribouille", "Chien":"Zacou"}

print(dico)

dico.pop("Chien") # On peut placer la suppression dans une variable pour en conserver la valeur : supp = dico.pop("Chien")

print(dico)

# Rechercher si une clé existe
dico = {"Chat":"Gribouille", "Chien":"Zacou"}

print("Chien" in dico) #Booleen
print("Vache" in dico) 


# Parcourir

## Retrouner tout
dico = {"Chat":"Gribouille", "Chien":"Zacou"}

for cle in dico:
    print(cle, dico[cle])
    
# OU

for cle, valeur in dico.items():
    print("Clé : {} - Valeur : {}".format(cle, valeur))

## Retourner seulement les clés
for cle in dico.keys():
    print(cle)

## Retourner seulement les valeurs
for valeur in dico.values():
    print(valeur)
    
"""

# Paramètres nommés dans les fonctions

def maFonctionBizarre(**parametres): # ** = paramètres nommés obligatoirement, * = paramètres variables
    print(parametres)
    
maFonctionBizarre(prenom="Agnes", nom="Doe")











