numero=304948768
segundos=numero
dias=numero//(3600*24)
numero=numero%(3600*24)
horas=numero//3600
numero=numero%3600
minutos=numero//60
numero=numero%60
print("numero de segundos dados: "+str(segundos))
print("dias: "+str(dias))
print("horas: "+str(horas))
print("minutos: "+str(minutos))
print("segundos: "+str(numero))
