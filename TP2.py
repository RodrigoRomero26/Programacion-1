# %% Ejercicio 1
año=int(input("Ingrese cuantos años tiene la computadora "))
if (año==2023) or (año>2020):
    print("La computadora es nueva ")
else:
    print("La computadora es vieja")
# %% Ejercicio 2
año=int(input("Ingrese cuantos años tiene la computadora "))
if (año>0):
    if (año==2023) or (año>2020):
        print("La computadora es nueva ")
    else:
        print("La computadora es vieja")
else:
    print("Dato ingresado incorrecto ")
# %% Ejercicio 3
nom1=input("Ingrese el primer nombre: ")
nom2=input("Ingrese el segundo nombre: ")
if (nom1[0].lower()==nom2[0].lower()):
    print("Coincidencia")
else:
    print("No hay coincidencia ")
# %% Ejercicio 4
voto=input("Ingrese su voto. A: partido rojo. B: partido verdad. C: partido azul")
vali=("A", "B", "C")
if (voto.upper() in vali):
    if(voto.upper()=="A"):
        print("Usted ha votado por el partido rojo.")
    elif(voto.upper()=="B"):
        print("Usted ha votado por el partido verdad.")
    else:
        print("Usted ha votado por el partido azul.")
else:
    print("Opcion incorrecta.")
# %% Ejercicio 5
dato=input("Ingrese una letra: ").lower()
lista=("a","e","i","o","u")
if (len(dato)==1):
    if (dato in lista):
        print(f"La letra {dato} es vocal.")
else:
    print("Dato invalido, no se puede procesar.")

# %% Ejercicio 6
ano=int(input("Ingresar un año: "))
if(ano%4==0):
    if(ano%100!=0):
        print("El año es bisiesto.")
    elif(ano%400==0):
        print("El año es bisiesto.")
    else:
        print("El año no es bisiesto.")
else:
    print("El año no es bisiesto.")
# %% Ejercicio 7
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
mayor=num1
if (num2>mayor):
    mayor=num2
if (num3>mayor):
    mayor=num3
print(f"El numero mayor es {mayor}")
# %% Ejercicio 8
user=input("Ingrese el usuario ")
password=input("Ingrese la contraseña ")
lista=("Gwenevere", "excalibur")
if (user in lista) and (password in lista):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")
# %% Ejercicio 9
nombre=input("Ingrese el nombre del alumno").upper()
sex=input("Ingrese el sexo H/M: ").upper()
if (sex == 'M' and nombre[0] < 'M') or (sex == 'H' and nombre[0] > 'N'):
    grupo = 'A'
else:
    grupo = 'B'
print(f"El alumno pertenece al grupo {grupo}")
# %% Ejercicio 10
edad=int(input("Ingrese la edad del cliente."))
if (edad<=4):
    print("La entrada es gratis")
elif (edad<=18):
    print("La entrada vale $500")
elif (edad>18):
    print("La entrada vale $1000")
# %% Ejercicio 11
tipo=input("Ingrese si quiere pizza vegetariana (V) o no vegetariana (NV)").upper()
if (tipo=="V"):
    print("Eligio pizza vegetariana. Los ingredientes base son: Mozzarella y tomate")
    ingrediente=input("Elija un ingrediente adicional: Pimiento o Tofu.").lower()
    if (ingrediente=="pimiento"):
        print("Su orden es: Pizza vegetariana. Mozzarella, tomate, pimiento")
    elif (ingrediente=="tofu"):
        print("Su orden es: Pizza vegetariana. Mozzarella, tomate, tofu")
    else:
        print("Opcion incorrecta.")
elif (tipo=="NV"):
    print("Eligio pizza no vegetariana. Los ingredientes base son: Mozzarella y tomate")
    ingrediente=input("Elija un ingrediente adicional: Pepperoni, Jamon, Salmon.").lower()
    if(ingrediente=="pepperoni"):
        print("Su orden es: Pizza no vegetariana. Mozzarella, tomate, pepperoni")
    elif(ingrediente=="jamon"):
        print("Su orden es: Pizza no vegetariana. Mozzarella, tomate, jamon")
    elif(ingrediente=="salmon"):
        print("Su orden es: Pizza no vegetariana. Mozzarella, tomate, salmon")
    else:
        print("Opcion incorrecta")
else:
    print("Opcion incorrecta.")

# %% Ejercicio 12
ano=int(input("Ingrese el primer año"))
ano1=int(input("Ingrese el segundo año"))
if(ano>ano1):
    print(f"Han pasado {ano-ano1} años")
else:
    print(f"Faltan {abs(ano-ano1)} años")

# %% Ejercicio 13
num1=int(input("Ingrese el primer valor."))
num2=int(input("Ingrese el segundo valor."))
if(num1>0) and (num2>0):
    mayor=max(num1,num2)
    menor=min(num1,num2)
else:
    print("Valores incorrectos.")
if mayor % menor == 0:
    print(f"{mayor} es múltiplo de {menor}.")
else:
    print(f"{mayor} no es múltiplo de {menor}.")

# %% Ejercicio 14
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
if (a==0):
    if (b==0):
        print("La ecuación tiene infinitas soluciones.")
    else:
        print("La ecuación no tiene soluciones.")
else:
    x = -b / a
    print(f"La solución de la ecuación {a}x + {b} = 0 es x = {x:.2f}.")
# %% Ejercicio 15
import math
forma = str(input("Desea calcular el area de un triangulo o de un circulo? T/C")).lower()
if(forma=="t"):
    b=int(input("Ingrese la base. "))
    h = int(input("Ingrese la altura. "))
    tot=(b*h)/2
    print(f"El area del triangulo es: {tot}")
elif(forma == "c"):
    r=int(input("Ingrese el radio. "))
    tot = (r**2)*math.pi
    print(f"El area del circulo es: {tot}")
# %% Ejercicio 16
numero1=int(input("Ingrese un numero. "))
numero2 = int(input("Ingrese otro numero. "))
print("1. Suma")
print("2. Multiplicacion")
print("3. Resta")
print("4. Division")
op = int(input("Ingrese el numero de la operacion que desea hacer."))
if(op==1):
    suma = (numero1 + numero2)
    print(f"{suma}")
elif(op==2):
    multi = (numero1 * numero2)
    print(f"{multi}")
elif(op==3):
    rest = (numero1 - numero2)
    print(f"{rest}")
elif(op==4):
    if (numero1==0 or numero2==0):
        print("0")
    else:
        divi = (numero1 / numero2)
        print(f"{divi}")

# %% Ejercicio 17
dia = str(input("Ingrese un dia de la semana")).lower()
if(dia == "lunes"):
    print("Feliz lunes.")
if(dia == "viernes"):
    print("Feliz viernes.")
if(dia == "sabado" or dia == "domingo"):
    print("Buen finde.")
else:
    print("Mitad de semana. Sobrevivi.")
# %% Ejercicio 18
horas = float(input("Cuantas horas trabajaste?"))
sal = float(input("Cuanto es su salario por hora?"))
if(horas > 48):
    hs_extra=horas-48
    print(f"Trabajo {hs_extra} horas extra.")
    tot=sal*48+sal+((sal*0.10)*hs_extra)
    print(f"Este mes se realizaron horas extras.\nSe cobro {tot} de salario.")
else:
    print(f"Este mes no se realizaron horas extras.\nSe cobro {horas*sal}")
# %% Ejercicio 19
lapiz = int(input("Cuantas lapices se va a llevar?"))
if(lapiz>= 1000):
    tot=60*lapiz-((60*0.07)*lapiz)
    print(f"El total es de ${tot}")
else:
    print(f"El total es de ${lapiz*60}")

# %% Ejercicio 20
num1 = float(input("Ingrese la nota 1: "))
num2 = float(input("Ingrese la nota 2: "))
num3 = float(input("Ingrese la nota 3: "))
num4 = float(input("Ingrese la nota 4: "))
prom = (num1 + num2 + num3 + num4)/4
if (prom > 6):
    print("Esta aprobado.")
else:
    print("Desaprobo.")