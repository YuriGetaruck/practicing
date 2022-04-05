#Black jack game on terminal

import random

baralho = ["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"Q","Q","Q","Q", "J","J","J","J", "K","K","K","K"]

random.shuffle(baralho)

class player(object):
    
    def __init__(self):
        self.hand = [0,0]

    def valordamao(self):
        if((self.hand[0]=='A') and ((self.hand[1]==10) or (self.hand[1]=='Q') or (self.hand[1]=='J') or (self.hand[1]=='K'))):
            self.hand = [11,10]
        if((self.hand[1]=='A') and ((self.hand[0]==10) or (self.hand[0]=='Q') or (self.hand[0]=='J') or (self.hand[0]=='K'))):
            self.hand = [11,10]
        if((self.hand[0]=='A')):
            self.hand[0] = 11
        if((self.hand[1]=='A')):
            self.hand[1] = 11
        if((type(self.hand[0]) == str) and (type(self.hand[1]) == str)):
            self.hand = [10,10]
        if((type(self.hand[0]) == str) and (type(self.hand[1]) == int)):
            self.hand[0]= 10
        if((type(self.hand[0]) == int) and (type(self.hand[1]) == str)):
            self.hand[1]= 10
        if((type(self.hand[0]) == int) and (type(self.hand[1]) == int)):
            return(self.hand[0]+self.hand[1])

    def receviCards(self):
        self.hand = [random.choice(baralho),random.choice(baralho)]

    def hit():
        pass

    def stand():
        pass

class dealer():

    def __init__(self):
        pass

p = player()

p.receviCards()

print(p.valordamao)