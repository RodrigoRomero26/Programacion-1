import Fc_ahorcado
word = Fc_ahorcado.wordselecter()
tries = 6
letters = []

print ("Comienza el juego del ahorcado. \n")

while tries > 0:
    board = Fc_ahorcado.boardshow(word, letters)
    print(f"Palabra: {board}")
    letter = input("Ingresa tu letra").lower()

    if len(letter) != 1 or not letter.isalpha():
        print ("Ingrese una letra valida.")
        continue

    if letter in letters:
        Fc_ahorcado.lettershow(letters)
        print("Ya adivinaste esta letra.")
        continue

    letters.append(letter)

    if letter in word:
        Fc_ahorcado.lettershow(letters)
        print("Adivinaste!")
    else:
        tries -=1
        Fc_ahorcado.lettershow(letters)
        print(f"Letra incorrecta. Te quedan {tries} intentos.")

    if "_" not in Fc_ahorcado.boardshow(word,letters):
        print(f"Ganaste! Tu palabra era: {word}")
        break

if tries == 0:
    print(f"Perdiste! Tu palabra era {word}")