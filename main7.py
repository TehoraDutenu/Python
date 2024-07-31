#coding:utf-8

# CLASSES ET ATTRIBUTS

"""

# Base 

class Humain:
   '''
   # Classe des êtres humains
   '''
    def __init__(self):
        pass # Sortir de la classe

print("Lancement du programme")

###

# Utilisation

class Humain:

    '''
    Classe des êtres humains
    '''
    def __init__(self):
        print("Création d'un Humain", self)

print("Lancement du programme")

h1 = Humain() # Creation d'un objet de la classe Humain (instanciation)
h2 = Humain()

###

# ATTRIBUTS

class Humain:

    '''
    Classe des êtres humains
    '''
    def __init__(self):
        print("Création d'un Humain")
        self.prenom = "Jojo"
        self.age = 1

print("Lancement du programme")

h1 = Humain()
print("Prénom de h1 -> {}".format(h1.prenom))

h2 = Humain()

###

class Humain:

    '''
    Classe des êtres humains
    '''
    def __init__(self, c_prenom="Gégé", c_age=18): # Par défaut (marche comme pour les fonctions)
        print("Création d'un Humain")
        self.prenom = c_prenom
        self.age = c_age

print("Lancement du programme")

h1 = Humain("Jojo", 25)
print("Prénom de h1 -> {}".format(h1.prenom))
print("Âge de h1 -> {}".format(h1.age))

h2 = Humain("Titi", 30)
print("Prénom de h2 -> {}".format(h2.prenom))
print("Âge de h2 -> {}".format(h2.age))

###

class Humain:

    '''
    Classe des êtres humains
    '''
    def __init__(self, c_prenom, c_age): 
        print("Création d'un Humain")
        self.prenom = c_prenom
        self.age = c_age

print("Lancement du programme")

h1 = Humain("Jojo", 25)
print("Prénom de h1 -> {}".format(h1.prenom))
print("Âge de h1 -> {}".format(h1.age))

h1.prenom = "Titi"
print("Prénom de h1 -> {}".format(h1.prenom))
"""

###

# Attributs de classe

class Humain:

    '''
    Classe des êtres humains
    '''

    humains_crees = 0 # Attribut de classe

    def __init__(self, c_prenom, c_age): 
        print("Création d'un Humain")
        self.prenom = c_prenom
        self.age = c_age
        Humain.humains_crees += 1

print("Lancement du programme")

h1 = Humain("Jojo", 25)
print("Humains existants : {}".format(Humain.humains_crees))

h2 = Humain("Titi", 30)
print("Humains existants : {}".format(Humain.humains_crees))