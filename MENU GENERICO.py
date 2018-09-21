#FUNCIONES:
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

def validarflt(x):
    while True:
        try:
            flt=str(input(x))
            break
        except ValueError:
            print("Valor inválido. Solo puedes introducir un float.")
    return flt

def 
#PROGRAMA:
pregunta="Qué opción deseas?"
while True:
    print("Bienvenido al menú de opciones. Las opciones son las siguientes:\n  1) N numero")
    respuesta=validarstr(pregunta)
    if respuesta==1:
    
    
