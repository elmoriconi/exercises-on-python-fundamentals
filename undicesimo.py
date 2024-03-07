lista_dispari = [x * 2 + 1 for x in range(0, 5)]
lista_numeri = [x for x in range(0, 5)]
print(lista_numeri)
print(lista_dispari)
print(list(zip(lista_numeri, lista_dispari)))

nomi = ["mario", "blanco", "verde"]
cognomi = ["rossi", "bianchi", "verdi"]

coppie = list(zip(nomi, cognomi))

print(coppie)

