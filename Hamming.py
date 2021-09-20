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

    arr = []
    for x in BinConvert:
        x = "000"+x
        arr.append(x)
    Total = np.array(arr)
    return Total


Bin = toBinary("fajsdklfj asdjf aksñdlfkaj sdkfj alskdñjfak sdjfkasldk jgoriuja irauifhurhf dcj dncudcnuencue cenucn e ceunc ecnu amalsdkfjasdfjaej hfeh fa")

print(Bin)

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
    a1 = int(newarr[c][10])
    a2 = int(newarr[c][9])
    a3 = int(newarr[c][8])
    a4 = int(newarr[c][7])
    a5 = int(newarr[c][6])
    a6 = int(newarr[c][5])
    a7 = int(newarr[c][4])
    a8 = int(newarr[c][3])
    a9 = int(newarr[c][2])
    a10 = int(newarr[c][1])
    a11 = int(newarr[c][0])

    P0 = a1+a2+a4+a5+a7+a9+a11
    P1 = a1+a3+a4+a6+a7+a10+a11
    P2 = a2+a3+a4+a8+a9+a10+a11
    P3 = a5+a6+a7+a8+a9+a10+a11

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

    #print("P0: ", P0,"|P1: ", P1,"|P2: " ,P2,"|P3: ", P3)
    #print("xorP0: ", xorP0,"|xorP1: ", xorP1,"|xorP2: " ,xorP2,"|xorP3: ", xorP3)
    newarr[c] = np.insert(newarr[c], (7, 10, 11, 11), (P3, P2, P1, P0))

    d1 = int(newarr[c][14])
    d2 = int(newarr[c][13])
    d3 = int(newarr[c][12])
    d4 = int(newarr[c][11])
    d5 = int(newarr[c][10])
    d6 = int(newarr[c][9])
    d7 = int(newarr[c][8])
    d8 = int(newarr[c][7])
    d9 = int(newarr[c][6])
    d10 = int(newarr[c][5])
    d11 = int(newarr[c][4])
    d12 = int(newarr[c][3])
    d13 = int(newarr[c][2])
    d14 = int(newarr[c][1])
    d15 = int(newarr[c][0])

    xorP0 = d1 ^ d3 ^ d5 ^ d7 ^ d9 ^ d11 ^ d13 ^ d15
    xorP1 = d2 ^ d3 ^ d6 ^ d7 ^ d10 ^ d11 ^ d14 ^ d15
    xorP2 = d4 ^ d5 ^ d6 ^ d7 ^ d12 ^ d13 ^ d14 ^ d15
    xorP3 = d8 ^ d9 ^ d10 ^ d11 ^ d12 ^ d13 ^ d14 ^ d15

    print("P--", P0, P1, P2, P3, "Xor--", xorP0, xorP1, xorP2, xorP3)

error = np.random.randint(2)
position = np.random.randint(15)

noerrorarr = np.array(newarr[0])


print("error aleatorio: insertar", error, "en posicion: ", position)

np.put(newarr[0], [position], [error])

if newarr[0][position] != noerrorarr[position]:
    print("eror hayado xd en: ", 15-position)
else:
    print("NO HAY ERROR")

print("original")
print(noerrorarr)
print(newarr[0])

d1 = int(newarr[0][14])
d2 = int(newarr[0][13])
d3 = int(newarr[0][12])
d4 = int(newarr[0][11])
d5 = int(newarr[0][10])
d6 = int(newarr[0][9])
d7 = int(newarr[0][8])
d8 = int(newarr[0][7])
d9 = int(newarr[0][6])
d10 = int(newarr[0][5])
d11 = int(newarr[0][4])
d12 = int(newarr[0][3])
d13 = int(newarr[0][2])
d14 = int(newarr[0][1])
d15 = int(newarr[0][0])

xorP0 = str(d1 ^ d3 ^ d5 ^ d7 ^ d9 ^ d11 ^ d13 ^ d15)
xorP1 = str(d2 ^ d3 ^ d6 ^ d7 ^ d10 ^ d11 ^ d14 ^ d15)
xorP2 = str(d4 ^ d5 ^ d6 ^ d7 ^ d12 ^ d13 ^ d14 ^ d15)
xorP3 = str(d8 ^ d9 ^ d10 ^ d11 ^ d12 ^ d13 ^ d14 ^ d15)

xor_position = xorP3+xorP2+xorP1+xorP0
print("valores xor(posicion error)", xorP3, xorP2, xorP1, xorP0, xor_position)

print("correccion de error")


def binaryToDecimal(n):
    return int(n, 2)

decimal_position_xor = binaryToDecimal(xor_position)
int_xor_position = int(decimal_position_xor)
posicion_error_array= 15-int_xor_position

if posicion_error_array == 15:
    posicion_error_array = 0


print("a trabajar", newarr[0][posicion_error_array])


if int(int_xor_position) > 0:
    if int(newarr[0][posicion_error_array]) == 0:
        np.put(newarr[0], [posicion_error_array], [1])
        print("sustituido por 1")
    elif int(newarr[0][posicion_error_array]) == 1:
        np.put(newarr[0], [posicion_error_array], [0])
        print("sustituido por 0")

print("corregido xd")

FINALset = []
for c in range(len(Bin)):

    print(newarr[c])
    FINALnewarr = np.delete(newarr[c], [0,1,2,7,11,13,14])
    print(FINALnewarr)    
    FINALset.append(FINALnewarr)
    FINALfullarr = np.array(FINALset).reshape(-1)
    ascii_final = "".join(FINALfullarr)

print(ascii_final) 


def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

print("MENSAJE FINAL CORREGIDO :",toString(ascii_final))
