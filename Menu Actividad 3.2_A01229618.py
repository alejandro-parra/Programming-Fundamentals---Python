#Menú Actividad 3: Alejandro Parra Altamirano
#A01229618
def palindrome(variable):
    x=variable.replace(" ", "")
    y=x[::-1]
    if x==y:
        return True
    else:
        return False
    
def esVocal(ip2):
    return ip2 in "aeiouAEIOU"

def cuantasVocales(ip3):
    return ip3.count("a")+ip3.count("e")+ip3.count("i")+ip3.count("o")+ip3.count("u")

def suprimeVocales(ip4):
    a=ip4.replace("a","")
    e=a.replace("e","")
    i=e.replace("i","")
    o=i.replace("o","")
    u=o.replace("u","")
    return u

print("Bienvenido al menu de opciones de la Actividad 3.2. A continuación mostramos las opciones: \n  1) Palindrome\n  2) esVocal\n  3) cuantasVocales\n  4) suprimeVocales")
respuesta=int(input("¿Qué opción desea? (introduzca solamente el número) "))

if respuesta==1:
    variable=input("Escribe un string para checar si su versión inversa se escribe de la misma manera: ")
    variable=variable.lower()
    r1=palindrome(variable)
    print (r1)
if respuesta==2:
    ip2=str(input("Dame un caracter para verificar si es Vocal: "))
    r2=esVocal(ip2)
    print (r2)
if respuesta==3:
    ip3=input("Echele con un string para contar sus vocales: ")
    ip3=ip3.lower()
    r3=cuantasVocales(ip3)
    print("Tu string tiene ", r3, " vocales. ")
if respuesta==4:
    ip4=input("Dame un string para suprimir sus vocales: ")
    ip4=ip4.lower()
    r4=suprimeVocales(ip4)
    print (r4)
