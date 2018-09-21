def valida_num(x):
    while True:
        try:
            y=int(input(x))
            break
        except ValueError:
            print("Debes de introducir sólo números enteros. ")
    return y
def mayor_Ingresado(x):
    lista=[]
    while True:
        y=valida_num(x)
        if y<0:
            return "El dato mayor ingresado es %s"%(max(lista))
        lista.append(y)
def palabras(string,num):
    contador=0
    lista=string.split(" ")
    for x in lista:
        if len(x)==num:
            contador+=1
    return "El string tiene %s palabras con %s letras"%(contador,num)
def extension_frecuente(lista):
    nueva=[]
    extensiones=[]
    mats=0
    frec=" "
    todas=[]
    for x in lista:
        nueva.append(x.split("."))
    for x in nueva:
        try:
            z=extensiones.index(x[1])
        except ValueError:
            extensiones.append(x[1])
        todas.append(x[1])
    for x in todas:
        z=extensiones.count(x)
        if z>mats:
            mats=z
            frec=x    
    return "La extensión más frecuente es .%s"%(frec)
def duplica_lista(lista):
    nueva=[]
    for x in range(2):
        for y in lista:
            nueva.append(y)
    return nueva
def ganador(comp,tiempos):
    contador=0
    times=[]
    for x in tiempos:
        contador=0
        for y in x:
            contador+=y
        times.append(contador)
    ganador=times.index(min(times))    
    return "El ganador es %s"%(comp[ganador])
def con_prefijo(string,pre):
    lista=string.split(" ")
    final=[]
    for x in lista:
        if pre in x:
            final.append(x)
    return final
def nomenclatura(string,piso,depa):
    final=[]
    for x in range(piso):
        lista=[]
        for y in range(depa):
            if len(str(y+1))==1:
                lista.append("%s%s-0%s"%(string,x,y+1))
            else:
                lista.append("%s%s-%s"%(string,x,y+1))
        final.append(lista)
    return final

