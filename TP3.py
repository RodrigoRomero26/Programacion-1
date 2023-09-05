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

# %% Ejercicio 10
number=int(input("Ingrese un numero entero."))
for i in range(2,number):
    if (number%i) == 0:
        print(f"El numero {number} no es primo")
        break
    else:
        print(f"El numero {number} es primo")
        break

# %% Ejercicio 11
word=input("Ingrese una palabra o frase")
for i in range(len(word)-1, -1, -1):
    print(word[i])

# %% Ejercicio 12
word=input("Ingrese una palabra o frase")
letter=input("Ingrese la letra a buscar")
aux=0
for i in word:
    if i==letter:
        aux+=1
print(f"Hay {aux} {letter} en total.")

# %% Ejercicio 13
validator=bool(False)
while validator!=True:
    word=input("Ingrese palabra a repetir")
    if word!="salir":
        print(word)
    else:
        validator=True

# %% Ejercicio 14
number1=int(input("Ingrese el primer numero"))
number2=int(input("Ingrese el segundo numero"))
if (number1%2==0):
    print(f"El numero {number1} es par")
else:
    print(f"El numero {number1} es impar")
if (number2%2==0):
    print(f"El numero {number2} es par")
else:
    print(f"El numero {number2} es impar")
# %% Ejercicio 15
validator=bool(False)
while validator!=True:
    number=int(input("Ingrese un numero mayor a 0"))
    if number>0:
        print("Los divisores de el numero ingresado son:")
        for i in range(1, number + 1):
            if number % i == 0:
                print(i)
        validator=True
# %% Ejercicio 16
cant=int(input("Especifique cuantos numeros seran ingresados"))
neg=0
for i in range(0, cant):
    number=int(input(f"Ingrese el numero {i+1}"))
    if number<0:
        neg+=1
print(f"Se ingresaron {neg} numeros negativos.")
# %% Ejercicio 17
phrase=input("Ingrese una frase").lower()
vowels=[]
vowels_list=["a", "e", "i", "o", "u"]
for i in phrase:
    if i in vowels_list and i not in vowels:
        vowels.append(i)
if vowels:
    print("Las vocales encontradas son:")
    for i in vowels:
        print(i, end=" ")
# %% Ejercicio 18
num1, num2= 0,1
count=0
while count<=10:
    print(num1, end=" ")
    num1,num2=num2,num1+num2
    count+=1

# %% Ejercicio 19
goal=int(input("Ingrese el objetivo: "))
saving=0
while saving<goal:
    aux=int(input("Ingrese el ahorro de hoy."))
    if aux>0:
        saving+=aux
    else:
        print("El valor debe ser positivo!")
print("Se completo el objetivo.")
# %% Ejercicio 20
num=1
num2=0
while num != 0:
    num=int(input("Ingrese un numero (salir con 0): "))
    num2+=num
print(f"La suma de los numeros es: {num2}")

# %% Ejercicio 21
num=1
top=0
while num != 0:
    num=int(input("Ingrese un numero (salir con 0): "))
    if(num > top):
        top = num

# %% Ejercicio 22
num=0
count=0
while num != -1:
    num=int(input("Ingrese un número entero positivo (-1 para salir): "))
    add=0
    num2=num
    while num2 > 0:
        digit=num2 % 10
        add+=digit
        num2 //= 10
    print(f"La suma es {add}")
    if num % 2 == 0:
        count += 1
print(f"Total de números pares ingresados: {count}")

# %% Ejercicio 23
num=1
tot=0
while num != 0:
    num=int(input("Ingrese los montos de los productos (0 para salir): "))
    tot+=num
print(f"El monto total es: {tot}")

# %% Ejercicio 24
tot= 0
num = int(input("Ingrese los montos de los productos (0 para salir): "))
while num!=0:
    if num<0:
        print("Ingreso un monto negativo, intente nuevamente. ")
    else:
        tot+=num
    num=int(input("Ingrese los montos de los productos (0 para salir): "))
if tot>1000:
    pay =tot-(tot*0.10)
    print(f"El total a pagar, con descuento, es de {pay}.")
else:
    print(f"El total a pagar es: {tot}")
# %% Ejercicio 25
num=int(input("Ingrese un número entero: "))
if num<0:
    print("Ingreso un numero negativo.")
elif num==0:
    print("El factorial de 0 es 1.")
else:
    factorial=1
    for i in range(1, num + 1):
        factorial=i
    print(f"El factorial de {num} es {factorial}.")