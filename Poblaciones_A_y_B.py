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
