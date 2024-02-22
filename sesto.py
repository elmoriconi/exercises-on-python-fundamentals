# per generare un numero casuale tra 10 e 20, 20 incluso: random.randint(10, 20)
# per generare un numero casuale tra 0 e 1: random.random()
# GENERARE UNA LISTA DI UN MILIONE DI ELEMENTI RANDOM. CALCOLARNE LA SOMMA E LA MEDIA.

import random

lista = []
n = 1000000
for i in range(n):
    x=random.randint(10, 20)  
    lista.append(x)

somma = 0
for i in lista:
    somma = somma + i

media = somma/n

print(somma)
print(media)