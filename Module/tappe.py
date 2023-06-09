from Module.player import *
from pathlib import Path

#Funzione che Genera i giocatori o aggiunge il punteggio delle giornate ai giocatori esistenti
def AddTappe(p):
    current_folder = Path('./Negozio/Input')
    for path in current_folder.iterdir():
        with open(path,'r') as f:
            for line in f:
                    if Check_Existance(line,p) == True:
                        AddPlayer(line,p) 
                    else:
                        GenPlayer(line,p)

#Funzione che cerca l'esistenza di un giocatore nel campionato
def Check_Existance(line,p):
    l1 = line.split(";")
    for player in p:
        if l1[0] == player.nome:
            return True
    return False

