print("Escribe una medida en pies que desea convertir:")
x=input()
x=float(x)
yarda=x/3
pulgada=x*12
centimetro=pulgada*2.54
m=centimetro/100

print("Valor en pies: "+str(x))
print("Valor en yardas: "+str(yarda))
print("Valor en metros: "+str(m))
print("Valor en pulgadas: "+str(pulgada))

