import random
import numpy as np
from matplotlib import pyplot as plt

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
        print("contador = "+str(contador)+str(contador.count(all)))
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
        
        contador[soma]+=1
        
        if inteacoes == 100:
            controle_while = False

        plt.ion()
        plt.stem(contador)
        plt.pause(0.0000001)
        
        

print(contador)
anima_func()
plt.pause(10)
plt.ioff()
