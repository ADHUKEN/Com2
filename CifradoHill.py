import math
import numpy as np

print("Hola Amigos")

toEncode = str(input("Frase a encriptar: "))
#toEncode = "tre"
toEncode = toEncode.upper().strip().replace(" ","")

print(toEncode)


FullVector = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in toEncode:
    des = alphabet.find(x.upper()) #Encuentra la posicion de alphabet
    print(x,des)
    FullVector.append(des)
arr = np.array(FullVector)
print(FullVector)


completmatrix = np.array([26])
 # imprimir el vector



length = int(len(arr)/2)
print(len(arr))
#
#
if len(arr)/2 > length: # añade una letra si no es par
  print("se pasa")
  length = length + 1
  newarray = np.hstack((arr, completmatrix))
  arr = newarray.reshape(length,2)
else:
  arr = arr.reshape(length,2)


arrFinal = arr.transpose()
print(arr)
print(arrFinal)


MatrixBase = np.array([[5,4],[21,5]])


print("Matriz llave\n",MatrixBase, "\n")


result = np.matmul(MatrixBase,arrFinal) # multiplicaion de matrices
print("Matriz multiplicada\n",result)

result = result.transpose()
EncryptVector = result.reshape(-1)

print(EncryptVector)

Encrypted=[]

for q in EncryptVector: # se opera para numero menor de 26
    if q > 26:
      n = int(q/26)
      q = q-26*n
    letterposition = alphabet[q]
    Encrypted.append(letterposition)
    print(q,letterposition)

EncryptedStr="".join(map(str,Encrypted))
print(EncryptedStr)
