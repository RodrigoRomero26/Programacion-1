# %%
word = input("Ingrese una palabra")
if len(word)==4:
    print(word+ "!")
else:
    print(word+ "?")
# %% Ejercicio 2
import random
list_total=["cama", "cocina" ,"escalera" ,"lavadora" , "mesa" , "nevera", "puerta", "silla", "terraza", "ventana"]
while True:
    word = (random.choice(list_total))
    print(f"El juego inicio.\n Tu palabra tiene {(len(word))+1} letras")
    tries=7
    list_totaltry=[]
    list_goodtry=[]
    list_failtry=[]
    for i in word:
        while tries!=0:
            print(f"Intentos: {tries}")
            print(f"Progreso: {list_totaltry}")
            print(f"Letras correctas pero mal ordenadas: {list_goodtry}")
            print(f"Letras incorrectas: {list_failtry}")
            letter=input("Ingrese la letra.\n")
            if letter==i:
                print("Acertaste!\n")
                list_totaltry.append(letter)
                if letter in list_goodtry:
                    list_goodtry.remove(letter)
                break 
            elif (letter in word):
                print("La letra es correcta, pero no en esta posicion.")
                tries-=1
                list_goodtry.append(letter)
            else:
                print("La letra no es correcta. Perdiste un intento!")
                tries-=1
                list_failtry.append(letter)
    print(word)
    print(list_totaltry)
    if (word==list_totaltry):
        print("Acertaste la palabra!")
    else:
        print("No acertaste la palabra.")
    aux = input("Ingrese 1 para seguir jugando o 2 para terminar")
    if aux == 1:
        print("El juego continuara.")
    elif aux==2:
        print("El juego termino.")





# %%
