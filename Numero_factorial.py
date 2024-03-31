#Numero factorial

num=int(input("Ingrese el numero natural del cual quiere saber su factorial: "))
i:int=1
factorial:int=1

while i <= num:
    factorial *= i
    i += 1

print("El factorial de "+str(num)+" es "+str(factorial))
