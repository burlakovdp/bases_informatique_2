from lc import *

def longueur(lc):
    if not is_empty(lc):
        return 1 + longueur(tail(lc))
    return 0

def double(lc):
    res = vide()
    if not is_empty(lc):
        res = liste(head(lc)*2, double(tail(lc)))
    return res

def majeur(lc):
    res = vide()
    if not is_empty(lc):
        if head(lc) > 18:
            res = liste(head(lc), majeur(tail(lc)))
        else:
            majeur(tail(lc))
    return res
        
        

