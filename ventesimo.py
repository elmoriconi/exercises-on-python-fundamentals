

def MCD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:  
            b = b - a    
    return a

a = int(input("Inserire il primo numero: "))
b = int(input("Inserire il secondo numero: "))
print(MCD(a, b))