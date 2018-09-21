#FUNCIONES:
def validarstr(x):
    while True:
        try:
            string=str(input(x))
            return string
        except ValueError:
            print("Valor inválido. Solo puedes introducir un string.")
            
def validarint(x):
    while True:
        try:
            num=int(input(x))
            break
        except ValueError:
            print("Valor inválido. Solo puedes introducir un entero.")
    return num

def val_int_mayor1(pr):
    while True:
            x=int(validarint(pr))
            if x>=1:
                break
            else:
                print("Error")
    return x

def val_int_mayor0(pr):
    while True:
            x=int(validarint(pr))
            if x>=0:
                break
            else:
                print("Error")
    return x

def sumaN():
    pr="Dame un número entero para sumar su serie: "
    x=validarint(pr)
    contador=0
    serie=0
    while contador<x+1:
        serie+=contador
        contador+=1
    return "f2(%s)= %s"%(x,serie)

def fl():
    pr="Dame un número entero mayor o igual a uno: "
    contador=1
    serie=1
    x=val_int_mayor1(pr)
    while contador<x+1:
        serie*=(2*contador)
        contador+=1
    return "f(%s)= %s"%(x,serie)

def h1():
    pr="Dame un número entero mayor o igual a cero: "
    contador=0
    serie=0
    x=val_int_mayor0(pr)
    while contador<x+1:
        if contador%2==0:
            serie-=contador
        else:
            serie+=contador
        contador+=1
    return "f(%s)= %s"%(x,serie)

def h2():
    pr="Dame un número entero mayor o igual a cero: "
    contador=0
    serie=0
    x=val_int_mayor0(pr)
    while contador<x+1:
        serie+=(2*contador+2)
        contador+=1
    return "f(%s)= %s"%(x,serie)

def numeros_triangulantes():
    pr="Dame un número entero para sacar los triangulares: "
    contador=1
    serie=list()
    x=validarint(pr)
    while contador<x+1:
        n=(contador*(contador+1))/2
        serie.append(int(n))
        contador+=1
    return "Los primeros números triangulares son: %s"%(serie)

def num_dig():
    pr="Dame un número entero para contar sus dígitos: "
    contador=0
    x=validarint(pr)
    if x<0:
        x*=-1
    while x>=1:
        x/=10
        contador+=1
    if x==0:
        contador=1
    return "Los dígitos que tiene tu número son: %s"%(contador)

        

#PROGRAMA:
pregunta="Qué opción deseas? "
while True:
    print("\n Bienvenido al menú de opciones. Las opciones son las siguientes:\n  1) Sumar N números\n  2) Serie de multiplicación de 2n\n  3) Función h1: 1-2+3...n\n  4) Función h2: 2+4+6...+(2n+2)\n  5) Función números triangulares\n  6) Función num_dig\n  7) Salir")
    respuesta=validarint(pregunta)
    if respuesta==1:
        r1=sumaN()
        print(r1)
    elif respuesta==2:
       r2=fl()
       print(r2)
    elif respuesta==3:
        r3=h1()
        print(r3)
    elif respuesta==4:
        r4=h2()
        print(r4)
    elif respuesta==5:
        r5=numeros_triangulantes()
        print(r5)
    elif respuesta==6:
        r6=num_dig()
        print(r6)                                      
    else:
        exit()
        
    
    
