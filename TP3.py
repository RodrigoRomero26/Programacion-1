# %% Ejercicio 1
word=input("Ingrese la palabra a repetir 10 veces.")
for i in range(10):
    print(word)
# %% Ejercicio 2
actual_age=int(input("Ingrese su edad actual."))
passing_age=0
for i in range(actual_age):
    passing_age+=1
    print(passing_age)
# %% Ejercicio 3
number=int(input("Ingrese un numero entero positivo"))
aux=0
if (number>0):
    for i in range(number):
        aux+=1
        if(aux % 2)!=0:
            print(aux, end=", ") 
else:
    print("Dato ingresado erroneo.")
# %% Ejercicio 4
number=int(input("Ingrese un numero entero positivo"))
aux=number
if (number>0):
    for i in range(number,0,-1):
        print(i, end=", ")
else:
    print("Datos incorrectos.")
# %% Ejercicio 5
money=float(input("Ingrese la cantidad a invertir."))
annual_interest=float(input("Ingrese el porcentaje de interes anual"))
years=int(input("Ingrese la cantidad de años de inversion"))
i=0
while(i!=years):
    aux=(annual_interest*money)/100
    money=money+aux
    print(f"En el año {i+1} se obtuvo {money}")
    i+=1
# %% Ejercicio 6
size=int(input("Ingrese el tamaño de la piramide"))
for i in range(size):
    for j in range (i+1):
        print("*" ,end="")
    print("")
# %% Ejercicio 7
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
# %% Ejercicio 8
size=int(input("Ingrese un numero entero"))
for i in range(1, size+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

# %% Ejercicio 9
validator=bool(False)
password="notsecurepass"
while (validator!=True):
    login=input("Ingrese la contraseña correspondiente")
    if (login==password):
        print("Acceso correcto.")
        validator=True
    else:
        print("Intente otra vez")
