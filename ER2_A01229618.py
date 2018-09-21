
def temperatura(t):
    if t>100:
        resultado="Vapor"
    if t<100 and t>=30:
        resultado="Caliente"
    if t>=0 and t<30:
        resultado="Fría"
    if t>=-273 and t<0:
        resultado="Congelada"
    if t<-273:
        resultado= "Temperatura inexistente"
    print ("El agua según la temperatura es: %s" % (resultado))

def esVocal(c):
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
        return True
    else:
        return False

t=float(input("Dame la temperatura del agua: "))
temperatura(t)

c=(input("Dame un carácter: "))
c=c.lower()
vocal= esVocal(c)
print (vocal)
