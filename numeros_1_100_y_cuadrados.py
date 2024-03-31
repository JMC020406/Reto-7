def cuadradonumero (i=int)->int:
    return (i**2)

#numero del 1 al 100 y sus cuadrados

if __name__ == "__main__":

    i:int=1

print("Lista de numeros del 1 al 100 y sus cuadrados:")
print("INICIO")

while i<=100:
    cuadrado=cuadradonumero(i)
    print(str(i)+" , "+str(cuadrado))
    i+=1

print ("FIN")
