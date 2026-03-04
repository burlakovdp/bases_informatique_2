##############################################################
##                                                          ##
##  Module pour manipuler des arbres binaire d’expression   ##
##                                                          ##
##############################################################

from random import randint
IMPLÉMENTATION = randint(0,1)



class Arbre():

    def __init__(self, r, g, d):
        self.racine = r
        self.gauche = g
        self.droite = d

    def __repr__(self):
        return f"({self.racine} {self.gauche} {self.droite})"

if IMPLÉMENTATION == 0:

    def arbre(r, Ag, Ad):
        """
        Construit un arbre à partir d’une racine et de deux arbres.
        """
        return Arbre(r, Ag, Ad)

    def est_feuille(A):
        """
        Regarde si l’arbre A est composé ou s’il est une simple feuille.
        Une feuille est soit un entier soit une chaîne de caractère.
        """
        return type(A) == int or type(A) == str


    def racine(A):
        """
        Renvoie la racine de l’arbre A
        A doit être un arbre composé et non une feuiile
        """
        if est_feuille(A):
                raise ValueError("une feuille n’a pas de racine")
        return A.racine


    def fg(A):
        """
        Renvoie le fils gauche de l’arbre A
        A doit être un arbre composé et non une feuiile
        """
        if est_feuille(A):
                raise ValueError("une feuille n’a pas de fils gauche")
        return A.gauche


    def fd(A):
        """
        Renvoie le fils droit de l’arbre A
        A doit être un arbre composé et non une feuiile
        """
        if est_feuille(A):
                raise ValueError('une feuille n’a pas de fils droit')
        return A.droite


else:


    def arbre(r, Ag, Ad):
        """
        Construit un arbre à partir d’une racine et de deux arbres.
        """
        return (r, Ag, Ad)


    def est_feuille(A):
        """
        Regarde si l’arbre A est composé ou s’il est une simple feuille.
        Une feuille est soit un entier soit une chaîne de caractère.
        """
        return type(A) == int or type(A) == str


    def racine(A):
        """
        Renvoie la racine de l’arbre A
        A doit être un arbre composé et non une feuiile
        """
        if est_feuille(A):
                raise ValueError("une feuille n’a pas de racine")
        return A[0]


    def fg(A):
        """
        Renvoie le fils gauche de l’arbre A
        A doit être un arbre composé et non une feuiile
        """
        if est_feuille(A):
                raise ValueError("une feuille n’a pas de fils gauche")
        return A[1]


    def fd(A):
        """
        Renvoie le fils droit de l’arbre A
        A doit être un arbre composé et non une feuiile
        """
        if est_feuille(A):
                raise ValueError('une feuille n’a pas de fils droit')
        return A[2]