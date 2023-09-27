# %%
def most (a,b):
    if (a>b):
        return a
    else:
        return b
    
def least (a,b):
    if (a<b):
        return a
    else:
        return b
#Main
x = int(input("Ingrese un numero"))
y = int(input("Ingrese otro numero"))
print(most(x-3, least (x+2, y-5)))
# El error esta en las variables usadas en la funcion, siendo las mismas del main.