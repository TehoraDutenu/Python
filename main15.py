#coding:utf-8

# FICHIERS

"""
Les fichiers ne comprennent que des chaînes de caractères, il sera impératif de cast pour les autres formats

Modes d'ouverture :  r (read : lecture seule)
                     w (write : ecriture avec remplacement)
                     a (append : ecriture avec ajout en fin de fichier)
                     x (exclusive : lecture et ecriture)
                     r+ (read and write : lecture et ecriture)
                     
Ouvrir : open(<nom_fichier>, <mode>)

Fermer : fic.close()

Lire tout                   : <nom_fichier>.read()

Lire une seule ligne        : <nom_fichier>.readline()

Lire toutes les lignes      : <nom_fichier>.readlines()

Ecrire                      : <nom_fichier>.write(<contenu>)
                     
"""

"""
# Ouvrir un fichier

fic = open("donnees.txt", "r")

fic.close() # /!\ fermeture obligatoire du fichier

if fic.closed:
    print("Le fichier est fermé")
else:
    print("Le fichier n'est pas fermé")
    

# Lire les informations d'un fichier

## Tout lire
content = fic.read()
print(content)

## Lire une seule ligne
line = fic.readline() # Lire une seule ligne
print(line)

line = fic.readline() # Chaque appel retourne la ligne suivante
print(line)

line = fic.readline()
print(line)

# OU
lines = fic.readlines() # Lire toutes les lignes et les stocker dans une liste
print(lines)

# Fermeture du fichier
fic.close() 

# Autre syntaxe

## Ouvrir, lire et fermer avec "with"
with open("donnees.txt", "r") as fic:
    content = fic.read()
    print(content)
    
# PLUS BESOIN DE FERMER LE FICHIER

## Modifier le contenu d'un fichier
with open("donnees.txt", "a") as fic:
    nombre = 15
    fic.write(str(nombre))
    fic.write("\nLigne ajoutée 2\n")
    fic.write("Ligne ajoutée 3\n")

"""

# Objet fichier, enregistrement d'objets

import pickle
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    def whoami(self):
        print("Je m'appelle {}({})".format(self.name, self.level))
        
        
## Enregistrer l'instance de l'objet dans un fichier
with open("player.data", "rb") as fic: # "wb" = write binary
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()
    
player_one.whoami()





