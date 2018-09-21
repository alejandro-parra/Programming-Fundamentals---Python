#FUNCIONES:
def funcion_intervalos(ip1):
    if ip1<=-2:
        return ip1+3
    if ip1<3 and ip1>-2:
        return ip1**2-4
    if ip1>=3:
        return ip1**2-12*ip1+32

def mts_a_pies(ip2):
    return ip2*3.28084

def huracanes(ip3):
    marea=mts_a_pies(ip3)
    if marea<4:
        return"error"
    if marea>=4 and marea<6:
        return "La categoría es 1 y el daño es Mínimo"
    if marea>=6 and marea<9:
        return "La categoría es 2 y el daño es Moderado"
    if marea>=9 and marea<13:
        return "La categoría es 3 y el daño es Extenso"
    if marea>=13 and marea<19:
        return "La categoría es 4 y el daño es Extremo :("
    if marea>=19:
        return "La categoría es 5 y el daño es Catastrófico :'("

def encripta(ip4):
    return ip4.replace('a','*').replace('e','3').replace('i','=').replace('o','@').replace('u','>')

def mas_larga(ip5,ip51):
    if len(ip5)>len(ip51):
        return 1
    if len(ip5)==len(ip51):
        return 0
    if len(ip5)<len(ip51):
        return -1

def divide(ip6):
    num=len(ip6)//2
    parteuno=str(ip6[:num])
    partedos=str(ip6[num:])
    return parteuno+"---"+partedos

#EJECUCIÓN:
print("Bienvenido al menú de opciones. Seleccione la opción que desea ejecutar:\n  1) Función intervalos\n  2) Función convertidora de metros a pies\n  3) Función que calcula la magnitud y categoría de un huracán\n  4) Función que encripta una palabra\n  5) Función para comparar si un str es mas largo en caracteres que otro\n  6) Funcion que divide una frase en dos")
var=int(input("¿Qué opción desea? (Escribir solamente el número): "))

if var==1:
    ip1=float(input("Dame el número para resolver la función: "))
    r1=funcion_intervalos(ip1)
    print(r1)
if var==2:
    ip2=float(input("Dame el número en metros para convertirlo a pies (sólo el numero): "))
    r2=mts_a_pies(ip2)
    print(r2)
if var==3:
    ip3=float(input("Dame el incremento en el nivel del mar en metros: "))
    r3=huracanes(ip3)
    print(r3)
if var==4:
    ip4=str(input("Escribe una palabra y te la oculto: "))
    ip4=ip4.lower()
    r4=encripta(ip4)
    print(r4)
if var==5:
    ip5=input("Escribe la primera cadena a comparar: ")
    ip51=input("Escribe la segunda cadena a comparar: ")
    r5=mas_larga(ip5,ip51)
    print(r5)
if var==6:
    ip6=str(input("Dame el string que quieres dividir: "))
    r6=divide(ip6)
    print(r6)


