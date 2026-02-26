#ex.1
def intérieur(ch):
    return ch[1:len(ch)-1]

def suivant(ch):
    return ch[1:]

def découpage(ch, i):
    return (ch[:i], ch[i], ch[i+1:])

#ex.2
def suppression_espaces(ch):
    res = ''
    for e in ch:
        if e != ' ':
            res += e
    return res

def remplacement_négatif(ch):
    res = ''
    tmp = 0
    signe = '(+-*/^<=>&|~'
    if ch[0] == '-':
        res += '_'
        tmp = 1
    for i in range(tmp, len(ch)):
        if ch[i] == '-':
            if res[-1] in signe:
                res += '_'
            else:
                res += ch[i]
        else:
            res += ch[i]

    return res

#ex.3
