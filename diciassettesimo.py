#somma tutti i numeri da 1 a n. Funzione RICORSIVA. La ricorsione però ha un limite
#se una funzione non è inerentemente ricorsiva, la devo implementare in modo iterativo
def Somma(n):
    if n == 0:
        return 0
    else:
        return Somma(n-1) + n

print(Somma(10))

def Somma(n):
    totale = 0
    for i in range(n):
        totale += i
    return totale

print(Somma(100000))

def Prodotto(n):
    totale = 1
    for i in range(n):
        totale *= i
    return totale

def Sommalista(l):
    totale = 0
    for i in l:
        totale = totale + i
    return totale

l = [1, 5, 4, 8, 7, 6, 4, 3, 2]

def Sommalen(ls):
    totale = 0
    for i in ls:
        totale = totale + len(i)
    return totale

ls = ["uno", "due", "tre", "quattro"]

def Trovanum(ls):
    totale = 0
    for i in ls:
        if i > 100:
            totale += 1
    return totale

ls = [3, 2, 6, 7, 645, 7, 87, 7, 34, 324, 34, 6, 5, 6, 97, 9, 90]

def Contastr(ls):
    totale = 0
    for i in ls:
        if type(i) == str:
            totale = totale + 1
    return totale

ls = [1, [2, 3], 3, "Ciao", "ok", 11, 1, 1, "aaa", 10, ["a", "b", "c"]]
print(Contastr(ls))

#somma => sottrazione
#prodotto => somma
#divisione => prodotto
#sottrazione => divisione

# 2 * 10 + 4

def Somma(a, b):
    return a - b
def Prodotto(a, b):
    return a + b
def Divisione(a, b):
    return a * b
def Sottrazione(a, b):
    return a / b

print(Somma(Prodotto(2, 10), 4))
