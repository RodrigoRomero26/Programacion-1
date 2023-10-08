# %% Ejercicio 1 
import funciones
dni = input("Ingrese el DNI a comprobar")
print(funciones.dnivalidator(dni))
# %% Ejercicio 2
import funciones
word = input("Ingrese la frase")
print(f"La longitud de la palabra es: {funciones.lastwordlen(word)}")
# %% Ejercicio 3 
import funciones
while True:
    completename = input("Ingrese el nombre completo del socio. \n")
    if (completename == ""):
        break
    while True:
        dni = input("Ingrese el DNI del socio")
        if (funciones.dnivalidator(dni)):
            break
        else:
            print("Ingrese un DNI valido.")
    name = funciones.wordselector(completename,0)
    lastname = funciones.wordselector(completename,-1)
    identi = funciones.idmaker(name,lastname,dni)
    print(identi)

# %% Ejercicio 4
import funciones
number = int(input("Ingrese el primer numero"))
number2 = int(input("Ingrese el segundo numero"))
if (funciones.ismult(number,number2)):
    print("El primero es multiplo del segundo")
else:
    print("El primero no es multiplo del segundo")
# %% Ejercicio 5
import funciones
days = int(input("Ingrese la cantidad de dias: "))
for i in range(days):
    temp = float(input("Ingrese la temperatura minima."))
    temp2 = float(input("Ingrese la temperatura maxima"))
    print(f"La temperatura media del dia {i+1} es de {funciones.medtemp(temp,temp2)}")
# %% Ejercicio 6
import funciones
phr = input("Ingrese su frase.")
print(funciones.letterbyletter(phr))
# %% Ejercicio 7
import funciones
numbers = []
while True:
    num = input("Ingrese su numero. Ingrese un espacio para buscar el maximo y el minimo.")
    if (num == " "):
        break
    else:
        numbers.append(num)
maxnum = funciones.minmaxlist(numbers)[-1]
minnum = funciones.minmaxlist(numbers)[0]
print(f"El numero mayor ingresado es {maxnum} y el menor es {minnum}")
# %% Ejercicio 8
import funciones
rad = input("Ingrese el radio de la circunferencia.")
area = funciones.areandper(rad)[0]
peri = funciones.areandper(rad)[-1]
print(f"El area es {area} y el perimetro es {peri}")

# %% Ejercicio 9
import funciones
tries = 0
while tries < 3:
    user = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    result, tries = funciones.login(user, password, tries)
    if result:
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Inicio de sesión fallido. Intentos restantes:", 3 - tries)
if tries == 3:
    print("Se han agotado los intentos. Cuenta bloqueada.")

#%% Ejercicio 10
import funciones
cart = {100:15 , 500:25, 1000:35}
print(f"El precio con descuento es de {funciones.discart(cart)}")

# %% Ejercicio 11
import funciones
numbers = [1,2,3,4,5,6]
doublenumbers = funciones.listchanger(numbers,funciones.double)
print(doublenumbers)
# %% Ejercicio 12
import funciones
phrase = input("Ingrese una frase")
dicc = funciones.phraselen(phrase)
print(dicc)

# %% Ejercicio 13
import funciones
x = int(input("Ingrese el valor de x"))
y = int(input("Ingrese el valor de y"))
mod = funciones.modcalc(x,y)
print(f"El modulo es: {mod}")

# %% Ejercicio 14
import funciones
num = int(input("Ingrese un numero entero"))
if funciones.is_prime(num):
    print("El numero es primo")
else:
    print("No es numero primo")
# %% Ejercicio 15
import funciones
print("Ingrese numeros para obtener su factorial. El programa parara al ingresar un 0")
aux = funciones.getnumbers()
print(f"Se ingresaron {aux} numeros en total.")
# %% Ejercicio 16
import funciones
num = int(input("Ingrese un numero."))
numfind = int(input("Ingrese el digito a buscar."))
total = funciones.digitcount(num,numfind)
print(f"El digito {numfind} se encuentra {total} veces en el numero {num}.")
# %% Ejercicio 17
import funciones
max = 0
while True:
    num = int(input("Ingrese un numero primo."))
    if funciones.is_prime(num):
        print(f"La suma de los digitos de este numero es de {funciones.add_digits(num)}")
        digit = int(input("Ingrese un digito para buscar la frecuencia."))
        print(f"El digito {digit} aparece {funciones.digitcount(num,digit)} veces.")
        if num>max:
            max = num
    else:
        print(f"El mayor numero ingresado es {max} y su factorial es {funciones.factorial(max)}")
        break

# %%
