# %% Ejercicio 1
lugares=int(input("Ingrese la cantidad de lugares a mover."))
for i in range(5): 
    palabra=input(f"Palabra {i+1}").upper()
    aux=""
    for j in palabra:
        j=ord(j)
        if (j>=65) and (j<=90):
            j=j+lugares
            j=chr(j)
            aux += j
        else:
            j=chr(j)
            aux += j
    print(f"La palabra codificada es: {aux}")
# %% Ejercicio 2
x=1
pares_con=0
impares_con=0
while x!=0:
    x=int(input("Ingrese el numero. "))
    z=x
    pares=0
    impares=0
    while z>0:
        digito=z % 10
        if (digito % 2)==0:
            pares_con+=1
            pares+=1
        else:
            impares_con+=1
            impares+=1
        z //= 10
    print(f"En el numero {x} hay {pares} numeros pares y {impares} impares")
print(f"Se contaron {pares_con} numeros pares y {impares_con} numeros impares.")
