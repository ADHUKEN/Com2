import CifradoHill as Hill
from Hamming128 import *
import numpy as np

from Envio import send


print("\n")

#to Encode = 
print("Mensaje Recibido:" ,send)


MatrizLlave = np.array([[17, 22], [9, 13]])  # matriz llave


print("DesEncriptacion Hill Sin Hamming: ",Hill.DesEncrypt(send,MatrizLlave))

print("\n")
Recieve = Hamming(Hill.DesEncrypt(send,MatrizLlave))


print("DesEncriptacion Hill Con Hamming: ",Recieve)
print("\n")
