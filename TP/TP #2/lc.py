##################################################
##                                              ##
##  Module pour manipuler les listes chaînées   ##
##                                              ##
##################################################

from random import randint
IMPLÉMENTATION = randint(0,1)


class Vide:

    def __init__(self):
        pass

    def est_vide(self):
        return True

    def __repr__(self):
        return "⋅"

    def __eq__(self, x):
        return type(self) == type(x)

class LC:

    def __init__(self,t,q):
        self.tête = t
        self.queue = q

    def est_vide(self):
        return False

    def __eq__(self, x):
        if type(self) != type(x):
            return False
        else:
            return (x.tête == self.tête) and (x.queue == self.queue)

    def __repr__(self):
        return f"{self.tête} → {self.queue}"



if IMPLÉMENTATION:
    def is_empty(lc):
        return lc.est_vide()

    def vide():
        """Renvoie une liste chaînée vide"""
        return Vide()

    def liste(t,q):
        """Construit une liste chaînée à partir d’une tête et d’une queue"""
        return LC(t, q)

    def head(lc):
        if is_empty(lc):
            raise ValueError("head n’est pas définie pour une liste vide")
        return lc.tête


    def tail(lc):
        if is_empty(lc):
            raise ValueError("head n’est pas définie pour une liste vide")
        return lc.queue

else:



    def is_empty(lc):
        return lc == None

    def vide():
        """Renvoie une liste chaînée vide"""
        return None

    def liste(t,q):
        """Construit une liste chaînée à partir d’une tête et d’une queue"""
        return (t, q)

    def head(lc):
        if is_empty(lc):
            raise ValueError("head n’est pas définie pour une liste vide")
        (h,t) = lc
        return h


    def tail(lc):
        if is_empty(lc):
            raise ValueError("head n’est pas définie pour une liste vide")
        (h,t) = lc
        return t



def triche(*tab):
    match tab:
        case () :
            return vide()
        case (a, *b):
            return liste(a, triche(*b))