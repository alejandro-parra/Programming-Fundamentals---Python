
def coincidencias(x,y):
    lista1=list(x)
    lista2=list(y)
    contador=0
    suma=0
    if len(x)<len(y):
        b=len(x)
    elif len(x)>len(y):
        b=len(y)
    else:
        b=len(y)
    
    while contador<b:
        if lista1[contador]==lista2[contador]:
            suma+=1
        contador+=1
    return "Numero de caracteres iguales: %s"%(suma)

def vacios(matriz):
    lista=["a","b","c","d","e","f","g","h","i","j"]
    contador=0
    cont=0
    new=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==0:
                new.append(lista[i]+str(j))             
    return "lugares vacios: %s"%(new)

    
def mayores_3(matriz):
    new=[]
    for i in range(3):
        new.append(max(matriz))
        matriz.remove(max(matriz))
    return new

def validarint(x):
    while True:
        try:
            num=int(input(x))
            break
        except ValueError:
            print("Valor inválido. Solo puedes introducir un entero.")
    return num

def validar_rango(pr,x,y):
    while True:
        guess=validarint(pr)
        if guess<x or guess>y:
            print("Valor fuera de rango, inserte otro numero")
        else:
            return "Su numero está en el rango de %s y %s"%(x,y)


    
