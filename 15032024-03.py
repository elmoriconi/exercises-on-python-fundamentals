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
for a in diz.keys():
    if a != "":
        if diz[a] > partecipazioni:
            calciatore = a
            partecipazioni = diz[a]
print("Calciatore: ", calciatore, partecipazioni)                                   #perché non mi stampa nessun nome?

#come l'ha fatto il professore:
calciatori = dict()
for c in worldcup:
    key = c["FullName"] + ":" + c["DateOfBirth"]
    if key in dict.keys():
        calciatori[key] = calciatori[key] + 1
    else:
        calciatori[key] = 1
massimo = 0
calciatore = None
for chiave, valore in calciatori.items():
    if chiave.split(":")[0] != "":
        if valore > massimo:
            massimo = valore
            calciatore = chiave    
print(massimo, calciatore)

# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo. Organizzare per nazione. 
#    Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

squadre = dict()
for calciatore in worldcup:
    if c["Club"] in squadre.keys():
        squadre[c["Club"]] += 1
    else:
        squadre[c["Club"]] = 1
massimo = 0
squadra = None
for s in squadre.items():
    if s[1] > massimo:
        squadra, massimo = s
print(massimo, squadra)

# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
#così non dà i nomi

filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
Compleanno = []
for Date in worldcup:
    yearb = int(Date["DateOfBirth"].split("-")[0])
    if yearb != "":
        yearb = int(yearb)
        yearc = Date["Year"]
        Compleanno.appened((yearb, yearc))
anno = [dates[1] - dates[0] for dates in Compleanno]
print("Calciatore più giovane: ", max(anno) )
print("Calciatore più anziano: ", min(anno))
exit(-1)

#così per trovare anche i nomi
calciatore_piu_giovane = None
eta_piu_giovane =200
for giocatore in worldcup:
    campionato = giocatore["Year"]
    data_di_nascita = giocatore['DateOfBirth']
    if data_di_nascita:
        anno_di_nascita = int(data_di_nascita.split('-')[0])
        eta = campionato - anno_di_nascita


        if eta < eta_piu_giovane:
            eta_piu_giovane = eta
            calciatore_piu_giovane = giocatore
print("Il calciatore più giovane è:" , calciatore_piu_giovane,eta_piu_giovane)
