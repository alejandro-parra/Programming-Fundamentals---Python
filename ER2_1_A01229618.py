import random

#Funciones:
def validarint(x):
    while True:
        try:
            num=int(input(x))
            return abs(num)
        except ValueError:
            print("Valor inválido. Solo puedes poner un entero. ")
            
def novacio(x):
    cadena=None
    while not cadena:
        num=input(x)
    return num
        
def tirada(x):
    suma=0
    n=validarint(x)
    
    for x in range(n):
        tirada=random.randrange(1,6)
        suma+=tirada
    return "\nLa suma de las tiradas del dado %s veces es de %s."%(n,suma)

def revuelvepalabra(x):
    palabra=list(x)
    revuelta=[]
    while len(palabra)>0:
        r=random.randint(0,len(palabra)-1)
        revuelta.append(palabra[r])
        palabra.remove(palabra[r])
    return "\nTu palabra revuelta es: "+"".join(revuelta)
        
while True:
    print("\nBienvenido al menú del examen. Aquí las opciones:\n  1) Suma de tiradas de dado\n  2) Revuelve Palabra\n  3) Salir")
    respuesta=validarint("¿Qué opción deseas? ")
    if respuesta==1:
        pr1="Dame el número de veces que quieres tirar el dado: "
        f1=tirada(pr1)
        print(f1)
    elif respuesta==2:
        pr2=input("Dame el string que quieres que revuelva: ")
        f2=revuelvepalabra(pr2)
        print(f2)
    else:
        exit()
    




    
