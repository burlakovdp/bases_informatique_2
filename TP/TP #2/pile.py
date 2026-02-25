PileErreur=ValueError('Pile vide')

def nouvelle_pile():
        return []

def empile(L,e):
        L.append(e)

def depile(L):
        if L == []:
                raise PileErreur
        return L.pop()

def sommet(L):
        if L == []:
                raise PileErreur
        return L[len(L)-1]

def est_vide(L):
        return L==[]