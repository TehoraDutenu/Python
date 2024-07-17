#coding:utf-8

""" 
Opérateurs de comparaison :
    == (egal)
    != (different)
    > (superieur)
    < (inferieur)
    >= (superieur ou egal)
    <= (inferieur ou egal)

Conditions multiples :
    and (et)
    or (ou)
    in (dans)
    not in (pas dans)
    not (non)

Conditions :
    if (si)
    elif (sinon si)
    else (sinon)

"""

"""
calcul = 5 / 2
calcul = int(calcul)
calcul2 = 5 % 2
calcul2 = int(calcul2)

print("Resultat :", calcul)
print("Resultat :", calcul2)

calcul3 = 5 + 3 * 7 # fonctionne comme en maths avec priorité de certaines opérations

identifiant = "Tehora"
mot_de_passe = "password1234"

print("Interface de connexion")

user_id = input("Entrez votre identifiant : ")
user_password = input("Entrez votre mot de passe : ")

if user_password == mot_de_passe and user_id == identifiant: # SI
    print("Vous êtes connecté, bienvenue", user_id)
elif user_password == mot_de_passe and user_id != identifiant: # SINON
    print("Identifiant incorrect")
elif user_password != mot_de_passe and user_id == identifiant:
    print("Mot de passe incorrect")
else:
    print("Identifiant et mot de passe incorrect")

###

ident = "Teho"
mdp = "Zac123"

user_id1 = input("Entrez votre identifiant : ")
user_password1 = input("Entrez votre mot de passe : ")

if user_id1 == ident and user_password1 == mdp:
    print("Vous êtes connecté, bienvenue", user_id1)
else:
    print("Identifiant ou mot de passe incorrect")

###


lettre_hasard = "a"

if lettre_hasard in "aeiouy":
    print("C'est une voyelle")
else:
    print("C'est une consonne")

###

jeu_charge = True # True = vrai (= 1), False = faux (= 0)

if not jeu_charge:
    print("Jeu non chargé")
else:
    print("Jeu chargé")

###

age = input("Quel âge as-tu ? ")
age = int(age)

if age > 0 and age <= 100:
    print("L'âge est validé")
else:
    print("L'âge est invalide")

###

"""
age = input("Quel âge as-tu ? ")
age = int(age)

if 0 < age <= 100:
    print("L'âge est validé")
else:
    print("L'âge est invalide")
