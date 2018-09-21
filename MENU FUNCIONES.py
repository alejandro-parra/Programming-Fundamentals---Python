import math
print("Hola! Bienvenido al menú de opciones. \nA continuación le desplegamos lo que usted puede hacer: \n  1)Convertidor de unidades de tiempo \n  2)Convertidor de unidades de distancia \n  3)Funcion Volumen Esfera \n  4)Funcion Multiplode")
print("  5)Comparador de dos números")
master=int(input("Qué opción deseas? "))

if master==1:
    numero=int(input("Dame el número de segundos: "))
    def segundos(numero):
        segundos=numero
        dias=numero//(3600*24)
        numero=numero%(3600*24)
        horas=numero//3600
        numero=numero%3600
        minutos=numero//60
        numero=numero%60
        print("numero de segundos dados: "+str(segundos))
        print("dias: "+str(dias))
        print("horas: "+str(horas))
        print("minutos: "+str(minutos))
        print("segundos: "+str(numero))

    segundos(numero)
    
if master==2:
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
if master==3:
    print("Escribe el radio deseado: ")
    r=input()
    r=float(r)
    def volumen (r):
        a=4*math.pi*(r**2)
        v=(4/3)*math.pi*(r**2)
        print("Area de la esfera: "+str(a))
        print("Volumen de la esfera: "+str(v))

    volumen (r)
if master==4:
    mult_x=int(input("Dame un número a comprobar: "))
    mult_y=int(input("Dame el segundo número a comprobar: "))
    def multiplo (mult_x):
        if mult_x%mult_y==0:
            x=True
        else:
            x=False
        print (x)
    multiplo (mult_x)

if master==5:
    num1=int(input("Escribe un número entero: "))
    num2=int(input("Escribe un segundo número: "))
    def compara(num1, num2):
        if num1<num2:
            return -1
        if num1==num2:
            return 0
        if num1>num2:
            return 1
    resultado= compara(num1, num2)
    if resultado==1:
        print("%s es mayor a %s" % (num1, num2))
    if resultado==0:
        print("%s es igual a %s" % (num1, num2))
    if resultado==-1:
        print("%s es menor a %s" % (num1, num2))
