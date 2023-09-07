# %% Ejercicio 0
x=0
list_aux=[4,6,10]
while(x<=30):
    x+=1
    if x in list_aux:
        print(f"The value {x} of x was skipped")
    elif x!=15:
            print(f"The value of the loop is {x}")
    else:
        print(f"The execution of the loop was broken when x was {x}")
        break
# %% Ejercicio 1
line="a"
while line!="":
    line=input("Ingrese una linea").upper()
    print(line)
    print(" ")

# %% Ejercicio 2
aux="a"
account=0
while True:
    aux=(input("Ingrese su operacion. D o R")).upper()
    if aux=="":
        break
    else:
        if (aux[0]=="D"):
            account+=float(aux[aux.find(" "):])
        elif (aux[0]=="R"):
            account-=float(aux[aux.find(" "):])
        else:
            print("No se ingreso R o D, intente otra vez.")
print(account)
# %% Ejercicio 3
prime_num=0
while True:
    number=int(input("Ingrese un numero mayor a 1 "))
    if number>1:
        for i in range(2, number):
            if number % i == 0:
                break
            else:
                prime_num+=1
                break
    elif number==0:
        break
print(f"Se ingresaron {prime_num} numeros primos")

# %% Ejercicio 4
year=int(input("Ingrese el primer año"))
year1=int(input("Ingrese el segundo año"))
if year > year1:
    for i in range(year1,year):
        if ((i%4==0) and (i%100!=0)) or i%400==0:
            if i%10==0:
                print(f"El año {i} es bisiesto y multiplo de 10")
                print(" ")
else:
    for i in range(year,year1):
        if ((i%4==0) and (i%100!=0)) or i%400==0:
            if i%10==0:
                print(f"El año {i} es bisiesto y multiplo de 10")

# %% Ejercicio 5
for i in range(1, 21):
    if i%2==0:
        print(i, end=" ")
    else:
        continue

# %% Ejercicio 6
import random
list_1=[]
size=int(input("Ingrese el tamaño de la lista"))
for i in range(0, size-1):
    list_1.append(random.randint(0,10))
num_find=int(input("Ingrese el numero a buscar."))
for j in list_1:
    if j == num_find:
        print(f"Numero {num_find} encontrado.")
        break

# %% Ejercicio 7
option=1
import time
while True:
    option=int(input("Ingrese una opcion.\n 1.Compras \n 2.Ventas \n 3.Consultas \n 0.Salir"))
    if option==1:
        print("Seleccionó Compras, comuniquese con compras@empr.com")
        time.sleep(3)
    elif option==2:
        print("Seleccionó Ventas, comuniquese con ventas@empr.com")
        time.sleep(3)
    elif option==3:
        print("Seleccionó Consultas, comuniquese con atencionalcliente@empr.com")
        time.sleep(3)
    elif option==0:
        print("Esperamos que vuelva pronto.")
        time.sleep(3)
        break
    else:
        print("Ingreso una opcion incorrecta, intente otra vez.")
        time.sleep(3)
# %%
