#coding:utf-8

# BOUCLES

"""
Boucles :
    while (tant que)
    for (pour)
    else (sinon)
    elif (sinon si)

Mots-clés :
    break (casser la boucle)
    continue (revenir au début de la boucle)
"""


"""
compteur = 0

while compteur < 5:
    print("Je suis une phrase")
    compteur += 1

print("Fin de la boucle")

###

jeu_lance = True
print("")

while jeu_lance:
    choix_menu = input("> ")

    if choix_menu == "again":
        continue
    elif choix_menu == "stop":
        jeu_lance = False
    elif choix_menu == "hello":
        print("Coucou !")
    else:
        print("Choix invalide")

print("Fin du jeu")

###

phrase = "Bonjour tout le monde :) !"

for lettre in phrase: # phrase est une séquence de lettres, lettre en étant un élément. Inventaire de la séquence
    print(lettre)

print("Fin de la boucle")

###
"""

list_news = get_new() # get_new() est une fonction qui renvoie une liste

for news in list_news:
    print(news)

print("Fin de la boucle")