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

