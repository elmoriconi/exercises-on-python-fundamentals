numero = ""
i = 0
while True:
    c = input("Digita 0-9,+-*/=: ")
    if len(c) > 0:
        c = c[0]
    if len(c) == 0:
        continue
    # dovete leggere un numero sia intero, sia decimale
    # e stamparlo nella sua interezza quando viene
    # digitato un simbolo non numerico (+-*/=)
    # se legge più di una "," deve dare errore
    if c == ",":
        i += 1
    if i > 1:
        print("Non è un numero")
    # Terminerete quando varrà la
    if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
        #se legge più di una "," , deve dare errore
        # Stampate il numero letto
        print("Il numero è: ", numero)
        break
    else:
        #costruzione del numero...
        numero = numero + c 