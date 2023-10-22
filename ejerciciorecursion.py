import random
def pathchoice(count):
    
    paths = [1,2,3]
    choice = random.choice(paths)
    if choice == 1:
        count+=3
        print(count)
        return pathchoice(count)
    elif choice == 2:
        count += 5
        print(count)
        return pathchoice(count)
    elif choice == 3:
        count += 7
        print(count)
    return count

secs = 0
print(f"La rata demoro {pathchoice(secs)}")

#Es una función recursiva que toma un número n y devuelve su representación como cadena de caracteres con los dígitos en orden inverso.