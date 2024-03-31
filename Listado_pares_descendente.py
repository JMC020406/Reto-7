#listado descendente de numero pares desde un n hasta el 2

n=int(input("Ingrese un numero natural: "))

print("Listado de numeros pares descendentemente desde "+str(n)+" hasta 2:")
print("INICIO")

while n>=2:
    if n % 2 == 0:
        print(n)
    n -= 1

print("FIN")
