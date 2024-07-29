#coding:utf-8

# MODULARITÉ

"""

Importation d'un module :

    - Importer un module : import <nom_module>
    - Importer une fonction : from <nom_module> import <nom_fonction>
    - Importer tous les modules d'un module : from <nom_module> import *

Fonctions math :

    - sqrt : racine carrée
    - sin : sinus


"""
"""
import math # Import module math
resultat = math.sqrt(100) # Module + fonction (racine carrée) du module utilisée
print(resultat)

###

from math import sqrt  # N'importer que sqrt du module math

###

from math import * # Importer tous les modules du module math, évite de répéter "math."

###

from math import sqrt, sin # N'importer que sqrt et sin du module math

sinus = sin(42)
print(sinus)


###

# Créer son propre module (fichier player.py)

import includes.player as player  # player est placé dans le dossier includes

player.parler("Joueur", "Bonjour")

player.au_revoir()

"""

###

# Tester indépendamment chaque module

