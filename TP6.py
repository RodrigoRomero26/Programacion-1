# %% Ejercicio 1, 2, 3, 4, 5
list = []
listmod = []
listcant = []

while True:
    num = int(input("Ingrese numeros. El programa se detendra al ingresar 0."))
    if num == 0:
        delete = int(input("Ingrese un numero a eliminar."))
        if delete in list:
            list.remove(delete)
        else:
            print("No se encontro el numero.")
        print("Los numeros ingresados son:")
        for i in list:
            print (i, end=" ")
        nummax = int(input("Ingrese otro numero."))
        for j in list:
            if j <= nummax:
                listmod.append(j)
        print("Lista modificada:")
        for j in listmod:
            print (j, end=" ")
        break
    else:
        list.append(num)
print(" ")
for i in list:
    cont = 0
    for j in list:
        if j == i:
            cont+=1
    if (i,cont) not in listcant:
        listcant.append((i,cont))
for i in listcant:
    print (i, end=" ")
# %% Ejercicio 6 
from funciones import *
schoolstudents = []
highschoolstudents = []
print("Ingrese los nombres de los alumnos de primaria.")
schoolstudents = listmaker(schoolstudents,"X")
print("Ingrese los nombres de los alumnos de secundaria.")
highschoolstudents = listmaker(highschoolstudents,"X")
listshow(listmakenoreps(schoolstudents))
listshow(listmakenoreps(highschoolstudents))
listshow(showreps(schoolstudents,highschoolstudents))
listshow(shownoreps(schoolstudents, highschoolstudents))
# %% Ejercicio 7
count = {}
strings = 50
while strings > 0:
    userstring = input(f"Ingrese la frase. Quedan: {strings}")
    strings -= 1
    for letter in userstring:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
print("Total de ocurrencias: ")
for i, j in count.items():
    print(f"Caracter: {i} Ocurrencias: {j}")
# %% Ejercicio 8
import random
rows = 9
columns = 9
goals = []
for i in range(rows):
    row = []
    for j in range(columns):
        if (i!=j):
            row.append(random.randint(1,8))
        else:
            row.append(0)
    goals.append(row)
for i in range(len(goals)):
    team = 0
    wins = 0
    lose = 0
    tie = 0
    totalgoals = 0
    for j in range(len(goals)):
        if goals[i][j] > goals [j][i]:
            wins +=1
        elif goals[i][j] == goals[j][i]:
            tie +=1
        else:
            lose +=1
        totalgoals += (goals[i][j] - goals[j][i])
    print(f"El equipo {i+1} tuvo {wins} victorias, {tie} empates y {lose} derrotas. La diferencia total de goles es de {totalgoals}. Y obtuvo {(wins*3+tie)} puntos.")
# %% Ejercicio 9



# %% Ejercicio 10
import random
matriz = []
rows = int(input("Ingrese la dimension de la matriz. Debe ser cuadrada."))
columns = rows
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(random.randint(1,8))
    matriz.append(row)
for i in matriz:
    print(i)
    print(" ")
print("La diagonal de la matriz es:")
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if (i == j):
            print(matriz[i][j], end=" ")
print("\nLa diagonal inversa de la matriz es:")
for i in range(len(matriz)):
    print(matriz[i][len(matriz) - 1 - i], end=" ")

# %% Ejercicio 11
moneytypes = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
money = input("Ingrese una divisa.").title()
if money in moneytypes:
    aux = moneytypes[money]
    print(f"El simbolo del tipo de moneda {money} es {aux}")
else:
    print("No se encuentra este tipo de divisa.")

# %% Ejercicio 12
name = input("Ingrese su nombre.").capitalize
age = input("Ingrese su edad.")
address = input("Ingrese su direccion.")
num = input("Ingrese su telefono.")
data = {
    'name' : name,
    'age' : age,
    'address' : address,
    'num' : num
}
print(f"{data['name']} tiene {data['age']} años, vive en {data['address']} y su numero de telefono es {data['num']}")
# %% Ejercicio 13
fruitprices = {
    'manzana' : 300,
    'pera' : 250,
    'uva' : 230,
    'banana' : 600,
    'frutilla' : 1000
}
fruit = input("Ingrese que fruta quiere comprar")
if fruit in fruitprices:
    kg = float(input("Ingrese la cantidad de kilos a llevar."))
    total = fruitprices[fruit] * kg
    print(f"El total de llevar {kg} kg de {fruit} es de {total}")
else:
    print("La fruta no esta en el catalogo.")
# %%
