import random

interacoes = 0

contadorA = 0
contadorB = 0
contaodrEmpate = 0

v = range(10000000)

while True:

    a = random.choice(v)
    b = random.choice(v)

    interacoes = interacoes + 1

    if(a < b):
        contadorA = contadorA+1
    elif(a > b):
        contadorB = contadorB+1
    else:
        contaodrEmpate = contaodrEmpate+1

    if(interacoes %  100000 == 0):
        print("total de interaçoes: "+str(interacoes))
        print("A ganhou: "+str(contadorA)+" B ganhou: "+str(contadorB)+" e Empates: "+str(contaodrEmpate))
        print("deferença: "+str(contadorA-contadorB))
