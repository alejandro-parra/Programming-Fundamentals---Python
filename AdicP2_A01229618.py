def coincidenVocales(x,y):
    lista1=list(x)
    lista2=list(y)
    contador=0
    vocales=["a","e","i","o","u"]
    final=[]
    while contador<5:
        if vocales[contador] in lista1 and vocales[contador] in lista2 and vocales[contador] not in final:
            final.append(vocales[contador])
        contador+=1
    return final

def aprobados(x):
    archivo=None
    try:
        archivo=open("calificaciones.csv")
    except IOError:
        print("Archivo no encontrado. ")
    if archivo:
        print("Estudiantes Aprobados: ")
        for linea in archivo:
            if linea[:2]==x:
                promedio=(int(linea[12:14])+int(linea[15:17])+int(linea[18:]))/3
                if promedio>=70:
                    print(linea)
                
