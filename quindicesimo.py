# Esercizio: ho la stringa "123", la voglio trasformare in [1, 2, 3].
#definire una funzione che risolva il problema

def StringToList(a):
    return [int(x) for x in a]

a = "123"
print(StringToList(a))

######################################################################à


fin = open("alice.txt", "r")    # = apri il file che si chiama "...", "r" significa IN LETTURA. 
                                #Un file si può appendere in lettura, scrittura o per appendere ("w")
                                #fin è una variabile
linee = fin.readlines()         #linee è una lista di stringhe
fin.close()
#readlines legge tutte le righe incluso il carattere a capo \n (eol/eoln). Per levare \n faccio 'stripping':
l1 = []
for linea in linee:
    l1.append(linea.strip())
linee = l1
print(linee)

s = "alfa;beta;gamma"
#come posso ottenere la lista ["alfa", "beta, "gamma"]?
print(s.split(";"))     #usa ";" come separatore

#Dato alice.txt, stamare riga per riga tutte le parole che la compongono

fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()
l1 = []
for linea in linee:
    l1.append(linea.strip())
linee = l1
parole = []
for i in linee:
    parole.extend(i.split(" "))
print(parole)



#Data una lista di stringhe, eliminare dalla lista tutte le stringhe vuote
#se la lunghezza della stringa è minore di 1, la stringa è vuota.

def vuota(ls):
    return len(ls.strip()) > 0
 
ls = ["uno", "due", "", "", "", "", "", "fine"]
print(list(filter(vuota, ls)))


#altrimenti
"""
ls = ["uno", "due", "", "", "", "", "", "fine"]
lista = []
for x in ls:
    if len(x) > 0:
        lista.append(x)
print(lista)
"""