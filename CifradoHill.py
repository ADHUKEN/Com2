import math
import numpy as np

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NoLetras = 26

def LettersToMatrix(str):
    str = str.upper().strip().replace(" ", "")

    FullVector = []
    for x in str:
        des = alphabet.find(x.upper())  # Encuentra la posicion de alphabet
        FullVector.append(des)
    arr = np.array(FullVector)

    global length
    length = int(len(arr)/2)
#
    if len(arr)/2 > length:  # añade una letra si no es par
        length = length + 1
        newarray = np.insert(arr, length+1, 0)
        arr = newarray.reshape(length, 2).transpose()
    else:
        arr = arr.reshape(length, 2).transpose()

    return arr

def MatrixtoLetters(Matrix):
    LettersVector = []
    for q in Matrix:  # se opera para numero menor de NoLetras
        q = q % NoLetras
        letterpositions = alphabet[int(q)]
        LettersVector.append(letterpositions)
        LettersStr = "".join(LettersVector)
    return LettersStr

# Encriptacion----------------------------------

def Encrypt(str,KeyMatrix):
    EncryptedMatrix = np.matmul(KeyMatrix, LettersToMatrix(str)).transpose(
    ).reshape(-1) % NoLetras  # multiplicaion de matrices
    return MatrixtoLetters(EncryptedMatrix)


# Desencriptacion----------------------------------


def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return int(x)

def DesEncrypt (str,KeyMatrix):

  EncryptedMatrix =LettersToMatrix(str)

  detmod26 = int(np.linalg.det(KeyMatrix)) % NoLetras

  KeyMatrixTrans = (modInverse(int(detmod26), NoLetras) *
                     (np.linalg.inv(KeyMatrix).T * np.linalg.det(KeyMatrix)).transpose())

  DesEcryptedMatrix = np.matmul(KeyMatrixTrans %
                                NoLetras, EncryptedMatrix).transpose().reshape(-1) % NoLetras
  return MatrixtoLetters(DesEcryptedMatrix)

