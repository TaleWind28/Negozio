__all__=["player","tappe","stampa"]

from .player import Player #classe Player
from .player import GenPlayer #Funzione che crea un player dato un file
from .player import AddPlayer #Funzione che aggiunge il punteggio ad un player dato un file
from .tappe import AddTappe #Funzione che aggiunge il punteggio di ogni giocatore nell tappe disputate
from .stampa import Printing #Funzione che stampa la classifica