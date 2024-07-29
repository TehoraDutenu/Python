#coding:utf-8

# GESTION D'ERREURS

"""
Message d'erreur :
    ValueError          (pour les erreurs relatives au cast)
    ZeroDivisionError   (pour les erreurs relatives aux divisions par 0)
    NameError           (pour les erreurs relatives aux noms non defini)
    IndexError          (pour les erreurs relatives aux index)
    KeyError            (pour les erreurs relatives aux clefs)
    TypeError           (pour les erreurs relatives aux types)
    AttributeError      (pour les erreurs relatives aux attributs)
    ImportError         (pour les erreurs relatives aux modules)
    OSError             (pour les erreurs relatives aux fichiers)
    AssertionError      (pour les erreurs relatives aux assertions)

"""

"""
# Le try: except: (+ else: + finally:)
ageUtilisateur = input("Quel age as-tu ? ")

try: # Essaie de caster la chaine de caractères
    ageUtilisateur = int(ageUtilisateur)
    print("Tu as", ageUtilisateur, "ans")
except: # En cas d'exception
    print("Ceci n'est pas un nombre !")

# OU

ageUtilisateur = input("Quel age as-tu ? ")

try: 
    ageUtilisateur = int(ageUtilisateur) 
except: 
    print("Ceci n'est pas un nombre !")
else: # Sinon
    print("Tu as", ageUtilisateur, "ans")

# OU

ageUtilisateur = input("Quel age as-tu ? ")

try: 
    ageUtilisateur = int(ageUtilisateur) 
except: 
    print("Ceci n'est pas un nombre !")
else: 
    print("Tu as", ageUtilisateur, "ans")
finally: # Si le try est bon ou pas, le finally est appelé
    print("Fin du programme")


###

nombre1 = 150

nombre2 = input("Choisir un nombre pour diviser : ")

try:
    nombre2 = int(nombre2)
    print("Résultat = {}".format(nombre1 / nombre2))
except ZeroDivisionError:
    print("Le diviseur ne doit pas être 0")
except ValueError:
    print("Ceci n'est pas un nombre !")
except:
    print("Une erreur est survenue")
else:
    print("OK")
finally:
    print("Fin du programme")

###

# Lever une exception

try:
    age = input("Quel age as-tu ? ")
    age = int(age)

    if age < 25:
        raise ZeroDivisionError("Tu es trop jeune")
except ZeroDivisionError:
    print("J'ai attrapé ton erreur !")

"""
###

# Gérer une assertion

try: 
    age = input("Quel age as-tu ? ")
    age = int(age)

    assert age > 25 # Je veux que age soit plus grand que 25
except AssertionError:
    print("Tu es trop jeune !")

