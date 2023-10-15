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
# %%
