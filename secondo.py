from math import sqrt

print("ipotenusa = ", sqrt((10.123 ** 2) + (30.456 ** ")))
                                           
# in alternativa ho provato 
                                           
from math import sqrt
                                           
float c = 0
a = 10.123 ** 2
b = 30.456 ** 2
c = a + b

print(sqrt(c))

# oppure (quello giusto)

import math

cateto1 = 10123
cateto2 = 30.456

ipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(ipotenusa)

# quello che dice chatgpt

import math

def calcola_ipotenusa(cateto1, cateto2):
  ipotenusa = math.sqrt(cateto1*2 + cateto2*2)
  return ipotenusa

cateto1 = 10.123
cateto2 = 30.456
ipotenusa = calcola_ipotenusa(cateto1, cateto2)

print( "L'ipotenusa del triangolo rettangolo è:", ipotenusa)
                                                                                  

