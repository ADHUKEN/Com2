import CifradoHill as Hill
from Hamming128 import *
import numpy as np

print("\n")

#to Encode = 
toEncode = "Hola"
print("Mensaje a Enviar:" ,toEncode)
#Eleccion del metodo de encriptacion
#Cesar,Hill,Propio

#Conexion inalambrica



MatrizLlave = np.array([[17, 22], [9, 13]])  # matriz llave


print("Encriptacion Hill Sin Hamming: ",Hill.Encrypt(toEncode,MatrizLlave))

print("\n")
send = Hamming(Hill.Encrypt(toEncode,MatrizLlave))


print("Encriptacion Hill Con Hamming: ",send)
print("\n")
