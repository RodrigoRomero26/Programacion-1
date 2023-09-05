# %% Ejercicio 1
base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
print(f"El area {base*altura} y el perimetro {(base*2)+(altura*2)}")
# %% Ejercicio 2
cat1=float(input("Ingrese el primer cateto: "))
cat2=float(input("Ingrese el segundo cateto: "))
print(f"La hipotenusa de estos catetos es {cat1**2+cat2**2}")
# %% Ejercicio 3
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
print(f"La suma es: {num1+num2}. La resta es: {num1-num2}. La multiplicacion: {num1*num2}. La division: {num1/num2}")
# %% Ejercicio 4
tempf=float(input("Ingrese la temperatura en grados Fahrenheit para transformarlo a Celsius: "))
tempc=(tempf-32)*5/9
print(f"{tempf} Grados Fahrenheit corresponden a {tempc} grados Celsius.")
# %% Ejercicio 5
#a)
nombre=(input("Cuál es tu canción favorita?”)"))
#b)
precio=float(input("Precio: "))
total=precio+(precio*0.1)
#c)
edad=int(input("Edad: "))
print(f"Tu edad es {edad}")
#d)
edad=int(input("Edad: "))
print("Veamos si tu edad es 18...", edad==18)
# %% Ejercicio 6
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
print(f"La media de estos numeros es: {(num1+num2+num3)/3}")
# %% Ejercicio 7
minutos=int(input("Ingrese la cantidad de minutos: "))
horas=minutos//60
minutosr=minutos%60
print(f"En {minutos} entran {horas} horas y {minutosr} minutos.")

# %% Ejercico 8 
sueldo=int(input("Ingrese el valor de su sueldo base: "))
venta1=int(input("Ingrese el valor de la primer venta: "))
venta2=int(input("Ingrese el valor de la segunda venta: "))
venta3=int(input("Ingrese el valor de la tercer venta: "))
comisiones=(venta1*0.10)+(venta2*0.10)+(venta3*0.10)
print(f"Recibira ${comisiones} por comisiones y ${sueldo+comisiones} en total.")
# %% Ejercicio 9
total=int(input("Ingrese el valor total de la compra: "))
print(f"El total a pagar con su descuento del %15 es de {total*0.85}")
# %% Ejercicio 10
par1=int(input("Ingrese la nota del primer parcial: "))
par2=int(input("Ingrese la nota del segundo parcial: "))
par3=int(input("Ingrese la nota del tercer parcial: "))
ex_final=int(input("Ingrese la nota del examen final: "))
tr_final=int(input("Ingrese la nota del trabajo final: "))
porc=float(par1+par2+par3)/3
print(f"La calificacion final es {(porc*0.55)+(ex_final*0.30)+(tr_final*0.15)}")
# %% Ejercicio 11
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
print(f"La distancia entre estos numeros es {abs(num1-num2)}")
# %% Ejercicio 12
num=int(input("Ingrese el numero: "))
print(f"Su raiz cuadrada es {num**(1/2)} y su raiz cubica es {num**(1/3)} ")
# %% Ejercicio 13
num=input("Ingrese un numero de 2 cifras: ")
print(f"Su invertido es {num[::-1]}")
# %% Ejercicio 14
A=(input("Ingrese el primer valor: "))
B=(input("Ingrese el segundo valor: "))
aux=A
A=B
B=aux
print(f"La variable A vale {A} y la variable B {B}")
# %% Ejercicio 15
hora=int(input("Ingrese la hora de salida HH: "))
minutos=int(input("Ingrese el minuto de salida MM: "))
segundos=int(input("Ingrese el segundo de salida SS: "))
segundos_v=int(input("Ingrese los segundos de viaje: "))
tiempo_total_segundos=hora*3600+minutos*60+segundos+segundos_v
hora_llegada = tiempo_total_segundos // 3600
tiempo_total_segundos = tiempo_total_segundos % 3600
minutos_llegada = tiempo_total_segundos // 60
segundos_llegada = tiempo_total_segundos % 60
print(f"El tiempo de llegada es {hora_llegada}:{minutos_llegada}:{segundos_llegada}")
# %% Ejercicio 16
nombre=input("Ingrese su nombre")
apellido=input("Ingrese su apellido")
apelido2=input("Ingrese su segundo apellido")
iniciales= nombre[0] + apellido[0] + apelido2[0]
print(f"Sus iniciales son {iniciales.upper()}")
# %% Ejercicio 17
usuario=input("Ingrese su nombre: ")
print(f"Ahora estás en la matrix, {usuario.capitalize()}")
# %% Ejercicio 18
precio_plato=int(input("Ingrese el precio del plato consumido: "))
precio_bebida=int(input("Ingrese el precio de la bebida consumida: "))
precio_total=(precio_plato+precio_bebida)
precio_final=(precio_total*(16.2/100))+precio_total
print(f"El monto final a pagar, tomando en cuenta el servicio y la propina es de ${precio_final}")
# %% Ejercicio 19
dia=input("Ingrese su dia de nacimiento (DD): ")
mes=input("Ingrese su mes de nacimiento (MM): ")
año=input("Ingrese su año de nacimiento (AAAA): ")
print(f"Fecha de nacimiento: {dia}/{mes}/{año}")
# %% Ejercicio 20
fecha=input("Ingrese su fecha de nacimiento DDMMAAAA")
print(f"Fecha de nacimiento: {fecha[0:2]}/{fecha[2:4]}/{fecha[4:]}")
# %% Ejercicio 21
km_por_litro=float(input("Cuantos kilometros puede recorrer con un litro de combustible: "))
capacidad_tanque=float(input("Que capacidad de litros tiene el tanque: "))
kilometros_viaje=float(input("Cuantos kilometros se recorreran: "))
km_tanque=capacidad_tanque*km_por_litro
print(f"Se necesitaran {kilometros_viaje/km_tanque} tanques para recorrer {kilometros_viaje} kilometros")
# %%
