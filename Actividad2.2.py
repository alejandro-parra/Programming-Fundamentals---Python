print("Dame una cantidad de dinero (sin centavos)")
cantidad=input()
cantidad=int(cantidad)
mil=cantidad//1000
cantidad=cantidad%1000
quinientos=cantidad//500
cantidad=cantidad%500
doscientos=cantidad//200
cantidad=cantidad%200
cien=cantidad//100
cantidad=cantidad%100
veinte=cantidad//20
cantidad=cantidad%20
cincuenta=cantidad//50
cantidad=cantidad%50
diez=cantidad//10
cantidad=cantidad%10
cinco=cantidad//5
cantidad=cantidad%5
dos=cantidad//2
cantidad=cantidad%2
uno=cantidad//1
cantidad=cantidad%1

print ("billetes de mil: "+str(mil))
print ("billetes de quinientos: "+str(quinientos))
print ("billetes de doscientos: "+str(doscientos))
print ("billetes de cien: "+str(cien))
print ("billetes de cincuenta: "+str(cincuenta))
print ("billetes de veinte: "+str(veinte))
print ("monedas de diez: "+str(diez))
print ("monedas de cinco: "+str(cinco))
print ("monedas de dos: "+str(dos))
print ("monedas de uno: "+str(uno))
