dividendo=int(input("Ingrese un numero natural del 2 al 50: "))
divisor:int=1

print("Los divisores del numero "+str(dividendo)+" son:")

while dividendo>=2 and dividendo<=50:
    if dividendo%divisor == 0:
        print(divisor)
    divisor += 1

print("FIN")