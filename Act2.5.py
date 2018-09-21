import math
print("Escribe el radio A: ")
A=input()
print("Escribe el radio B: ")
B=input()
A=float(A)
B=float(B)
C=math.pi*math.sqrt(2**2*(A+B)**2)

print("Circunferencia: "+str(C))
