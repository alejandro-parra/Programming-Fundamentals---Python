x= int(input("Dame un número: "))
y= int(input("Dame otro número: "))
z= int(input("Dame un último número: "))

if x==y and y==z:
    print ("Los tres números son iguales")
elif (x==z and y!=z) or (x==y and y!=z) or (z==y and y!=x) or (x!=z and y==z) or (x!=y and y==z) or (z!=y and y==x):
    print ("Dos números son iguales")
elif x!=y and y!=z:
    print ("Los tres números son diferentes")
    
