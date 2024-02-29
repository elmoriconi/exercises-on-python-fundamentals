#stampare la tabellina del 23

for i in range(23, 231, 23):
    print(i)

#oppure

for i in range(10):
    print(23 * (i + 1))

#oppure

for i in range(1, 11):
    print(23 * i)

t = 23
for i in range(10):
    print(t)
    t = t + 23

#ce ne sono tanti altri

#Sapendo che la funzione random.randint(start, end) genera un numero intero
#compreso tra start e end, end compreso, costruire una lista di numeri casuali 
#lunga 100 e stampare la somma di tutti i suoi numeri
    
import random   

lista = []
for i in range(101):
    x=random.randint(1, 10)  
    lista.append(x)

somma = 0
for i in lista:
    somma = somma + i

print(somma)