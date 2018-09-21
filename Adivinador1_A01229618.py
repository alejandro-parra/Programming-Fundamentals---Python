#Funciones:
def validarstr(x):
    while True:
        try:
            string=str(input(x))
            break
        except ValueError:
            print("Valor inválido. Solo puedes introducir un string.")
    return string

def validarint(x):
    while True:
        try:
            num=int(input(x))
            break
        except ValueError:
            print("Valor inválido. Solo puedes introducir un entero.")
    return num

def funcionamiento(nmax,nmin):
    while True:
        guess=validarstr("¿Es %s?"%(int((nmax+nmin)/2)))
        if guess=="mayor":
            nmin=(nmax+nmin)/2
        elif guess=="menor":
            nmax=(nmax+nmin)/2
        else:
            break
    return "He ganado de nuevo. Tu número es %s."%(int((nmax+nmin)//2))

#Ejecución
print("Bienvenido al adivinador.")
nmax=validarint("Dime el numero máximo: ")
nmin=validarint("Dime el numero mínimo: ")
print("Aqui las reglas: tienes que decirme si es mayor, menor o igual al número que pensaste.")
respuesta=funcionamiento(nmax,nmin)
print(respuesta)
