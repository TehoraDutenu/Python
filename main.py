#coding:utf-8

"""
Opérateurs en python :
    + (addition)
    - (soustraction)*
    * (multiplication)
    / (division)
    % modulo

variable = variable + X 
variable += X

variable = variable - X 
variable -= X

variable = variable * X 
variable *= X
    
"""

calcul = 5 / 2
calcul = int(calcul)
calcul2 = 5 % 2
calcul2 = int(calcul2)

print("Resultat :", calcul)
print("Resultat :", calcul2)

calcul3 = 5 + 3 * 7 # fonctionne comme en maths avec priorité de certaines opérations
calcul3 = int(calcul3)
calcul4 = (5 + 3) * 7
calcul4 = int(calcul4)

print("Resultat :", calcul3)
print("Resultat :", calcul4)

niveauPerso = 1
print("Niveau du personnage :", niveauPerso)

niveauPerso = niveauPerso + 1
print("Bravo, tu avances ! Niveau :", niveauPerso)

niveauPersonnage = input("Quel est le niveau du personnage ? ")
niveauPersonnage = int(niveauPersonnage)

print("Niveau du personnage :", niveauPersonnage)

print("Combat réussi, tu gagnes un niveau !")
niveauPersonnage += 1

print("Niveau du personnage :", niveauPersonnage)