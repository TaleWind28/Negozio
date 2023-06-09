class Player:
    def __init__(self,nome,punteggio):
        self.nome = nome
        self.punteggio = punteggio
        self.printed = False

def GenPlayer(string,p):
        l1 = string.split(';')
        lp = l1[1].split('\n')
        punt = int(lp[0])
        a = Player(l1[0],punt)
        p.append(a)

def AddPlayer(string,p):
    l1 = string.split(';')
    lp = l1[1].split('\n')
    punt = int(lp[0])
    for x in p:
        if x.nome == l1[0]:
            x.punteggio+=punt

