#listado de numeros impares y pares

i:int=1

print("Listado de numeros impares del 1 hasta el 999:")
print("INICIO")

while i<1000:
    if i % 2 != 0:
        print(str(i))
    i += 1

print("FIN")

i -= 998

print("Listado de numeros pares del 2 hasta el 1000:")
print("INICIO")

while i<=1000:
    if i % 2 == 0:
        print(str(i))
    i += 1

print("FIN")