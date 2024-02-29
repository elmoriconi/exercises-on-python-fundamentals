#Costruire due liste, la prima che contiene i numeri pari 
#fino a 1000, la seconda che contiene i numeri dispari fino 
#a 1000. A partire dalle prime due liste, costruire una terza 
#lista che contiene prima tutti i pari e poi tutti i dispari.

listapari = []
for i in range(1000):
    if i % 2 == 0:
        listapari.append(i)
    else:
        i + 1

listadispari = []
for i in range(1000):
    if i % 2 != 0:
        listadispari.append(i)
    else:
        i + 1

#fin qui ok
#print(listapari, listadispari)
        
terzalista = listapari + listadispari

print(terzalista)