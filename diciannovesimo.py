import copy
import random


# Genera una lista che contiene M numeri casuali tra 1 e N
def GeneraLista(N, M):
    lista = []
    for i in range(M):
        v = random.randint(1, N)
        lista.append(v)
    return lista

def ConvertiStringaDigitInListaNumeri(l2):
    return [int(x) for x in list(l2)]

def ContaUgualiInStessoEInAltro(ls, lsCheck):
    ls = ls.copy()
    lsCheck = lsCheck.copy()
    # Conteggio e elimino gli elementi nello stesso posto
    stessoPosto = 0
    for i in range(len(lsCheck)):
        if lsCheck[i] == ls[i]:
            stessoPosto += 1
            ls[i] = None
            lsCheck[i] = None

    # Conteggio e elimino gli elementi in posto differente
    altroPosto = 0
    for v in lsCheck:
        if v != None and v in ls:
            altroPosto += 1
            ls.remove(v)
    return stessoPosto, altroPosto


N = int(input("Inserire il numero di simboli: "))
M = int(input("Inserire la lunghezza della lista: "))
l1 = GeneraLista(N, M)
strike = 0 
while strike!= M:
    l2 = input("Inserire la sequenza: ")
    lista = ConvertiStringaDigitInListaNumeri(l2)
    strike, ball = ContaUgualiInStessoEInAltro(l1, lista)
    print("Strike: ", strike, "Ball: ", ball)
print("Hai vinto! ", l1)


"""
Progetto:
Il gioco del mastermind consiste in:
- N palline colorate (i digit)
- M caselle da riempire (lunghezza delle liste)
- una sequenza di M palline colorate generata dal master del gioco
- un ciclo di prove in cui:
    1) il giocatore fornisce la proposta
    2) il master verifica il numero di strike e ball ottenuti
    3) il master comunica strike e ball al giocatore
    4) se sono M strike, il giocatore ha vinto
    5) altrimenti si riparte da 1
"""