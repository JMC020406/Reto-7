# Listado primos del 1 al 100: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97 ; 25 primos 

limite=int(input("Ingrese hasta el numero que quiera saber la cantidad de primos que hay: "))
num:int=1
div:int=2
cont = 1 

if num == 1:
    num += 1
    print(num) 

elif num == 2:
    num += 1

while num < limite:
    if num%div != 0:
        if div < num-1:
            div += 1

        elif div == num-1:
            div = 2
            print(num)
            num += 1
            cont += 1

    elif num%div == 0:
        num += 1
        div = 2

print("Cantidad primos:"+str(cont))