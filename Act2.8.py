import math
print("Dame la altura de la escalera: ")
a=input()
print("Dame el ángulo de inclinación de la escalera: ")
g=input()
a=float(a)
g=float(g)
r=g*math.pi/180
l=a/math.sin(r)

print("El largo de la escalera es: "+str(l))
