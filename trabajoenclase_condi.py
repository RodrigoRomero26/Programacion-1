fecha=input("Ingrese el dia de semana, el numero y el mes. Use el formato: dia, DD/MM ")
dia_semana=fecha[0:fecha.find(",")]
dia_numero=fecha[fecha.find(" ")+1:fecha.find("/")]
mes_numero=fecha[fecha.find("/")+1:]
lista=["lunes", "martes", "miercoles", "jueves", "viernes"]
lista2=["lunes", "martes", "miercoles"]
if (int(dia_numero)<=31) and (int(mes_numero)<=12):
    if (dia_semana.lower())in lista:
        if (dia_semana.lower())in lista2:
            examenes=input("Se tomaron examenes hoy? si/no ")
            if (examenes.lower()) == "si":
                alumnos=input("Ingrese cuantos alumnos rindieron: ")
                aprobados=input("Ingrese cuantos aprobaron: ")
                desaprobados=(int(alumnos)-int(aprobados))
                print(f"El porcentaje de alumnos aprobados es de: {int(aprobados)/int(alumnos)*100}%")
        elif (dia_semana.lower())=="jueves":
            asistencia=input("Ingrese el porcentaje de alumnos que asistieron: ")
            if (int(asistencia)>50):
                print("Asistio la mayoria ")
            else:
                print("No asistio la mayoria ")
        elif (dia_semana.lower())=="viernes":
            if dia_numero=="01" and (mes_numero=="01" or mes_numero=="07"):
                print("Comienzo de nuevo ciclo ")
                alumnos=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
                arancel=int(input("Ingrese el arancel correspondiente por alumno: "))
                print(f"El ingreso total es de {alumnos*arancel} pesos.")
else:
    print("Datos ingresados erroneos ")