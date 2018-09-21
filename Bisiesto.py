año=int(input("Dame un año: "))
if año%4 ==0:
    if año%100 != 0:
        if año%400!=0:
            print ("Año Bisiesto")      
else:
    print ("No es año bisiesto")
