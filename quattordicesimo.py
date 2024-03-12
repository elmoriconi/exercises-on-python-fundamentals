import random

def ColoreRandom():
    colori = ["rosso", "giallo", "verde", "blu", "arancio", "ciano"]
    return colori[random.randint(0, len(colori)-1)]


print(ColoreRandom())