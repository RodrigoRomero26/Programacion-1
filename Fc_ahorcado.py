import random
def wordselecter():
    words_list = ["programa", "computadora", "monitor", "programacion"]
    return (random.choice(words_list))

def boardshow(word, letters):
    board = ""
    for i in word:
        if i in letters:
            board += i
        else:
            board += "_"
    return board

def lettershow(letters):
    print("Ingresaste: ", end="")
    for i in letters:
        print(i, end=" ")
    print (" ")
