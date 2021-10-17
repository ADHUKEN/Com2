from math import e, sqrt
import random
from re import I
import numpy as np
from numpy.core.arrayprint import printoptions

from numpy.lib.function_base import append


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def Encryptdef(String):
    global KeyMatrix 
    KeyMatrix = []
    global Encrypt 
    Encrypt = []
    global opr 
    opr = []
    for char in String:
        numbers = alphabet.find(char.upper())
        print(numbers)
        x = random.randint(1,10)
        suma = numbers + x
        resta = numbers - x
        multi = numbers * x
        KeyMatrix.append(x)


        operations = [suma,resta,multi]
        y =  random.sample(operations,1)
        z = operations.index(y[0])
        opr.append(z)
        print(y,x,operations,z)
        Encrypt.append(y[0])
    
    KeyMatrix = np.array(KeyMatrix)
    Encrypt = np.array(Encrypt)
    opr = np.array(opr)
    print(KeyMatrix)
    print(Encrypt)
    print(opr)

    strEncrypted = ''.join(str(e) for e in Encrypt)
    print(strEncrypted)
    return strEncrypted

opr_res = []
numbers = []


def DesEncrypt(KeyMatrix, Encrypt):

    for c in opr: 
        if c==0:
            letter = Encrypt - KeyMatrix

        elif c==1:
            letter = Encrypt + KeyMatrix

        elif c==2:
            letter = Encrypt / KeyMatrix

        opr_res.append(letter)

    for y in range(len(opr)):
        numbers.append(alphabet[int(opr_res[y][y])])
    print(numbers)
    LettersStr = ''.join(numbers)
    print(LettersStr)
    return LettersStr

print(Encryptdef("hola maestro como esta xd"))
print(DesEncrypt(KeyMatrix,Encrypt))
    

