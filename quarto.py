""" 
S1 base della botte
S2 superficie del cerchio massimo
S3 base della botte
h altezza
V volume della botte = 1/6 * h * (S1 + 4S2 + S3)
area di un cerchio S = pr**2 e p = 3.1415
r di S1 r1 = 30cm 
r di S2 r2 = 45cm
r di S3 r3 = 33cm
h = 130cm
? VOLUME DELLA BOTTE ?
Volume in LITRI
Leggere dimensioni da terminale (input)
"""

r1 = int(input("Inserisci il raggio della base superiore della botte: "))
r2 = int(input("Inserisci il raggio del cerchio massimo: "))
r3 = int(input("Inserisci il raggio della base inferiore: "))
h = int(input("Inserisci l'altezza della botte: "))
p = 3.1415
S1 = p * (r1 ** 2)
S2 = p * (r2 ** 2)
S3 = p * (r3 ** 2)

V = 1/6 * h * (S1 + (4 * S2) + S3)

litri = V/1000

print(litri)
