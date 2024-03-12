a = 10
b = 20
c = 30

if a % 2 == 0:
    print(b+c)
else:
    print(b-c)

#si poteva scrivere anche con gli operatori booleani (più veloce): 
#if a & 1 == 0:

#terzo modo:
# if math.floor(a/2)*2 == a
#che significa? esempio: 7/2 = 3,5 => prendo solo la parte intera
# 3 * 2 = 6. 6 == 7 ? no, quindi dispari

a = 13
b = 7
c = 2
if a % 2 == 0:
    print(b+c)
else:
    print(b-c)

a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    print(b+c)
else:
    print(b-c)

#Per evitare di copiare continuamente lo stesso pezzo di codice uso le funzioni
    
def Arit(a, b, c):
    if a % 2 == 0:
        print(b+c)
    else:
        print(b-c)

Arit(10, 11, 12)
Arit(11, 2, 3)
Arit(101, 1000, 2)
a, b, c = 10, 20, 30
Arit(b, c, a)


def Cambia(a, b):
    a = b
    print(a)   #stampa 200


a = 100
b = 200
Cambia(a, b)
print(a)   #stampa 100

def Somma(a, b):
    c = a + b
    return c

print(Somma(1, 2)) #stampa 3
print(Somma("a", "b")) #stampa a e b

def Divisione(a, b):
    return a // b, a % b

h, i = a // b, a % b 

