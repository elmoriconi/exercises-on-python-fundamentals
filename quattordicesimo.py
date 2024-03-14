# Esercizio
# definire la funzione ColoreRandom() che torna una stringa casuale tra "rosso", 
# "giallo", "verde", "blu", "arancio", "ciano", ...

import random

def ColoreRandom():
    colori = ["rosso", "giallo", "verde", "blu", "arancio", "ciano", "rosa"]
    return colori[random.randint(0, len(colori)-1)]


print(ColoreRandom())


#funzione che fa la radice quadrata

def Square(x):
    return x * x

print(Square(2894124))

#funzione che fa la radice quadrata

def Sqrt(a):
    return a**0.5

#funzione che stabilisce il numero maggiore

def Maggiore(a, b):
    if a > b:
        return a
    else:
        return b

print(Maggiore(10, 20))
def Combinazioni():
    digits = []
    for i in range(0, 10000):
        s = str(i)
        while len(s) < 4:
            s = "0" + s
        digits.append(s)
    return digits

print(Combinazioni())
    
print(Maggiore([1, 5, 7, 9, 34, 67, 24, 89]))


#Esercizio
#scrivere una funzione che costruisce una lista contenente
#tutte le possibili combinazioni di quattro digit.
#Ricorda che un digit è uno tra 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

def Combinazioni():
    digits = []
    for i in range(0, 10000):
        s = str(i)
        while len(s) < 4:               #oppure s = s.zfill(4)
            s = "0" + s                 #oppure s = "0" * (4 - len(s)) + s
        digits.append(s)
    return digits

print(Combinazioni())

#Data una stringa numerica, convertirla in una lista di digit

def StringToList(a):
    return [int(x) for x in a]

a = "987532"
print(StringToList(a))

"""
alternativa

def StringDigitsToList(sd):
    lista = []
   
    for c in sd :
        lista.append(int(c))
    return lista

print(StringDigitsToList("945243"))

"""

#Modificare la funzione Combinazioni per generare una lista di liste del tipo
#[[0,0,0,0],[0,0,0,1],[0,0,0,2]...]   ESERCIZIO PER CASA

def Combinazioni():
    digits = []
    for i in range(0, 10000):
        s = str(i)
        while len(s) < 4:
            s = "0" + s
        lista = [int(x) for x in s]
        digits.append(lista)
    return digits

print(Combinazioni())
