x= int(input("Dame un valor en ohmios: "))
y= int(input("Dame el segundo valor en ohmios: "))
z= int(input("Dame el tercer valor en ohmios: "))

r=1/(1/x+1/y+1/z)

print ("El valor de la resistencia combinada es de %s ohmios" % (r))
