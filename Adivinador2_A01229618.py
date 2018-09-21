#Funciones:
def validarint(x):
    while True:
        try:
            num=int(input(x))
            break
        except ValueError:
            print("Valor inválido. Solo puedes introducir un entero.")
    return num

def funcionamiento():
    resultado=False
    contador=1
    numero=random.randrange(1,100)
    print(numero)
    while contador<6:
        guess=validarint("Intento %s. Diga su número: "%(contador))
        if guess<numero:
            print("El número es mayor")
        elif guess>numero:
            print("El número es menor")
        else:
            resultado=True
            break
        contador+=1
    if resultado==True:
        return("Felicidades! Has Ganado!")
    else:
        return("Lo siento. Numero de intentos alcanzados.")

#Ejecución:
import random
print("Bienvenido al adivinador. El numero que tienes que adivinar es entre 1 y 100")
f=funcionamiento()
print(f)
