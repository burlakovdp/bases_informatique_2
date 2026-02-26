#ex.1
def intérieur(ch):
    return ch[1:len(ch)-1]

def suivant(ch):
    return ch[1:]

def découpage(ch, i):
    return (ch[:i], ch[i], ch[i+1:])

