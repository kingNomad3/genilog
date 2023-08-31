import random
# from tkinter import *
# from random import choice


class Docteur():
    # cette fonction (i.e.la fct init) nest pas obligatoire... si on a un init on passe par la et on rempli l'objet
    # par des attributs self veut dire que ...
    def __init__(self, parent, x: int, y: int):
        self.parent = parent
        self.x = x
        self.y = y

    def jouer_coups(self, rep):

        if self.x >= 0 and self.x < self.parent.airedejeu.largeur-1:
            if self.y >= 0 and self.y < self.parent.airedejeu.hauteur-1:

                self.x += rep[0]
                self.y += rep[1]
            else:
                self.x = self.x
                self.y = self.y
        else:
            self.x = self.x
            self.y = self.y





# doc1 = Docteur()
# doc2 = Docteur()
# doc3 = Docteur
# doc4 = doc3()

# print(doc1)
# print(doc2)
# print(doc3)
# print(doc4)

class Dalek():
    def __init__(self, parent, x: int, y: int):
        self.parent = parent
        self.x = x
        self.y = y


class Ferraille():
    def __init__(self, parent, x: int, y: int):
        self.parent = parent
        self.x = x
        self.y = y


class AireDeJeu():
    def __init__(self, parent, largeur: int, hauteur: int):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur


class Partie():
    def __init__(self, parent):
        self.parent = parent
        self.airedejeu = AireDeJeu(self, 10, 8)
        self.doc = Docteur(self, 5, 4)
        self.daleks = []
        self.ferrailles = []
        self.niveau = 0
        self.daleksParNiveau = 5
        self.creer_niveau()

    def creer_niveau(self):
        self.niveau += 1 # ya pas de ++ et -- en python il faut donc utiliser +=1 et -=1
        nb_daleks = self.niveau * self.daleksParNiveau
        for i in range(nb_daleks):
            x = random.randrange(self.airedejeu.largeur)
            y = random.randrange(self.airedejeu.hauteur)
            d = Dalek(self, x, y)
            self.daleks.append(d)

    def jouer_coups(self, rep):
        self.doc.jouer_coups(rep)


# la vue se charge de faire l'affichage
class Vue():
    def __init__(self, parent):
        self.parent = parent
        self.options_deplacement = {"1": [-1, 1],
                                    "2": [0, 1],
                                    "3": [1, 1],
                                    "4": [-1, 0],
                                    "5": [0, 0],
                                    "6": [1, 0],
                                    "7": [-1, 1],
                                    "8": [0, -1],
                                    "9": [1, -1]
                                    } # accolades = dictionnaire
        # self.affiche_airedejeu()

    def afficher_demarrage(self):
        print("    Bienvenue aux DALEKS")
        rep = input("Que desirez-vous faire ? (1-jouer, 2-afficher score, 3-quitter) : ")
        if rep == "1":
            return "partie"
        elif rep == "2":
            print("Pas de score")
        else:
            pass
        return None

    def afficher_jeu(self, partie):
        tableau = self.creer_airedejeu(partie.airedejeu)
        for i in partie.daleks:
            tableau[i.y][i.x] = "W"
        for i in partie.ferrailles:
            tableau[i.y][i.x] = "A"
        tableau[partie.doc.y][partie.doc.x] = "D"
        for i in tableau:
            print(i)

    def creer_airedejeu(self, aire):
        tableau = []
        for i in range(aire.hauteur):
            ligne = []
            for j in range(aire.largeur):
                ligne.append("-")
            tableau.append(ligne)
        return tableau

    def menu_prochain_coups(self):
        rep = input("Votre déplacement (pave num) : ")
        if rep in self.options_deplacement.keys():
            return self.options_deplacement[rep]
        else:
            return "Erreur"


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.partie = None
        self.joueur_courant = ""
    def creer_partie(self):
        self.partie = Partie(self)
    def jouer_coups(self, rep):
        self.partie.jouer_coups(rep)


class Controleur():
    def __init__(self):
        self.jeu_actif = False # jeu est pas actif en partant jeu est actif qd créer partie
        self.vue = Vue(self)
        self.modele = Modele(self)
        rep = self.vue.afficher_demarrage()
    # un splash screeen = c'est la toute premiere page que l'on voit au démarrage du jeu
        if rep == "partie":
            self.modele.creer_partie()
            self.jeu_actif = True
            self.boucler_jeu()

    def boucler_jeu(self):
        while self.jeu_actif:
            self.vue.afficher_jeu(self.modele.partie)
            rep = self.vue.menu_prochain_coups()
            if rep != "Erreur":
                self.modele.jouer_coups(rep)
            else:
                self.jeu_actif = False


if __name__ == "__main__":
    c = Controleur()
