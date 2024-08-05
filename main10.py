#coding:utf-8

# HÉRITAGE

"""
Classe         : plan de conception, genre (ex : Humain)
Classe mere    : plan de conception, genre (ex : Humain)
Classe fille   : plan de conception, genre (ex : Humain)

Fonctions utiles :

    isinstance(<objet>, <classe>) : verifie qu'un objet est de la classse indiquée
    issubclass(<classe-fille>, <classe_mere>) : verifie qu'une classe est une sous-classe d'une autre

    
"""

"""# Classe mère

class Vehicule:

    def __init__(self, nom, quantite_essence):
        self.nom = nom
        self.essence = quantite_essence

# Classe fille

class Voiture(Vehicule):
    pass

# programme principal

v1 = Vehicule("F22 Raptor", 2400)
v2 = Vehicule("Toyota Supra", 90)
print(v1.nom)
print(v2.nom)

###

# Classe mère

class Vehicule:

    def __init__(self, nom_vehicule, quantite_essence):
        self.nom = nom_vehicule
        self.essence = quantite_essence

    def se_deplacer(self):
        print("Le véhicule {} se déplace...".format(self.nom))


# Classe fille

class Voiture(Vehicule):
    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self, nom_voiture, essence)
        self.puissance = puissance


# programme principal

voiture1 = Voiture("Toyota Supra", 90, 420)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")

###

# Classe mère

class Vehicule:

    def __init__(self, nom_vehicule, quantite_essence):
        self.nom = nom_vehicule
        self.essence = quantite_essence

    def se_deplacer(self):
        print("Le véhicule {} se déplace...".format(self.nom))


# Classes filles

class Voiture(Vehicule):
    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self, nom_voiture, essence)
        self.puissance = puissance

    def se_deplacer(self):
        print("Je roule")

class Avion(Vehicule):
    def __init__(self, nom, essence, marchandise):
        Vehicule.__init__(self, nom, essence)
        self.marchandise = marchandise

    def se_deplacer(self):
        print("Je vole")

# programme principal

voiture1 = Voiture("Toyota Supra", 90, 420)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")

av1 = Avion("F22 Raptor", 2400, "Missiles")
av1.se_deplacer()


"""
###

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(self.nom, "mange")

class Reptile(Animal):
    def __init__(self, nom, regime_alimentaire):
        Animal.__init__(self, nom)
        self.regime = regime_alimentaire

    def manger(self):
        print("Le reptile mange")


# programme principal
lezard = Reptile("Lézard", "Grenouille")
lezard.manger()

print(isinstance(lezard, Animal)) # "True" pour lezard : isinstance vérifie qu'un objet est de la classse indiquée

if isinstance(lezard, Reptile):
    print("Lezard est un reptile")
else:
    print("Lezard n'est pas un reptile")

if isinstance(lezard, Animal):
    print("Lezard est un animal")
else:
    print("Lezard n'est pas un animal")

if issubclass(Reptile, Animal):
    print("Reptile hérite de Animal") 