from hashlib import new
from os import error
import random
import math
from re import A

from numpy.lib.function_base import insert
from sympy import *
import numpy as np

from operator import *

def toBinary(String):
    BinConvert = np.array([(format(ord(char), '#010b')[2:]) for char in String])

    return BinConvert


def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

def binaryToDecimal(n):
    return int(n, 2)




def Hamming(Str):
    Bin = toBinary(Str)

    set = []
    for y in Bin:
        for b in y:
            set.append(b)
    fullarr = np.array(set)

    newarr = np.array_split(fullarr, len(Bin))




    for c in range(len(Bin)):
        a1 = int(newarr[c][7])
        a2 = int(newarr[c][6])
        a3 = int(newarr[c][5])
        a4 = int(newarr[c][4])
        a5 = int(newarr[c][3])
        a6 = int(newarr[c][2])
        a7 = int(newarr[c][1])
        a8 = int(newarr[c][0])

        P0 = a1+a2+a4+a5+a7
        P1 = a1+a3+a4+a6+a7
        P2 = a2+a3+a4+a8
        P3 = a5+a6+a7+a8

        if (P0 % 2):
            P0 = 1
        else:
            P0 = 0
        if (P1 % 2):
            P1 = 1
        else:
            P1 = 0
        if (P2 % 2):
            P2 = 1
        else:
            P2 = 0
        if (P3 % 2):
            P3 = 1
        else:
            P3 = 0

        newarr[c] = np.insert(newarr[c], (4, 7, 8, 8), (P3, P2, P1, P0))

        d1 = int(newarr[c][11])
        d2 = int(newarr[c][10])
        d3 = int(newarr[c][9])
        d4 = int(newarr[c][8])
        d5 = int(newarr[c][7])
        d6 = int(newarr[c][6])
        d7 = int(newarr[c][5])
        d8 = int(newarr[c][4])
        d9 = int(newarr[c][3])
        d10 = int(newarr[c][2])
        d11 = int(newarr[c][1])
        d12 = int(newarr[c][0])

        xorP0 = d1 ^ d3 ^ d5 ^ d7 ^ d9 ^ d11 
        xorP1 = d2 ^ d3 ^ d6 ^ d7 ^ d10 ^ d11 
        xorP2 = d4 ^ d5 ^ d6 ^ d7 ^ d12 
        xorP3 = d8 ^ d9 ^ d10 ^ d11 ^ d12 


    error = np.random.randint(2)
    position = np.random.randint(12)

    noerrorarr = np.array(newarr[0])



    np.put(newarr[0], [position], [error])

    if newarr[0][position] != noerrorarr[position]:
        print("Error hallado en posicion:", 12-position)
    else:
        print("NO HAY ERROR")



    d1 = int(newarr[0][11])
    d2 = int(newarr[0][10])
    d3 = int(newarr[0][9])
    d4 = int(newarr[0][8])
    d5 = int(newarr[0][7])
    d6 = int(newarr[0][6])
    d7 = int(newarr[0][5])
    d8 = int(newarr[0][4])
    d9 = int(newarr[0][3])
    d10 = int(newarr[0][2])
    d11 = int(newarr[0][1])
    d12 = int(newarr[0][0])

    xorP0 = str(d1 ^ d3 ^ d5 ^ d7 ^ d9 ^ d11 )
    xorP1 = str(d2 ^ d3 ^ d6 ^ d7 ^ d10 ^ d11 )
    xorP2 = str(d4 ^ d5 ^ d6 ^ d7 ^ d12 )
    xorP3 = str(d8 ^ d9 ^ d10 ^ d11 ^ d12 )

    xor_position = xorP3+xorP2+xorP1+xorP0





    decimal_position_xor = binaryToDecimal(xor_position)
    int_xor_position = int(decimal_position_xor)
    posicion_error_array= 12-int_xor_position

    if posicion_error_array == 12:
        posicion_error_array = 0




    if int(int_xor_position) > 0:
        if int(newarr[0][posicion_error_array]) == 0:
            np.put(newarr[0], [posicion_error_array], [1])
        elif int(newarr[0][posicion_error_array]) == 1:
            np.put(newarr[0], [posicion_error_array], [0])


    FINALset = []
    for c in range(len(Bin)):


        FINALnewarr = np.delete(newarr[c], [4,8,10,11])
 
        FINALset.append(FINALnewarr)
        FINALfullarr = np.array(FINALset).reshape(-1)
        ascii_final = "".join(FINALfullarr)



    

    return toString(ascii_final)
    
