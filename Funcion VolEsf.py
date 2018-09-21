import math
print("Escribe el radio deseado: ")
r=input()
r=float(r)

def volumen (r):
    a=4*math.pi*(r**2)
    v=(4/3)*math.pi*(r**2)
    print("Area de la esfera: "+str(a))
    print("Volumen de la esfera: "+str(v))

volumen (r)

