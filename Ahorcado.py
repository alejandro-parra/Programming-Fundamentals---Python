#Ahorcado, juego hecho por Alejandro Parra

#Funciones

def crearlista():
    'Esta función crea la lista de palabras que usaremos después, además de seleccionar una de ellas'
    lista=["serpiente", "ornitorrinco", "pizza", "bote", "calculadora"]
    return random.choice(lista)

def listar(palabra):
    'Esta función crea una lista para la palabra seleccionada aleatoriamente.'
    return list(palabra)
def listaoculta(palabra):
    'Esta función hace una lista para la palabra pero en versión oculta'
    return list("_"*len(palabra))
def dibujo(errores):
    'Esta función dibuja el código ASCII dependiendo de cuantos errores tenga el usuario'
    g="_"
    s=" "
    b="\n"
    l="|"
    gd="/"
    gi="\\"
    if errores==0:
        print(s,g*9,s*5,b,l,s*7,l,s*4,b,l,s*7,"0",s*4,b,l,s*5,gd,l,gi,s*3,b,l,s*5,gd,s,gi,s*3,b,l,s*11,b,l,s*11) 
    if errores==1:
        print(s,g*9,s*5,b,l,s*7,l,s*4,b,l,s*7,"0",s*4,b,l,s*5,gd,l,gi,s*3,b,l,s*5,gd,s,s,s*3,b,l,s*11,b,l,s*11)
    if errores==2:
        print(s,g*9,s*5,b,l,s*7,l,s*4,b,l,s*7,"0",s*4,b,l,s*5,gd,l,gi,s*3,b,l,s*5,s,s,s,s*3,b,l,s*11,b,l,s*11)
    if errores==3:
        print(s,g*9,s*5,b,l,s*7,l,s*4,b,l,s*7,"0",s*4,b,l,s*5,s,l,gi,s*3,b,l,s*5,s,s,s,s*3,b,l,s*11,b,l,s*11)
    if errores==4:
        print(s,g*9,s*5,b,l,s*7,l,s*4,b,l,s*7,"0",s*4,b,l,s*5,s,l,s,s*3,b,l,s*5,s,s,s,s*3,b,l,s*11,b,l,s*11)

#Funcionamiento
      
import random
import math
errores=0
palabra=(crearlista())
#palabra: la variable que decide qué palabra aleatoria se escogió.
desglose=(listar(palabra))
#desglose: la lista de las letras de la palabra sin ocultar
oculta=listaoculta(palabra)
#oculta: la lista de palabras inicial oculta, que se va modificando conforme el usuario adivina.

print(desglose)
print("Este es el juego del ahorcado. Tienes 5 errores para tratar de adivinar la palabra.")

while errores<5:
    print(dibujo(errores))
    print(oculta)
    print("¿Cual es la siguiente letra? Errores: "+str(errores))
    guess=str(input())
    guess=guess.lower
    for x in range(len(desglose)):
        if guess==desglose[x]:
            oculta[x]=desglose[x]
        else:
            errores=errores+1
    if oculta[::]==desglose[::]:
        print("Has Ganado!")
        errores=6

if errores==5:
    print("¡Has Perdido!")

        
    



