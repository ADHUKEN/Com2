import math
import numpy as np
print("Hola Amigos")

toEncode = str(input("Frase a encriptar: "))
#toEncode = "help"
toEncode = toEncode.upper().strip().replace(" ", "")

print(toEncode)


FullVector = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in toEncode:
    des = alphabet.find(x.upper())  # Encuentra la posicion de alphabet
    print(x, des)
    FullVector.append(des)
arr = np.array(FullVector)
print(FullVector)

NoLetras = 26

completmatrix = np.array([NoLetras])
# imprimir el vector


length = int(len(arr)/2)
print(len(arr))
#
#
if len(arr)/2 > length:  # añade una letra si no es par
    print("se pasa")
    length = length + 1
    newarray = np.hstack((arr, completmatrix))
    arr = newarray.reshape(length, 2)
else:
    arr = arr.reshape(length, 2)


arrFinal = arr.transpose()
print(arr)
print(arrFinal)


MatrixBase = np.array([[17, 22], [9, 13]])  # matriz llave


print("Matriz llave\n", MatrixBase, "\n")


result = np.matmul(MatrixBase, arrFinal)  # multiplicaion de matrices
print("Matriz multiplicada\n", result)

result = result.transpose()
EncryptVector = result.reshape(-1)

print(EncryptVector)

Encrypted = []
EncryptedVectormod = []


for q in EncryptVector:  # se opera para numero menor de NoLetras
    q = q % NoLetras
    letterposition = alphabet[q]
    Encrypted.append(letterposition)
    EncryptedVectormod.append(q)
    print(q, letterposition)

print(Encrypted)
print(EncryptedVectormod)

EncryptedMatrix = np.array(EncryptedVectormod).reshape(length, 2).transpose()


# Encriptacion Completa variable a exportar
EncryptedStr = "".join(map(str, Encrypted))

print(EncryptedStr)


# Desencriptacion----------------------------------
print("desencriptacion--------------")

def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return int(x)

detmod26 = int(np.linalg.det(MatrixBase)) % NoLetras

print(detmod26)


print(modInverse(int(detmod26), NoLetras))


MatrixBaseTrans = (modInverse(int(detmod26), NoLetras) *
                   (np.linalg.inv(MatrixBase).T * np.linalg.det(MatrixBase)).transpose())

print(MatrixBaseTrans)

print("mod26")


print(MatrixBaseTrans % NoLetras)

print(EncryptedMatrix)

DesEcryptedMatrix = np.matmul(MatrixBaseTrans %
                              NoLetras, EncryptedMatrix).transpose().reshape(-1)


print(DesEcryptedMatrix)


DesEncrypted = []

for q in DesEcryptedMatrix:  # se opera para numero menor de NoLetras
    q = q % NoLetras
    letterpositionDes = alphabet[int(q)]
    DesEncrypted.append(letterpositionDes)
    print(int(q), letterpositionDes)

DesEncryptedStr = "".join(map(str, DesEncrypted))

print(DesEncryptedStr)
