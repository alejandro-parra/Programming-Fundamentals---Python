x=float(input("Escribe una medida que desea convertir: "))
y=input("Escribe la unidad en la que lo desea convetir: ".lower())

def medida(x,y):
    if y== "yardas" or "yarda":
        z=x/3
    elif y== "metros" or "metro":
        z=x*12*2.54/100
    elif y=="pulgadas" or "pulgada":
        z=x*12
    elif y=="centimetros" or "centimetro":
        z=x*12*2.54
    print (str(z)+" "+str(y))

medida(x,y)


