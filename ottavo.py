#Sapendo che la funzione random.randint(start, end) genera un numero intero
#compreso tra start e end, end compreso, costruire una lista di numeri casuali 
#lunga 100 e stampare la somma di tutti i suoi numeri
    
import random   

lista = []
for i in range(100):
    x=random.randint(1, 10)  
    lista.append(x)

somma = 0
for i in lista:
    somma = somma + i

print(somma)