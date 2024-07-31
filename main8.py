#coding:utf-8

# MÉTHODES

"""
Méthode           : fonction d'une classe (ex : manger, marcher, parler, dormir) 
Méthode de classe : fonction d'une classe (...)
Méthode statique  : fonction d'une classe, mais indépendante de celle-ci 
"""

"""
# Méthode

class Humain:

    ''' Classe qui définit un humain '''

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message))

# programme principal
h1 = Humain("Jojo", 25)

h1.parler("Bonjour")
h1.parler("Au revoir")

###

# Méthode de classe

class Humain:

    ''' Classe qui définit un humain '''

    lieu_habitation = "Terre"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, message): # self = méthode standart
        print("{} a dit : {}".format(self.nom, message))

    def changer_planete(cls, nouvelle_planete): # cls = méthode de classe
        Humain.lieu_habitation = nouvelle_planete

    changer_planete = classmethod(changer_planete)


# programme principal
h1 = Humain("Jojo", 25)

print("Planète actuelle : {}".format(Humain.lieu_habitation))

Humain.changer_planete("Mars")

print("Planète actuelle : {}".format(Humain.lieu_habitation))

"""

###

# Méthode statique

class Humain:

    ''' Classe qui définit un humain '''

    lieu_habitation = "Terre"

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, message): # self = méthode standart
        print("{} a dit : {}".format(self.nom, message))

    def changer_planete(cls, nouvelle_planete): # cls = méthode de classe
        Humain.lieu_habitation = nouvelle_planete

    changer_planete = classmethod(changer_planete)

    def definition():
        print("Je suis une méthode statique")

    definition = staticmethod(definition)


# programme principal

Humain.definition()