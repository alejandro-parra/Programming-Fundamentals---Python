#HOJA DE TRABAJO 3 PARTE UNO
variable=input("Escribe un string")
variable=variable.lower()

def palindrome(variable):
    x=variable.replace(" ", "")
    y=x[::-1]
    if x==y:
        return True
    else:
        return False
resultado=palindrome(variable)
print (resultado)

#HOJA DE TRABAJO 3 PARTE DOS

#1)

ip1=input("Dame un string: ")
print ("*"*len(ip1))

#2)

ip2=str(input("Dame un caracter: "))
def vocal(ip2):
    return ip2 in "aeiouAEIOU"
r2=vocal(ip2)
print (r2)

#3) La escribiría de la manera como la escribí en la pregunta 2

#4) Un string es inmutable, a menos que lo vayas a imprimir"

#5)

ip5=input("Dame un stringsillo: ")
def impar(ip5):
    return ip5[1::2]

var5=impar(ip5)
print(var5)

#6)
ip6=input("Deme otro no sea malo: ")
def ultimos3(ip6):
    return ip6[:-4:-1]
var6=ultimos3(ip6)
print(var6)

#7 y 8)
ip7=input("Echele con un string chingon")
ip7=ip7.lower()
def cuantasVocales(ip7):
    return ip7.count("a")+ip7.count("e")+ip7.count("i")+ip7.count("o")+ip7.count("u")
var7=cuantasVocales(ip7)
print("Tu string tiene ", var7, " vocales. ")

#9)

ip9=input("Echele con un str papason")
ip9=ip9.lower()
def suprimeVocales(ip9):
    a=ip9.replace("a","")
    e=a.replace("e","")
    i=e.replace("i","")
    o=i.replace("o","")
    u=o.replace("u","")
    return u
var9=suprimeVocales(ip9)
print (var9)

#10)

    
