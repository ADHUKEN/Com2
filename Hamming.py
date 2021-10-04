from hashlib import new
from os import error
import random
import math
from re import A

from numpy.lib.function_base import insert
from sympy import *
import numpy as np

from operator import *


# PrimaryBits = list(input("4 bits plox: "))
# PrimaryBits = [0,1,0,1,0,1,0]


# print(PrimaryBits)


# 2^x =>x + bits +1

# defining symbols used in equations

# x = (symbols('x'))


# defining equations
# Powresult = nsolve(2**x - x - 250 - 1, x ,1,verify=False)

# print(Powresult)

def toBinary(String):
    BinConvert = np.array([(format(ord(char), '#010b')[2:]) for char in String])

    return BinConvert


def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

def binaryToDecimal(n):
    return int(n, 2)

print("Hola maestro")


def Hamming(Str):
    Bin = toBinary(Str)

    set = []
    for y in Bin:
        for b in y:
            set.append(b)
    fullarr = np.array(set)
    print(fullarr)
    newarr = np.array_split(fullarr, len(Bin))

    for c in range(len(Bin)):
        print(newarr[c])

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

        print("P--", P0, P1, P2, P3, "Xor--", xorP0, xorP1, xorP2, xorP3)

    print("--------------------------------")

    for c in range(len(Bin)):
        error = np.random.randint(2)
        position = np.random.randint(12)
        print("error aleatorio: insertar", error, "en posicion desde la izquierda con 0: ", position)

        noerror_arr = np.array(newarr[c])
        print(noerror_arr)  
        np.put(newarr[c], [position], [error])
        print("original")
        print(newarr[c])
        
        
        if newarr[c][position] != noerror_arr[position]:
            print("eror hayado xd en: ", 12-position)
        else:
            print("NO HAY ERROR")


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

        xorP0 = str(d1 ^ d3 ^ d5 ^ d7 ^ d9 ^ d11 )
        xorP1 = str(d2 ^ d3 ^ d6 ^ d7 ^ d10 ^ d11 )
        xorP2 = str(d4 ^ d5 ^ d6 ^ d7 ^ d12 )
        xorP3 = str(d8 ^ d9 ^ d10 ^ d11 ^ d12 )

        xor_position = xorP3+xorP2+xorP1+xorP0
        print("valores xor(posicion error)", xorP3, xorP2, xorP1, xorP0, xor_position)

        print("correccion de error")




        decimal_position_xor = binaryToDecimal(xor_position)
        print(decimal_position_xor)
        int_xor_position = int(decimal_position_xor)
        posicion_error_array= 12-int_xor_position

        if posicion_error_array == 12:
            posicion_error_array = 0


        print("Sustituir: ", newarr[c][posicion_error_array])


        if int(int_xor_position) > 0:
            if int(newarr[c][posicion_error_array]) == 0:
                np.put(newarr[c], [posicion_error_array], [1])
                print("por 1")
            elif int(newarr[c][posicion_error_array]) == 1:
                np.put(newarr[c], [posicion_error_array], [0])
                print("por 0")

        print("-----------------------------------------------corregido xd")

    FINALset = []
    for c in range(len(Bin)):

        print(newarr[c])
        FINALnewarr = np.delete(newarr[c], [4,8,10,11])
        print(FINALnewarr)    
        FINALset.append(FINALnewarr)
        FINALfullarr = np.array(FINALset).reshape(-1)
        ascii_final = "".join(FINALfullarr)

    print(ascii_final) 

    

    return toString(ascii_final)
    
print("MENSAJE FINAL CORREGIDO :",Hamming("Hola"))
