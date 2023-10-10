import funcionestrabajovariables
# Ejercicio 1
passengerslist = [("Franco Ortiz","19487588","Lima"),("Juan Carlos","42659877","Buenos Aires"),("Julian Perez","16987855","Cordoba")]
citieslist = [("Lima","Peru"),("Buenos Aires", "Argentina"),("Sao Pablo","Brasil"),("Cordoba","Argentina")]

print("Bienvenido a AMADEUS. Elija su opcion.\n")
while True:
    print("1. Agregar pasajero")
    print("2. Agregar ciudades")
    print("3. Verificar ciudad")
    print("4. Vuelo a la ciudad")
    print("5. Verificar pais")
    print("6. Vuelo a pais")
    print("7. Salir")
    choice = input("Elija su opcion: ")
    
    if choice == "1":
        new_passenger = funcionestrabajovariables.option_1()
        passengerslist.append(new_passenger)
    elif choice == "2":
        new_city = funcionestrabajovariables.option_2()
        citieslist.append(new_city)
    elif choice == "3":
        find_DNI = input("Ingrese el DNI del pasajero a buscar: ")
        find_city = funcionestrabajovariables.option_3(passengerslist, find_DNI)
        print(find_city)
    elif choice == "4":
        city = input("Ingrese la ciudad que quiere saber cuantos pasajeros viajan: ").title()
        city_destiny = funcionestrabajovariables.option_4(passengerslist,city)
        print(city_destiny)
    elif choice == "5":
        DNI_for_country = input("Ingrese el DNI del pasajero para ver a que pais viaja: ")
        print(funcionestrabajovariables.option_5(passengerslist,DNI_for_country,citieslist))
    elif choice == "6":
        country = input("Ingrese el pais para saber cuantos pasajeros viajan: ").title()
        print(funcionestrabajovariables.option_6(passengerslist,country,citieslist))
    elif choice == "7":
        print("Gracias por usar nuestro servicio")
        break
    else:
        print("Ingrese una opcion valida")

# Ejercicio 2
clients = [("Maria Isabel","18","1345.3","Av. Corrientes 698"),("Pedro Cruz","12","2498","Patricias mendocinas 175"),("Ana de armas","6","654","Av. Siempreviva 698")]

while True:
    print("1. Agregar compra")
    print("2. Ver direcciones")
    print("3. Ver facturas de compra")
    print("4. Salir")
    selection = input("Ingrese su opcion: ")

    if selection == "1":
        new_clients = funcionestrabajovariables.add_buy()
        clients.append(new_clients)
        print(f"Lista de clientes actualizada \n {clients}")
    elif selection == "2":
        print(f"Direcciones de los clientes \n {funcionestrabajovariables.see_directions(clients)}")
    elif selection == "3":
        print("Facturas (Nombre del cliente, fecha, monto): ")
        print(funcionestrabajovariables.see_salecheck(clients))
    elif selection == "4":
        break
    else:
        print("Ingrese una opcion valida.")

# Exercise 3
partners_list = {
    "1" : ["Socio N°1","Marcos Jurado","17/03/2009","S"],
    "2" : ["Socio N°2","Georgina Collado","17/03/2009","S"],
    "3" : ["Socio N°3","Miren Arenas","17/03/2009","S"],
    "4" : ["Socio N°4","Valentin Curiel","7/10/2003","N"],
    "5" : ["Socio N°5","Rodrigo Romero","13/03/2018","N"],
}
while True:
    print("1. Cargar Informacion")
    print("2. Ver cantidad de socios")
    print("3. Verificar cuota")
    print("4. Modificar fechas")
    print("5. Eliminar socio")
    print("6. Ver todos los socios")
    print("7. Salir")
    select = input("Ingrese su opcion: ")

    if select == "1":
        funcionestrabajovariables.add_partner(partners_list)
    elif select == "2":
        print(f"Cantidad de socios en el club: {funcionestrabajovariables.total_partners(partners_list)}")
    elif select == "3":
        print(funcionestrabajovariables.update_dues(partners_list))
    elif select == "4": 
        funcionestrabajovariables.manipulate_date(partners_list)
        print("¡Fechas actualizadas!")
    elif select == "5":
        funcionestrabajovariables.delete_partner(partners_list)
        print("Socio eliminado de la lista")
    elif select == "6":
        print("Listado de socios: ")
        print(partners_list)