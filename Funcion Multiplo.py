mult_x=int(input("Dame un número a comprobar: "))
mult_y=int(input("Dame el segundo número a comprobar: "))
def multiplo (mult_x):
    if mult_x%mult_y==0:
        x=True
    else:
        x=False
    print (x)
multiplo (mult_x)
