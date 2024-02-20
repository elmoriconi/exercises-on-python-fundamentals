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