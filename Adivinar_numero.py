adivinanza:int=50
li:int=1
ls:int=100
pregunta_1:bool=False
pregunta_2:bool

band : bool = True
while band or pregunta_1 == True:
  band = False
  pregunta_1 = bool(input("Es "+str(adivinanza)+" tu numero? SI=True / NO/False: "))
  if pregunta_1 == True:
    break
  else: