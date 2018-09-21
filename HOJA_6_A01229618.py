def creaMatriz1(x):
    matriz=[]
    for i in range(x):
        lista=[]
        for n in range(x):
            lista.append(i)
        matriz.append(lista)
    return matriz

def creaMatriz2(x):
    matriz=[]
    for i in range(x):
        lista=[]
        contador=1
        for n in range(x):
            lista.append(contador)
            contador+=1
        matriz.append(lista)
    return matriz
    
def creaMatriz3(x):
    matriz=[]
    for i in range(x):
        lista=[]
        for n in range(x):
            lista.append(i+1)
        matriz.append(lista)
    return matriz

def creaMatriz4(x):
    matriz=[]
    contador=1
    for i in range(x):
        lista=[]
        for n in range(x):
            lista.append(contador)
            contador+=1
        matriz.append(lista)
    return matriz

def cuentaPares(matriz):
    contador=0
    for i in range(len(matriz)):
        for j in matriz[i]:
            if j%2==0:
                contador+=1
    return "El número de números pares que tiene tu matriz es de %s"%(contador)

def sumaMatriz(matriz):
    contador=0
    for i in range(len(matriz)):
        for j in matriz[i]:
            contador+=j
    return "La suma total de los números de tu matriz es de %s"%(contador)

def cuentaPositivos(matriz):
    contador=0
    for i in range(len(matriz)):
        for j in matriz[i]:
            if j>=0:
                contador+=1
    return "El número de números positivos que tiene tu matriz es de %s"%(contador)

def cambiaNegativos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]<0:
                matriz[i][j]=0  
    return "Tu nueva matriz se vería asi: \n%s"%(matriz)

def cuentaRepeticiones(matriz,num):
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==num:
                contador+=1  
    return "El valor %s se repite %s veces en la matriz"%(num,contador)

def busca(matriz,x):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==x:
                return True
    return False
                  
def sumaMayores5(matriz):
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]>5:
                contador+=1  
    return "En tu matriz hay %s numeros que son mayores a 5."%(contador)

def cambiaCeros(matriz):
    cont=1
    for i in range(len(matriz)):
        contador=1
        for j in range(len(matriz[i])):
            if matriz[i][j]==0:
                matriz[i][j]=cont*contador
            contador+=1
        cont+=1
    return "Tu nueva matriz se vería asi: \n%s"%(matriz)

