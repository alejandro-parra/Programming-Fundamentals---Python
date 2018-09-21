import math

def menu():
    print("Bienvenido al programa de análisis de datos de la compañía XETU. Creado por Alex Parra y Diego Cabrera \nA continuación le ofrecemos nuestras opciones:\n  1) Ingresar datos de la línea\n  2) Hacer resumen\n  3) Reiniciar semana\n  4) Consultas parciales\n  5) Salir")
    r=int(input("\n¿Qué opción deseas? "))
    if r==1:
        ingresa_datos()
    elif r==2:
        hacer_resumen()
    elif r==3:
        reiniciar_semana()
    elif r==4:
        consulta_parcial()
    else:
        exit()

def validaint(x):
    while True:
        try:
            s=int(input(x))
            break
        except ValueError:
            print("Solo puedes ingresar números enteros. ")
    return s
    
def valida_archivo(x,y):
    archivo=None
    while True:
        try:
            archivo=open(x,y)
            archivo.close()
            break
        except IOError:
            print("No se encontró el archivo. ")
    return open(x,y)

def ingresa_datos():
    numlineas=len_archivo("MAQUINAS.txt")
    a=valida_archivo("MAQUINAS.txt","r+")
    primera=a.readline()
    primera=primera.split(" ")
    inicio=primera[5]
    fin=primera[7]
    mes=primera[9]
    año=primera[11]
    meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    mesesin=int(meses.index(mes))+1
    a.close()
    while True:
        a=valida_archivo("MAQUINAS.txt","r+")
        d1=validaint("Ingresa el número de línea: ")
        d2=validaint("Ingresa el número de turno: ")
        while True:
            d3=validaint("Estamos en el mes de %s. Semana del %s al %s. Ingresa el día de producción: "%(mes,inicio,fin))
            if int(inicio)<=d3 and int(fin)>=d3:
                break
            else:
                print("Día no concuerda con la semana actual. ")
        d4=validaint("Ingresa la cantidad de material producido: ")
        d5=validaint("Ingresa las veces que la máquina se detuvo ese día: ")
        a.read()
        a.write("\nlinea {0},turno {1},{2}-{3}-{4},{5},{6}".format(d1,d2,d3,mesesin,año,d4,d5))
        a.close()
        r=input("¿Desea ingresar otro dato?")
        if r.lower()=="no":
            break    
    menu()
def validalinea():
    exit()
def len_archivo(x):
    num=sum(1 for linea in open(x))
    return num

def hacer_resumen():
    numlineas=len_archivo("MAQUINAS.txt")
    a=valida_archivo("MAQUINAS.txt","r+")
    primera=a.readline()
    primera=primera.split(" ")
    inicio=primera[5]
    fin=primera[7]
    mes=primera[9]
    año=primera[11]
    semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
    resumen=open("Resumen %s %s-%s.txt"%(mes,inicio,fin),"w+")
    resumen.write("Semana del %s al %s de %s:\n"%(inicio,fin,mes))
    prod=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    detenciones=[[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]]

    for x in range(numlineas-1):
        i=a.readline().split(",")
        for contador in range(5):
            if i[0]=="linea %s"%(contador+1):
                if i[1]=="turno 1":
                    prod[contador][0]+=int(i[3])
                    detenciones[contador][0][int(math.fabs(int(i[2][0:2])-int(inicio)))]+=int(i[4])
                elif i[1]=="turno 2":
                    prod[contador][1]+=int(i[3])
                    detenciones[contador][1][int(math.fabs(int(i[2][0:2])-int(inicio)))]+=int(i[4])
                elif i[1]=="turno 3":
                    prod[contador][2]+=int(i[3])
                    detenciones[contador][2][int(math.fabs(int(i[2][0:2])-int(inicio)))]+=int(i[4])

    for x in range(5):
        resumen.write("\nNúmero de línea: %s\n"%(x+1))
        for y in range(3):
            resumen.write("Turno: %s\n"%(y+1))
            resumen.write("Total de productos de la semana: %s\n"%(prod[x][y]))
            resumen.write("Veces que se detuvo la línea: %s\n"%(sum(detenciones[x][y])))
            resumen.write("Día en que más veces se detuvo la línea: %s\n"%(semana[detenciones[x][y].index(max(detenciones[x][y]))]))
    resumen.close()
    menu()

def reiniciar_semana():
    inicio=int(input("Dame el día del nuevo inicio de semana: "))
    final=inicio+6
    
    mes=input("dame el mes actual: ")
    año=input("dame el año actual: ")
    a=valida_archivo("MAQUINAS.txt","w+")
    a.write("Reporte de la semana del %s al %s de %s de %s "%(inicio,final,mes,año))
    a.close()
    menu()

def consulta_parcial():
    linea=validaint("¿qué línea deseas consultar?\n")
    turno=validaint("¿qué turno deseas consultar?\n")
    numlineas=len_archivo("MAQUINAS.txt")
    a=valida_archivo("MAQUINAS.txt","r+")
    primera=a.readline()
    primera=primera.split(" ")
    inicio=primera[5]
    fin=primera[7]
    mes=primera[9]
    semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
    prod=0
    detenciones=[0,0,0,0,0,0,0]
    for x in range(numlineas-1):
        i=a.readline().split
        if i[0]=="linea %s"%(linea):
                if i[1]=="turno %s"%(turno):
                    prod+=int(i[3])
                    detenciones[int(math.fabs(int(i[2][0:2])-int(inicio)))]+=int(i[4])

    print("Turno: %s\n"%(turno))
    print("Total de productos producidos al día: %s\n"%(prod))
    print("Veces que se detuvo la línea: %s\n"%(sum(detenciones)))
    print("Día en que más veces se detuvo la línea: %s\n"%(semana[detenciones.index(max(detenciones))]))
    menu()        
     
menu()
