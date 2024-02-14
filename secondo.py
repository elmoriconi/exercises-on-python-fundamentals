"""definire: 
    due variabili di tipo intero, 
    due variabili di tipo stringa, 
    due variabili di tipo float, 
    due variabili di tipo booleano 
stampare:
    i1 + i2 
    s1 + s2 
    f1 + f2 
    b1 + b2 
    i1 + s1
    s1 + i2
    i1 + f2
    f2 + i2
    i1 + b1
    f1 + b1
    s1 + b1
    b1 + i1
    b1 + s1
    b1 + f1

e commentare i risultati """

i1 = 2
i2 = 5
s1 = "Ciao"
s2 = "Hello"
f1 = 10.2
f2 = 0.4
b1 = True
b2 = False

a = i1 + i2 
b = s1 + s2 
c = f1 + f2 
d = b1 + b2 
#e = i1 + s1 somma tra un intero e una stringa, non si può fare
#f = s1 + i2 somma tra intero e stringa, errore
g = i1 + f2 #somma tra intero e float
h = f2 + i2 #somma tra intero e float
i = i1 + b1 #somma tra intero e booleano, se il booleano è true sommo 1 altrimento sommo 0
j = f1 + b1 #somma tra float e booleano, stesso di sopra
#k = s1 + b1 somma tra stringa e booleano, non si può
l = b1 + i1 #somma tra booleano e intero 
#m = b1 + s1 #somma tra booleano e stringa, non si può
n = b1 + f1 #somma tra booleano e float

print(a, b, c, d)
print(g, h, i, j)
print(l, n)


"""
print e input

"""
