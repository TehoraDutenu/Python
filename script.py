#coding:utf-8

# Commentaire


""" 
Commentaire sur
plusieurs lignes 
"""

#################################

""" PRINT """

print("Coucou")
print("Comment va ?")

print("L'envers\ndu décor") # Mise à la ligne
print("L'envers \t du décor") # Tabulation

print("\n")


#################################

""" VARIABLES """

""" 
Nommer une variable :
        doit commencer par une lettre ou underscore
        ne pas contenir de caractères spéciaux
        ne pas contenir d'espaces
        utilise les underscores et le Camel Case (_)

        agePersonne
        age_personne
        agepersonne
        AgePersonne
        Age_Personne
        _age_personne
        age_personne

Types standards :
        entier numérique (int)
        nombre flottant (float)
        chaîne de caractères (str)
        booléen (bool)
        autres (listes, dictionnaires, tuples, etc...)

        agePersone = 14 --> INT
        agePersonne = "25" --> STR

Fonctions vues :
        print()         --> afficher à l'écran
        input()         --> lire au clavier
        type()          --> retourne le tyoe d'une donnée, variable etc...
        str.format()    --> formater une chaîne
        int(), float(), str(), bool() --> 'caster' une donnée, la convertir
"""

agePersonne = 14
prixHT = 120.46
agePersonne2 = "25" 
continuer_partie = True

print(type(agePersonne))
print(type(prixHT))
print(type(agePersonne2))
print(type(continuer_partie))

###

print("Âge de la personne : ", agePersonne)

###

texte = "L'âge de la personne est {} ans et le prix HT est {}€."
print(texte.format(agePersonne, prixHT))

###

print("L'âge de la personne est {} ans et le prix HT est {}€.".format(agePersonne, prixHT))

###

nomJoueur = input("Choisissez un nom de joueur : ")
print("Bienvenue,", nomJoueur)

###

prixHT2 = input("Entrez un prix HT : ")

# input() ne lit que des strings, donc :
prixHT2 = int(prixHT2) # caster pour que le calcul puisse se faire entre numériques

prixTTC = prixHT2 + (prixHT2 * 20 / 100)
print("Prix TTC :", prixTTC, "€")

###

valeur_booleen = True
valeur_booleen = int(valeur_booleen) # si str, false ou true en toutes lettres (int ou str ils ne seront plus booléens)
print(valeur_booleen)