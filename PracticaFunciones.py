# %%
import funciones
num = int(input("Ingrese el numero: "))
aux = num
while num!=0:
    print(f"Suma: {funciones.add_digits(num)}")
    num = int(input("Ingrese el numero: "))
    aux+=num
print(f"El total es {aux} y la suma de sus digitos es {funciones.add_digits(aux)}")
