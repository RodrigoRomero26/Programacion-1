def option_1():
        name = input("Ingrese el nombre del pasajero a agregar: ").title()
        DNI = input("Ingrese DNI del pasajero: ")
        destiny = input("Ingrese el destino del vuelo: ")
        tuple_passenger = (name, DNI, destiny)
        return tuple_passenger

def option_2():
    country_name = input("Ingrese el pais: ")
    city_name = input("Ingrese la ciudad a donde viaja: ")
    tuple_destination = (city_name, country_name)
    return tuple_destination

def option_3(passenger_list,DNI):
    for tup in passenger_list:
        if tup[1] == DNI:
            return f"El destino de {tup[0]} es {tup[2]}"
    return "Pasajero no encontrado"

def option_4(passenger_list,city_to_find):
    counter = 0
    for findcity in passenger_list:
        if findcity[2] == city_to_find:
            counter += 1
    return f"Personas que viajan a {city_to_find}: {counter}"

def option_5(passenger_list ,DNI,country_list):
    for tupDNI in passenger_list:
        if tupDNI[1] == DNI:
            for country in country_list:
                if tupDNI[2] == country[0]:
                    return f"Pais al que viaja {tupDNI[0]}: {country[1]}"

def option_6(passenger_list,country_to_find,country_list):
    counter_country = 0
    for city in passenger_list:
        for findcountry in country_list:
            if country_to_find == findcountry[1]:
                if findcountry[0] == city[2]:
                    counter_country += 1
                    continue
    return f"La cantidad de personas que viajan a {country_to_find} son {counter_country}"

def add_buy():
    client_name = input("Ingrese el nombre del cliente: ").title()
    client_date = input("Ingrese la fecha en la que se realizo la compra: ")
    client_mount = input("Ingrese el monto de la compra: ")
    client_direction = input("Ingrese la direccion del cliente: ").title()
    tuple_client = (client_name, client_date, client_mount, client_direction)
    return tuple_client

def see_directions(clients_list):
    names_and_directions = {}
    for extract_directions in clients_list:
        name = extract_directions[0]
        direction = extract_directions[3]
        names_and_directions[name] = direction
    return names_and_directions

def see_salecheck(clients_list):
    salecheck = []
    for exctract_salecheck in clients_list:
        date_client = exctract_salecheck[1]
        mount_client = exctract_salecheck[2]
        name_client = exctract_salecheck[0]
        tuple_salecheck = (name_client, date_client, mount_client)
        salecheck.append(tuple_salecheck)
    return salecheck

def add_partner(partners):
    list_with_partners = partners
    partner_num = int(input("Ingrese el numero de socio: "))
    partner_num_id = "Socio N°" + str(partner_num)
    partner_name = input("Ingrese nombre y apellido: ").title()
    partner_date = input("Ingrese fecha de inscripcion (dd/mm/aaaa): ")
    partner_fee = input("Ingrese si abono la cuota (S/N): ").upper()
    partner_information = [partner_num_id, partner_name, partner_date, partner_fee]
    list_with_partners[partner_num] = partner_information
    
    return list_with_partners

def total_partners(partners):
    return len(partners)

def update_dues(partners):
    partner_access = input("Ingrese el numero de socio: ")
    if partner_access in partners.keys():
        for dues in partners[partner_access]:
            if (dues == "N"):
                confirmation = input("¿Desea actualizar el estado de la cuota? Pulse S para 'Si' o N para 'No' ").upper()
                if (confirmation == "S"):
                    partners[partner_access][3] = "S"
                    return f"{partners[partner_access]}"
                
            elif ("N" not in partners[partner_access]):
                return f"Este usuario tiene la cuota al dia"
    else:
        return f"Numero de socio no encontrado"

def manipulate_date(partners):
    for date in partners.values():
        for changedate in range(len(date)):
            if date[changedate] == "13/03/2018":
                date[changedate] = "14/03/2018"

def delete_partner(partners):
    name_partner = input("Ingrese el nombre del socio que desea eliminar:").title()
    keys_to_delete = []
    for namekey,namevalue in partners.items():
        for namedelete in namevalue:
            if name_partner in namedelete:
                keys_to_delete.append(namekey)

    for key in keys_to_delete:
        del partners[key]