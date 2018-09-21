def tablaDel(n):
    for counter in range(1,11):
        print (n*counter)

def sumando(dig):
    suma=0
    for counter in range(1,dig+1):
        sumador=int(input("Dame el número %s a sumar: " % (counter)))
        suma+=sumador
    return suma

def cuantasVocales(voc):
    voc=voc.lower()
    letra=0
    vocales=['a','e','i','o','u']
    for x in range(len(voc)):
        if voc[x] in vocales:
            letra+=1
    return letra
def masVocales(palabra1,palabra2):
    x=cuantasVocales(palabra1)
    y=cuantasVocales(palabra2)
    if x>y:
        print("La palabra %s tiene mas vocales." % (palabra1))
    elif x<y:
        print("La palabra %s tiene mas vocales." % (palabra2))
    else:
        print("Ambas palabras tienen el mismo número de vocales")
    
def reemplazar(viejo,nuevo,cadena):
    lista=list(cadena)
    p=0
    for x in lista:
        if viejo==x:
            lista[p]=nuevo
        p+=1
    cambiada="".join(lista)
    return cambiada

def comunes(lista1,lista2):
    uno=list(lista1)
    dos=list(lista2)
    comun=[]
    for x in uno:
        if x in dos and comun.count(x)==0:
            comun.append(x)
    return comun
            
def divideEnTam(cad,div):
    prin_t=[cad[x:x+div] for x in range(0,len(cad),div)]
    return("-".join(prin_t))

def figura(num):
    for x in range(1,num+1):
        print("*"*x)
        
respuesta="si"     
while respuesta=="si":    
    print("Menu: \n  1) Tabladel\n  2) sumando\n  3) Cuantas Vocales\n  4) Reemplazar\n  5) comunes\n  6) masVocales\n  7) divideEnTam\n  8) Armar Una figura ")
    menu=int(input())
    if menu==1:
        counter=int(0)
        n=int(input("Dime el numero que quieres que haga la tabla: "))
        tablaDel(n)
    elif menu==2:
        dig=int(input("Cuantos números quieres sumar?"))
        function2=sumando(dig)
        print(function2)
    elif menu==3:
        voc=str(input(("Cual es la palabra que quieres que cuente? ")))
        function3=cuantasVocales(voc)
        print(function3)
    elif menu==4:
        cadena=input("Cual palabra es la que vamos a usar: ")
        viejo=input("cual es el caracter que quieres reemplazar: ")
        nuevo=input("Por cual la quieres reemplazar? ")
        function5=reemplazar(viejo,nuevo,cadena)
        print(function5)
    elif menu==5:
        lista1=input("Cual es el primer string que se convertirá en lista? ")
        lista2=input("Cual es el segundo string que se convertirá en lista? ")
        function3=comunes(lista1,lista2)
        print(function3)
    elif menu==6:
        palabra1=input("Dime la primera palabra a comparar: ")
        palabra2=input("Dime la segunda palabra a comparar: ")
        masVocales(palabra1,palabra2)
    elif menu==7:
        cad=input("Dame la cadena que quieres dividir: ")
        div=int(input("Dame el numero de caracteres por división: "))
        function7=divideEnTam(cad,div)
        print(function7)
    else:
        num=int(input("Cuantas lineas de puntitos quieres? "))
        figura(num)
    respuesta=input("Quieres usar otro servicio? ")
    
    


