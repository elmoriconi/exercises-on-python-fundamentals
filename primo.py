from math import asin, cos, sin
from math import radians, sqrt

print("Hello world")


print(10 * 10)
print(10 ** 10)
print(sqrt(10))


print("ipotenusa =", sqrt(10.123**2 + 30.456**2))

#oppure

import math 
                                        
a = 10.123 ** 2
b = 30.456 ** 2
c = a + b
ipotenusa = math.sqrt(c)

print(ipotenusa)


# calcolare la distanza tra Oslo (59.9°N 10.8°E) e Vancouver (49.3°N 123.1°W)
a1 = 59.9
b1 = 10.8
a2 = 49.3
b2 = -123.1
a1 = radians(a1)
a2 = radians(a2)
b1 = radians(b1)
b2 = radians(b2)
r = 6371
el1 = sin(1 / 2 * (a2 - a1)) ** 2
el2 = cos(a1) * cos(a2) * sin(1 / 2 * (b2 - b1)) ** 2
d = 2 * r * asin(sqrt(el1 + el2))

print("Distanza: ", d)

