#coding:utf-8

"""

Module pour le joueur

"""

def parler(personnage, message):
    print("{} : {}".format(personnage, message))

def au_revoir():
    print("Au revoir")


# Tester indépendamment chaque module

if __name__ == "__main__": # __nomDuModule__ == "__nomDuProgrammeQuiExecute__"
    print("PHASE DE TEST DE PLAYER.PY")
    parler("Agnes", "Bonjour")
    au_revoir()