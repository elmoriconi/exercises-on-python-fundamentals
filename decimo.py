import random
import time

"""
start = time.time_ns()
lista = []
for v in range(1, 10):
    lista.append(random.randint(1, 10000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/10000000}")

start = time.time_ns()
trovati = 0
for v in range(1, 10):
    if random.randint(1, 1000000000) in lista:
        trovati += 1
end = time.time_ns()

print(f"Il tempo richiesto per cercare è: {(end-start)/10000000} e ne hai trovati {trovati}")

"""


###########################################################################################


start = time.time_ns()
set = set()
for v in range(1, 10000000):
    set.add(random.randint(1, 10000000))
end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/10000000}")

start = time.time_ns()
trovati = 0
for v in range(1, 10000000):
    if random.randint(1, 1000000000) in set:
        trovati += 1
end = time.time_ns()

print(f"Il tempo richiesto per cercare è: {(end-start)/10000000} e ne hai trovati {trovati}")