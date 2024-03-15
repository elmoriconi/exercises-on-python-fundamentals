a = 10
b = 20
if a > b:
    print(a-b)
else:
    print(b-a)

#potrei avere anche un if senza else
    if a > b:
        print("maggiore")

#in questo caso, dato che if è breve, si può mettere sulla stessa riga. 
#Breve = c'è un solo statement dopo if.
#Analogamente se ho sia then, sia else con un solo statement, posso scrivere:
        print(a-b) if a > b else print(b-a)
#Se ho più if in sequenza posso usare elif come keyword
if a>b:
    print(a-b)
elif a==b:
    print("sono uguali")
elif a<b:
    print(b-a)
else:
    print("boh")


#Esercizio: leggere da un file (persone.txt) i nomi, cognomi e età di un gruppo 
#di persone. Organizzarli in un dizionario la cui chiave è il cognome e il cui
#valore è una tupla contenente i tre valori letti.
    
fin = open("persone.txt", "r")
linee = fin.readlines()
fin.close()

for i in linee:
    nome = i.strip().split(",")
    print("Nome: ", nome[0], "Cognome: ", nome[1], "Età: ", nome[2])


"""
    diz = {
        "Nome" : nome[0],
        "Cognome" : nome[1],
        "Età" : nome[2]
    }
    print(diz)
"""
#Leggere da input una stringa. Se minore di "lettera", stampare 
#la stringa "minore", se maggiore di "lettera" e minore di "tocco", stampare 
#"intermedia", se maggiore di "tocco" e minore dui "what" stampare "maggiore", 
#altrimenti stampare "massima"

