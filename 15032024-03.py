import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

"""
print(len(worldcup))

print(worldcup[1200])
print(worldcup[1200]['DateOfBirth'])

"""

# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!

# 1) Contare quanti calciatori hanno giocato per l'Italia

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
calcita = 0
for i in worldcup:
    if i["Team"] == "ITA":
        calcita += 1
    elif i["Team"] == "Italy":
        calcita += 1
    else:
        continue
print("Calciatori italiani: ", calcita)

# 2) Contare quanti calciatori hanno giocato per il Brasile

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
calcbra = 0
for i in worldcup:
    if i["Team"] == "BRA":
        calcbra += 1
    elif i["Team"] == "Brazil":
        calcbra += 1
    else:
        continue
print("Calciatori brasiliani: ", calcbra)

# 3) Contare quanti calciatori hanno giocato per l'Argentina

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
calcarg = 0
for i in worldcup:
    if i["Team"] == "ARG":
        calcarg += 1
    elif i["Team"] == "Argentina":
        calcarg += 1
    else:
        continue
print("Calciatori argentini: ", calcarg)

# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
calcbra = set()
calcita = set()
for i in worldcup:
    if i["Team"] == "Brazil":
        x = i.get("FullName")
        calcbra.add(x)
    elif i["Team"] == "BRA":
        x = i.get("FullName")
        calcbra.add(x)
for i in worldcup:
    if i["Team"] == "Italy":
        x = i.get("FullName")
        calcita.add(x)
    elif i["Team"] == "ITA":
        x = i.get("FullName")
        calcita.add(x)
calcbra.intersection_update(calcita)
print("I giocatori che hanno giocato sia per il Brasile che per l'Italia sono: ", calcbra)

# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
calcarg = set()
calcita = set()
for i in worldcup:
    if i["Team"] == "Argentina":
        x = i.get("FullName")
        calcarg.add(x)
    elif i["Team"] == "ARG":
        x = i.get("FullName")
        calcarg.add(x)
for i in worldcup:
    if i["Team"] == "Italy":
        x = i.get("FullName")
        calcita.add(x)
    elif i["Team"] == "ITA":
        x = i.get("FullName")
        calcita.add(x)
calcarg.intersection_update(calcita)
print("I giocatori che hanno giocato sia per l'Argentina che per l'Italia sono: ", calcarg)


# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo



# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo



# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
lista = []                                          #inserisco tutti i nomi in una lista 
for i in worldcup:
    x = i.get("FullName")
    lista.append(x)
diz = {c: lista.count(c) for c in lista}            #conto quante volte si ripete ogni nome
calciatore = " "
partecipazioni = 1
for a in diz:
    if diz[a] > partecipazioni:
        calciatore = a
        partecipazioni = diz[a]
    else:
        continue
print(calciatore)                                   #perché non mi stampa nessun nome?

# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo. Organizzare per nazione. 
#    Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
lista1 = []
for i in worldcup:
    lista2 = []
    x = i.get("ClubCountry")
    lista2.append(x)
    y = i.get("Club")
    lista2.append(y)
    lista1.append(lista2)
diz = {c: lista1.count(c) for c in lista1}
print(diz)                                          #no non va bene nemmeno così

"""
lista = []
for i in worldcup:
    diz = {
        "Nazione": " ",
        "Club": " "
    }
    x = i.get("ClubCountry")
    diz["Nazione"] = x
    y = i.get("Club")
    diz["Club"] = y
    lista.append(diz)
diz2 = {c: lista.count(c) for c in lista}
print(diz2)
"""
"""
listaclub = []                                              #inizzializzo una lista in cui scrivere tutti i club
for i in worldcup:
    x = i.get("Club")
    listaclub.append(x)
diz = {c: listaclub.count(c) for c in listaclub}                #conto quante volte si ripete ogni club
#non capisco in che ordine fare le cose...
"""


#Conta quanti calciatori per ogni squadra. La key è team e il value è il numero di calciatori 
#quanticalciatori = dict()
#for v in worldcup:
    # se v["Team"] è già presente, sommo 1, altrimenti metto a 1
#    if v["Team"] in quanticalciatori.keys():
#        quanticalciatori[v["Team"]] = quanticalciatori[v["Team"]]+1
#    else:
#        quanticalciatori[v["Team"]] = 1
