#coding:utf-8

# CHAÎNES DE CARACTÈRES

"""
Classe str : string

help(str)         : documentation de la classe str

str.upper()                                         : met la chaine en majuscules
str.lower()                                         : met la chaine en minuscules
str.capitalize()                                    : met la première lettre de la chaine en majuscule
str.title()                                         : met chaque mot de la chaine en majuscule
str.center(<largeur>, <caractère de remplissage>)   : centre la chaîne

str.find(<chaîne>, <debut>, <fin>)                  : recherche une chaîne dans la chaine avec un retour "-1" en cas d'absence (<debut> et <fin> sont optionnels, zone de recherche)
str.index(<chaîne>, <debut>, <fin>)                 : recherche une chaine dans la chaine avec un ValueError en cas d'absence
str.replace(<ancienne>, <nouvelle>, <occurences>)   : remplace une chaîne dans la chaine, <occurences> est optionnel et représente le nombre de remplacements à effectuer

str.strip(<caractère>)                              : supprime les espaces en debut et fin de chaine

str.isalpha()                                       : True si la chaîne est composee uniquement de lettres
str.isdigit()                                       : True si la chaîne est composee uniquement de chiffres entiers
str.isdecimal()                                     : True si la chaîne est composee uniquement de chiffres décimaux
str.isnumeric()                                     : True si la chaîne est composee uniquement de nombres
str.isalphanum()                                    : True si la chaîne est composee de lettres et de chiffres

str.isupper()                                      : True si la chaîne est en majuscule
str.islower()                                      : True si la chaîne est en minuscule

str.isidentifier()                                 : True si la chaîne est un identifiant valide/autorisé/non réservé
str.iskeyword()                                    : True si la chaîne est un mot-clé valide

UNE MÉTHODE CHAÎNE TRAVAILLE SUR UNE COPIE, PAS SUR LA CHAÎNE INITIALE

"""

ma_chaine = "bonjour tout le monde"


"""
ma_chaine = ma_chaine.upper()
print(ma_chaine)

ma_chaine = ma_chaine.lower()
print(ma_chaine)

ma_chaine = ma_chaine.capitalize()
print(ma_chaine)

ma_chaine = ma_chaine.title()
print(ma_chaine)

ma_chaine = ma_chaine.center(50, "*")
print(ma_chaine)
###

print(ma_chaine[2]) # affiche le caractère d'index 2 (n)

print(ma_chaine.find("tout")) # affiche l'index de la première occurrence de la chaîne "tout" (8)

###

try:
    print(ma_chaine.index("une"))
except:
    print("la chaîne 'une' n'existe pas")

###
    

ma_chaine = ma_chaine.replace("bonjour", "au revoir")
print(ma_chaine)

"""
###

phrase = "Magicien|50|20"

print(phrase.split("|"))  # ["Magicien", "50", "20"]

###

ch = "Le langage Python"

if "langage" in ch:
    print("Oui")
else:
    print("Non")