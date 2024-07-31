#coding:utf-8

# PROPRIÉTÉS D'ENCAPSULATION

"""
Propriété : manière de manipuler/contrôler des attributs
            principe d'encapsulation !
"""

"""
# Getter
class Humain:

    def __init__(self, nom, age):
        print("Création d'un Humain")
        self.nom = nom
        self._age = age # underscore est une convention pour expliquer que l'attribut est privé (encapsulé)

    def _getage(self):
        return self._age
    
    # property (<getter>, <setter>, <deleter>, <helper)
    age = property(_getage)


# programme principal
h1 = Humain("Jojo", 25)

print(h1.age)

###

# Setter

class Humain:

    def __init__(self, nom, age):
        print("Création d'un Humain")
        self.nom = nom
        self._age = age # underscore est une convention pour expliquer que l'attribut est privé (encapsulé)

    def _getage(self):
        return self._age
    
    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self.age = 0
        else:
            self._age = nouvel_age
    
    # property (<getter>, <setter>, <deleter>, <helper)
    age = property(_getage, _setage)


# programme principal
h1 = Humain("Jojo", 25)

print(h1.age)

h1.age = -5
print(h1.age)

###
# Deleter

class Humain:

    def __init__(self, nom, age):
        print("Création d'un Humain")
        self.nom = nom
        self._age = age 
    def _getage(self):
        try:
            return self._age
        except AttributeError:
            print("L'attribut 'age' n'existe pas")
    
    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self.age = 0
        else:
            self._age = nouvel_age

    def _delage(self):
        del self._age
    
    # property (<getter>, <setter>, <deleter>, <helper)
    age = property(_getage, _setage, _delage)


# programme principal
h1 = Humain("Jojo", 25)

print(h1.age)

del h1.age # le résultat donne un AttributeError puisque l'attribut a été delete alors on met un try au _getage

print(h1.age)

###


# Helper
class Humain:
    ''' Classe qui definit un humain '''

    def __init__(self, nom, age):
        print("Création d'un Humain")
        self.nom = nom
        self._age = age

    def _getage(self):
        try:
            return self._age
        except AttributeError:
            print("L'attribut 'age' n'existe pas")
    
    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self.age = 0
        else:
            self._age = nouvel_age

    def _delage(self):
        del self._age
    
    # property (<getter>, <setter>, <deleter>, <helper)
    age = property(_getage, _setage, _delage, "Je suis l'age d'un humain")


# programme principal

help(Humain) # récupération d'une aide à propos de la classe Humain
help(Humain.age) # récupération d'une aide à propos de l'attribut age

###

"""
class Humain:
    ''' Classe qui definit un humain '''

    def __init__(self, nom, age):
        print("Création d'un Humain")
        self.nom = nom
        self._age = age

    def _getage(self):
        if self._age <= 1:
            return "{} {}".format(self._age, "an")
        else:
            return "{} {}".format(self._age, "ans")
        
    # property (<getter>, <setter>, <deleter>, <helper)
    age = property(_getage)


# programme principal

h1 = Humain("Robert", 45)

print("{} a {}".format(h1.nom, h1.age))