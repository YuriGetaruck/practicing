import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani

baralho = ["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"Q","Q","Q","Q", "J","J","J","J", "K","K","K","K"]

contador = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

names = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

def anima_func():
    controle_while = True
    inteacoes = 0
    
    while controle_while:
        plt.cla()
        plt.clf()
        inteacoes += 1
        print("========================================================================================")
        contador
        print("contador = "+str(contador))
        random.shuffle(baralho)
        hand = [random.choice(baralho),random.choice(baralho)]
        print(hand)
        if((hand[0]=='A') and ((hand[1]==10) or (hand[1]=='Q') or (hand[1]=='J') or (hand[1]=='K'))):
            hand = [11,10]
        if((hand[1]=='A') and ((hand[0]==10) or (hand[0]=='Q') or (hand[0]=='J') or (hand[0]=='K'))):
            hand = [11,10]
        if((hand[0]=='A')):
            hand[0] = 11
        if((hand[1]=='A')):
            hand[1] = 11
        if((type(hand[0]) == str) and (type(hand[1]) == str)):
            hand = [10,10]
        if((type(hand[0]) == str) and (type(hand[1]) == int)):
            hand[0]= 10
        if((type(hand[0]) == int) and (type(hand[1]) == str)):
            hand[1]= 10
        soma = hand[0]+hand[1]
        print("soma = "+str(soma))

        if soma == 0:
            contador[0] += 1
        if soma == 1:
            contador[1] += 1
        if soma == 2:
            contador[2] += 1
        if soma == 3:
            contador[3] += 1
        if soma == 4:
            contador[4] += 1
        if soma == 5:
            contador[5] += 1
        if soma == 6:
            contador[6] += 1
        if soma == 7:
            contador[7] += 1
        if soma == 8:
            contador[8] += 1
        if soma == 9:
            contador[9] += 1
        if soma == 10:
            contador[10] += 1
        if soma == 11:
            contador[11] += 1
        if soma == 12:
            contador[12] += 1
        if soma == 13:
            contador[13] += 1
        if soma == 14:
            contador[14] += 1
        if soma == 15:
            contador[15] += 1
        if soma == 16:
            contador[16] += 1
        if soma == 17:
            contador[17] += 1
        if soma == 18:
            contador[18] += 1
        if soma == 19:
            contador[19] += 1
        if soma == 20:
            contador[20] += 1
        if soma == 21:
            contador[21] += 1

        if inteacoes == 1000:
            controle_while = False

        plt.ion()
        plt.stem(contador)
        plt.pause(0.001)
        
        

print(contador)
anima_func()
plt.pause(10)
plt.ioff()






    
