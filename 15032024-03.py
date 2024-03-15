import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

print(len(worldcup))

print(worldcup[1200])
print(worldcup[1200]['DateOfBirth'])


# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) Contare quanti calciatori hanno giocato per l'Italia
# 2) Contare quanti calciatori hanno giocato per il Brasile
# 3) Contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

#Conta quanti calciatori per ogni squadra. La key è team e il value è il numero di calciatori 
quanticalciatori = dict()
for v in worldcup:
    # se i["Team"] è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in quanticalciatori.keys():
        quanticalciatori[v["Team"]] = quanticalciatori[v["Team"]]+1
    else:
        quanticalciatori[v["Team"]] = 1
