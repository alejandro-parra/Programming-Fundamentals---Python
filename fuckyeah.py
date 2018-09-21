import math
archivo=None

try:
    archivo=open("Dummy.txt")
except IOError:
    print("Error, no se puede abrir el archivo men")

if archivo:
    
