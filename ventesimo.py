"""def MCD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:  
            b = b - a    
    return a 

a = int(input("Inserire il primo numero: "))
b = int(input("Inserire il secondo numero: "))
print("MCD: ", MCD(a, b))
"""
def CancMultipli(n, lista):
    for i in range(10):
        m = i * n
        lista.pop(m)
    return lista

lista = []
primi = []
for i in range(2, 1000000):
    lista.append(i)
for x in lista:
    CancMultipli(x, lista)
    primi.append(x)
print(primi)