# Reto-7
## Bucles 1
Los bucles son un recurso de python el cual nos permite analizar un valor en varias ocasiones hasta que ya deje de cumplir una condición.

Para este reto habian un total de 8 puntos los cuales variaban en su dificultad mucho a mi parecer. Pero aquí estan los 8 puntos y los tres diagramas de flujo para los correspondientes tres primeros.

### Punto 1 / Listado del 1 al 100 y sus cuadrados
```py
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
```
#### Diagrama de flujo 1
```mermaid
graph TD;
  A(INICIO)-->B(i=1)
  B-->Z(Definir la funcion cuadrado)
  Z-->C{¡Es i<100?}
  C-->|si|D(Aplicar la funcion cuadrado)
  D-->E(Regresar los valores de i y su cuadrado)
  E-->F(i = i+1)
  F-->C
  C-->|no|G(FIN)
```

### Punto 2 / Listado Pares e Impares del 1 al 1000
```py
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
```
#### Diagrama de flujo 2
```mermaid
graph TD;
  A(INICIO)-->B(i=1)
  B-->C{¿Es i<1000?}
  C-->|si|D{¿Es i%2 == 0?}
  D-->|si|E(i va a la lista de pares)
  D-->|no|F(i va a la lista de impares)
  E-->G(i = i+1)
  F-->G(i = i+1)
  G-->C
  C-->|no|H(FIN)
```

### Punto 3 / Listado descendente de numeros pares hasta el 2
```py
#listado descendente de numero pares desde un n hasta el 2

n=int(input("Ingrese un numero natural: "))

print("Listado de numeros pares descendentemente desde "+str(n)+" hasta 2:")
print("INICIO")

while n>=2:
    if n % 2 == 0:
        print(n)
    n -= 1

print("FIN")
```
#### Diagrama de flujo 3
```mermaid
graph TD;
  A(INICIO)-->B(Definir n)
  B-->Z{¿Es n > = 2?}
  Z-->|si|C{¿Es n%2 == 0?}
  C-->|si|D(Escribir valor de n)
  C-->|no|E(n = n-1)
  D-->E
  E-->Z
  Z-->|no|F(FIN)
```

### Punto 4 / Población del país A y B
Este punto necesita un poco de explicación. Hay dos paises, cada uno con un porcentaje de crecimiento anual, los cuales son: 2% para el país A y 3% para el país B. El país A tiene una población de 25 millones de personas, mientras que el B tiene 18.9 millones. El tema es ¿Cuándo el país B rebasara al país A en población con respecto a años?
```py
def crecimiento_A(poblacionA=int)->int:
    return (poblacionA*(2/100))

def crecimiento_B(poblacionB=int)->int:
    return (poblacionB*(3/100))

if __name__ == "__main__":

    poblacionA:int=25000000
    poblacionB:int=18900000
    i:int=1

    crecimientoA=crecimiento_A(poblacionA)
    crecimientoB=crecimiento_B(poblacionB)

while poblacionA > poblacionB:
    poblacionA += crecimientoA
    poblacionB += crecimientoB
    i += 1

print("En el año en el que la poblacion B pasa a la poblacion A es en el año "+str(i)+" donde la poblacion B es de "+str(poblacionB)+" y la de A es de "+str(poblacionA))
```

Como se puede apreciar se tiene definido dos funciones, las cuales son los crecimientos poblacionales de cada país, las poblaciones, que es lo que vamos a usar como base del programa, y los años, lo cual esta denominado como i en el programa y que cada vez que se genera un ciclo va aumentando una unidad.

### Punto 5 / El factorial de un número n
```py
num=int(input("Ingrese el numero natural del cual quiere saber su factorial: "))
i:int=1
factorial:int=1

while i <= num:
    factorial *= i
    i += 1

print("El factorial de "+str(num)+" es "+str(factorial))
```

### Punto 6 / Adivinanza de un número del 1 al 100
```py
pregunta_1 : bool = 0
adivinanza : int = 50
limite_inferior: int = 1
limite_superior: int = 100

bandera : bool = True
while bandera or pregunta_1 != 0: 
  bandera = False
  pregunta_1 = int(input("Es "+str(adivinanza)+" tu numero? SI = 0 , ES MAYOR = 1 y ES MENOR = 2: "))
  if pregunta_1 == 1 and (limite_superior - limite_inferior) > 10:
    limite_inferior = adivinanza
    adivinanza += 9
  elif pregunta_1 == 1 and (limite_superior - limite_inferior) < 10:
    limite_inferior = adivinanza
    adivinanza += 1
  elif pregunta_1 == 2 and (limite_superior - limite_inferior) > 10:
    limite_superior = adivinanza
    adivinanza -= 8
  elif pregunta_1 == 2 and (limite_superior - limite_inferior) < 10:
    limite_superior = adivinanza
    adivinanza -= 1

print("Tu numero es el "+str(adivinanza))
```
Lo que hice en este punto fue usar el tipo de ciclo *do while* el cual se puede crear usando una bandera (como esta en este código) o la palabra reservada *break*.

Para resolver el problema primero definí 4 variables: la primera es la pregunta que se va a preguntar todo el rato, la cual es si el numero mencionado es el tuyo o es mayor o menor del cual se esta hablando, luego definí el valor inicial de la adivinanza el cual es 50, ya que era un punto medio entre el 1 y el 100, y por último definí dos variables las cuales me ayudaran a controlar el crecimiento o decrecimiento de la adivinanza, así pues si el numero se encuentra a un extremo del rango no tendre complicaciones en alcanzarlo.

Una vez definidas esas cuatro variables empece a codificar el ciclo *do while* co una bandera y seguido de eso coloque la pregunta primordial para que funcione el ciclo. Luego definí que se hace dependiendo de que se elija en esa pregunta, y como se puede notar uso los limites, como antes mencione, para controlar el crecimiento y decrecimiento de la adivinanza.

Y por último lo que hice fue colocar la instrucción para que aparezca el número elegido por el observador.

### Punto 7 / Divisores de un número del 2 al 50
```py
dividendo=int(input("Ingrese un numero natural del 2 al 50: "))
divisor:int=1

print("Los divisores del numero "+str(dividendo)+" son:")

while dividendo>=2 and dividendo<=50:
    if dividendo%divisor == 0:
        print(divisor)
    divisor += 1

print("FIN")
```

### Punto 8 / Listado de números primos del 1 al 100
```py
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
```
En este punto se habia especificado que se tenia que hacer con funciones, pero preferí hacerlo a mi manera y hacerlo de la manera tradicional de condiciones y operaciones matematicas; pero si es necesario lo que se puede hacer es cambiar el calculo de división por una función que represente lo mismo.

Y como notas: el limite determina hasta que numero se va a analizar, la variable num y div son los que iran analizando los valores de todos los numeros enteros entre 1 y el limite, y por ultimo cont significa contador, que es el total de numeros primos que hay entre el 1 y el limite definido.
