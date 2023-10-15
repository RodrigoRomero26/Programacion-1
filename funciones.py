def add_digits(number):
    add=0
    while number!=0:
        digit = number%10
        add +=digit
        number //=10
    return add

def dnivalidator (num):
    if (len(num) == 7) or (len(num)==8):
        return True
    else:
        return False
    

def lastwordlen(word):
    splitstr = str(word).split(" ")
    return len(splitstr[-1])

def wordlen(word):
    return str(len(word))

def wordselector(phrase, pos):
    splitph = str(phrase).split(" ")
    return str(splitph[pos])

def idmaker (name, lastname, dni):
    import funciones
    num = funciones.wordlen(lastname)
    aux = str(name) + str(num) + str(dni[0:3])
    return aux

def ismult(num1,num2):
    if (num1%num2 == 0):
        return True
    else:
        return False

def medtemp(temp1, temp2):
    temp = temp1 + temp2
    return round(temp/2,1)

def letterbyletter(phrase):
    phrspaced = ""
    for i in phrase:
        if i == " ":
            phrspaced+=i
        else:
            phrspaced+=i+" "
    return str(phrspaced)

def minmaxlist(numlist):
    maxmin= []
    maxmin.append(min(numlist))
    maxmin.append(max(numlist))
    return maxmin

def areandper(radio):
    import math
    area = round(math.pi*float(radio)**2,2)
    peri = round(2*math.pi*float(radio),2)
    aux = []
    aux.append(area)
    aux.append(peri)
    return aux

def login(user, password, tries):
    if user == "usuario1" and password == "asdasd":
        return True, tries
    else:
        tries += 1
        return False, tries

def discart(cart):
    total = 0
    for prod, discount in cart.items():
        discounted = prod - (prod * (discount / 100))
        total+=discounted
    return total

def double(num):
    return num*2

def listchanger(list1, func):
    backlist = []
    for i in list1:
        aux = func(i)
        backlist.append(aux)
    return backlist

def phraselen(phrase):
    splitedphrase = phrase.split()
    dicc = {i: len(i) for i in splitedphrase}
    return dicc

def modcalc(x,y):
    return (x**2 + y**2)

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def getnumbers ():
    import funciones
    cont = 0
    while True:
        num = int(input("Ingrese un numero: "))
        if num == 0:
            break
        else:
            cont+=1
            print(f"El factorial de este numero es {funciones.factorial(num)}")
    return cont

def factorial (num):
    if num==0 or num==1:
            result=1
    elif num>1:
            result=num*factorial(num-1)
    return result

def digitcount (num, digit):
    aux = str(num).count(str(digit))
    return aux

def listmaker (list, cond):
    while True:
        name = input(f"Ingrese su dato. Ingrese {cond} para terminar.").title()
        if name==cond:
            return list
        else:
            list.append(name)

def listmakenoreps(list):
    listnorep = []
    for i in list:
        conf = any(i == name for name in listnorep)
        if not conf:
            listnorep.append(i)
    return listnorep

def listshow(list):
    for name in list:
        print(name, end=", ")
    print(" ")

def showreps(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2

def shownoreps(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 - set2