
# %% Ejercicio 1
from funciones_busquedayord import *
import random
numbers = []
for i in range(10):
    numbers.append(random.randint(0,60))
for i in bubblesort(numbers):
    print (i, end=", ")
# %% Ejercicio 2
from funciones_busquedayord import *
words = ["agua", "zinc", "hambre", "casa", "youtube"]
for i in selection_sort(words):
    print (i, end=", ")
# %% Ejercicio 3
books = [
    {
        "title": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "year": 1967,
        "gender": "Realismo mágico"
    },
    {
        "title": "1984",
        "autor": "George Orwell",
        "year": 1949,
        "gender": "Ciencia ficción"
    },
    {
        "title": "El Gran Gatsby",
        "autor": "F. Scott Fitzgerald",
        "year": 1925,
        "gender": "Ficción"
    },
    {
        "title": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "year": 1605,
        "gender": "Novela de caballerías"
    },
    {
        "title": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "year": 1997,
        "gender": "Fantasía"
    }
]
opt = int(input("Elije como ordenar los libros. 1 Titulo. 2 Autor. 3 Año. 4 Genero."))
if opt==1:
    print(sorted(books, key=lambda x: x["title"]))
elif opt==2:
    print(sorted(books, key=lambda x: x["autor"]))
elif opt==3:
    print(sorted(books, key=lambda x: x["year"]))
elif opt==4:
    print(sorted(books, key=lambda x: x["gender"]))
else:
    print("Opcion equivocada")

# %% Ejercicio 4
from funciones_busquedayord import *
strings = []
while True:
    aux = input("Ingrese su cadena. Ingrese 0 para salir.")
    if aux != "0":
        strings.append(aux)
    else:
        break
for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1
        while j >= 0 and len(key) < len(strings[j]):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key
for i in strings:
    print (i)
# %% Ejercicio 5
from funciones_busquedayord import *
import random
numbers = []
for i in range(20):
    numbers.append(random.randint(0,60))
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] < numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for i in numbers:
    print(i, end=", ")

# %% Ejercicio 6
from funciones_busquedayord import *
import random
numbers = []
for i in range(20):
    numbers.append(random.randint(0,60))
for i in counting_sort(numbers):
    print(i, end=", ")

# %% Ejercicio 7
mixed_list = [1, "dos", 3, "cuatro", 5, "seis", 7, "ocho", 9, "diez"]
numbers = [x for x in mixed_list if isinstance(x, int)]
strings = [x for x in mixed_list if isinstance(x, str)]
numbers.sort()
strings.sort()
ascmixed = numbers + strings
for i in ascmixed:
    print(i, end=", ")
# %% Ejercicio 8
from funciones_busquedayord import *
import random
numbers = []
for i in range(20):
    numbers.append(random.randint(0,60))
for i in merge_sort(numbers):
    print(i, end=", ")
# %%
