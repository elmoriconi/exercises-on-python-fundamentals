# Esercizio
# definire la funzione ColoreRandom() che torna una stringa casuale tra "rosso", 
# "giallo", "verde", "blu", "arancio", "ciano", ...


import random

def ColoreRandom():
    colori = ["rosso", "giallo", "verde", "blu", "arancio", "ciano"]
    return colori[random.randint(0, len(colori)-1)]


print(ColoreRandom())