#esempio di progetto segmentato

# 1) data un lista ls contenente N digit da 1 a N non necessariamente tutti presenti e con eventuali ripetizioni
# N = 8, ls = [1, 1, 2, 2, 3, 5, 8, 8]

# sia data una seconda lista lscheck, costruita esattamente come la precedente (con valori diversi)
# N = 6, ls = [1, 3, 2, 2, 5, 6] lscheck = [2, 3, 3, 6, 6, 4]
#scrivere una funzione alla quale passare come parametri ls e lscheck e la funzione deve riportare 2 valori:
#il primo: tutte le volte (contare quante) che c'è lo stesso digit nella stessa posizione di ls e lscheck
#poi tolgo dalle due liste i valori che stanno nella stessa posizione
#il secondo: tutte le volte in cui un elemento della lista lscheck è presente in ls, ma non nella stessa posizione
#(non conto due volte gli elementi ripetuti) => levo da ls i valori che trovo

# Genera lista di N numeri casuali da 1 a N
import random

def GeneraLista(N):
    lista = []
    for i in range(N):
        x = random.randint(1, N)
        lista.append(x)
    return lista

def ContaUguali(ls, lscheck):
    uguali = 0
    posizdiversa = 0
    for i in range(len(ls)):
        if lscheck[i] == ls[i]:
            uguali += 1
            ls.pop(i)
            lscheck.pop(i)
    for i in lscheck:
        if i in ls:
            posizdiversa += 1
            ls.remove(i)
    print(ls)
    print(lscheck)
    return uguali, posizdiversa

ls = GeneraLista(7)
lscheck = GeneraLista(7)
print(ls)
print(lscheck)
print(ContaUguali(ls, lscheck))