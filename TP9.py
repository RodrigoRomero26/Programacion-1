# %% Ejercicio 1
"""from Persona import Persona
myperson = Persona()
myperson.name = input("Ingresa el name")
myperson.age = input("Ingresa la edad")
myperson.dni = input("Ingresa el DNI")
myperson.mostrar()
if myperson.esMayorDeEdad():
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad.")
"""
# %% Ejercicio 2
from Cuenta import Cuenta
myaccount = Cuenta()
while True:
    if (myaccount.account == ""):
        print("Debe ingresar el name de la cuenta")
        acc = input("Ingrese el name \n")
        if acc.replace(" ","").isalpha():
            myaccount.account = acc
            break
        else:
            print("Solo se aceptan letras, intente otra vez")
myaccount.mostrar()
myaccount.ingresar(1000)
myaccount.retirar(1500)
myaccount.mostrar()

# %% Ejercicio 3
from Triangulo import Triangulo
side1 = float(input("Ingresa el valor del primer lado: "))
side2 = float(input("Ingresa el valor del segundo lado: "))
side3 = float(input("Ingresa el valor del tercer lado: "))

triangulo = Triangulo(side1, side2, side3)

print(f"Tipo de triángulo: {triangulo.type()}")
print(f"Lado más largo: {triangulo.maxside()}")

# %% Ejercicio 4
from Agenda import *
mydiary = Agenda()
while True:
    print("\nMenú de la agenda:")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    opt = input("Selecciona una opción: ")

    if opt == "1":
        name = input("Nombre del contacto: ")
        phone = input("Teléfono del contacto: ")
        email = input("Email del contacto: ")
        mydiary.addcontact(name, phone, email)
    elif opt == "2":
        mydiary.contactlist()
    elif opt == "3":
        name = input("Nombre del contacto a buscar: ")
        mydiary.findcontact(name)
    elif opt == "4":
        name = input("Nombre del contacto a editar: ")
        newphone = input("Nuevo teléfono: ")
        newemail = input("Nuevo email: ")
        mydiary.editcontact(name, newphone, newemail)
    elif opt == "5":
        mydiary.close()
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")


# %%
