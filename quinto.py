#In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente: Antonio, Marco, Andrea, Luigi, Tony, Bruno,
#Laura, Anita, Annarita, Lucia. Le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone: John, 
#Alice, Mary. Altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire). 
#Stampare l'elenco delle persone presenti.
#Infine, stampare le persone presenti in ordine alfabetico

persone = ["Antonio", "Marco", "Andrea", "Luigi", "Tony", "Bruno","Laura", "Anita", "Annarita", "Lucia"]
persone.pop(0)
persone.pop(0)
persone.append("John")
persone.append("Alice")
persone.append("Mary")
persone.pop(0)
persone.pop(0)
print(persone)
persone.sort()
print(persone)