def multiplica(x,y):
    if y==1:
        return x
    else:
        return x+multiplica(x,y-1)

def validar_int(x):
    while True:
        try:
            y=int(input(x))
            break
        except ValueError:
            print("Ingrese un valor entero.")
    return y

def enAscendente(n):
    if n==0:
        return 0
    else:
        print(0)+
    

def menu():
    while True:
        print("Bienvenido al menú de opciones. A continuación las opciones:\n  1) multiplica\n  2) enAscendente\n  3) enDescendente\n  4) división por restas\n  5) Suma Harmónica\n  6) cuenta cuántas\n  7) cuantos dígitos\n  8) sumaDígitos\n  9) invierte lista\n  10) vocales\n  11) alreves\n  12) potencia\n  13) decimalABin\n  14) sumaArregloR\n  15) elmayorR\n  16) mcd\n")
        r=int(input("¿Qué opción desea? "))

        if r==1:
            val1=validar_int("Ingresa un número entero: ")
            val2=validar_int("Ingresa el segundo valor: ")
            f1=multiplica(val1,val2)
            print(f1)
        if r==2:
            n=validar_int("Ingresa un número entero: ")
            f2=enAscendente(n)
            print(f2)





