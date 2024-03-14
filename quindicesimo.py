# Esercizio: ho la stringa "123", la voglio trasformare in [1, 2, 3].
#definire una funzione che risolva il problema

def StringToList(a):
    return [int(x) for x in a]

a = "123"
print(StringToList(a))
