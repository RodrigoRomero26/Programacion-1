# %% Ejercicio 0
x=0
list_aux=[4,6,10]
while(x<=30):
    x+=1
    if x in list_aux:
        print(f"The value {x} of x was skipped")
    elif x!=15:
            print(f"The value of the loop is {x}")
    else:
        print(f"The execution of the loop was broken when x was {x}")
        break
# %% Ejercicio 1
line="a"
while line!="":
    line=input("Ingrese una linea").upper()
    print(line)
    print(" ")

# %% Ejercicio 2
aux="a"
account=0
while True:
    aux=(input("Ingrese su operacion. D o R")).upper()
    if aux=="":
        break
    else:
        if (aux[0]=="D"):
            account+=float(aux[aux.find(" "):])
        elif (aux[0]=="R"):
            account-=float(aux[aux.find(" "):])
        else:
            print("No se ingreso R o D, intente otra vez.")
print(account)
# %%
