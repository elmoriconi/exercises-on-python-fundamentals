a = 10
b = 20
c = 30

if a % 2 == 0:
    print(b+c)
else:
    print(b-c)

#si poteva scrivere anche con gli operatori booleani: 
#if a & 1 == 0:

#terzo modo:
# if math.floor(a/2)*2 == a
#che significa? esempio: 7/2 = 3,5 => prendo solo la parte intera
# 3 * 2 = 6. 6 == 7 ? no, quindi dispari