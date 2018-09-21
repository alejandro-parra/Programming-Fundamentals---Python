def bins(lista,x):
    long=max(lista)
    mats=int(lista.index(long))
    y=mats//2
    mins=0
    while True:
        s=lista[y]
        if x==s:
            return "El elemento %s está en la pocisión %s" % (x,y)
        if x>s:
            mins=lista.index(s)
        if x<s:
            mats=lista.index(s)
        if mats==mins:
            return -1
        y=(mats+mins)//2
def elimina_duplicados(lista):
    nueva=[]
    for x in lista:
        try:
            z=nueva.index(x)
        except ValueError:
            nueva.append(lista[lista.index(x)])
    return nueva
    
        
        
    

lista=[3,5,9,11,12,12,17,17,21,24,22,23,25]
r=elimina_duplicados(lista)
print(r)
