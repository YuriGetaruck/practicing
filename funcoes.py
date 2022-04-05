import math
from posixpath import split
import string

volume_esfera = lambda x:(4/3)*math.pi*x**3

print(volume_esfera(4))

def ran_check(num, low, max):
    if(num >= low and num <= max):return True
    else: return False

print(ran_check(1,2,5))

def up_low(s):
    Ma = 0
    Mi = 0
    for C in s:
        if C.isupper():
            Ma += 1
        elif C.islower():
            Mi += 1
        else:
            pass
    
    print(Ma)
    print(Mi)

up_low("Teste de contagem")


def unique_list(s):
    return set(s)

print(unique_list([1,2,3,4,5,1,2,5,4,3,2]))

def multiplica_numvetor(v):
    aux = 1
    for i in v:
        aux = aux * i

    return aux

print(multiplica_numvetor([1,2,3,4,5]))
#print(math.factorial(5))

def palindrome(s):
    if(s == s[::-1]):
        print("é palindrome")
    else:
        print('nao é palindrome')

palindrome('subinoonibus')


def ispangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram('The quick brown fox jumps over the lazy dog'))

        