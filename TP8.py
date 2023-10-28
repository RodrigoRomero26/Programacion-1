def diggit_count(number):
    if number < 10:
        return 1
    else:
        return 1 + diggit_count(number // 10)

def ispower(n, b):
    if n < 1 or b < 2:
        return False
    if n == 1:
        return True
    if n % b != 0:
        return False
    return ispower(n / b, b)

def find_positions(a, b, start=0, positions=None):
    if positions is None:
        positions = []
    pos = a.find(b, start)
    if pos == -1:
        return positions
    positions.append(pos)
    return find_positions(a, b, pos + 1, positions)

def evennumber(n):
    if n == 0:
        return True
    else:
        return oddnumber(n - 1)

def oddnumber(n):
    if n == 0:
        return False
    else:
        return evennumber(n - 1)

def findmax(list_1):
    if len(list_1) == 1:
        return list_1[0]
    else:
        rest = findmax(list_1[1:])
        if list_1[0] > rest:
            return list_1[0]
        else:
            return rest

def listrepeater(list_1, n):
    if not list_1 or n == 0:
        return []
    return [list_1[0]] * n + listrepeater(list_1[1:], n)

def k (n,p):
    if n == 1:
        return p
    else:
        return n * p + k(n - 1, p)

def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

def combinations(list_1, k, actualstring=""):
    if k == 0:
        print(actualstring)
        return
    for char in list_1:
        combinations(list_1, k - 1, actualstring + char)

def medidas_hoja_A(N):
    if N == 0:
        return (841, 1189)
    prev_width, prev_length = medidas_hoja_A(N - 1)
    new_length = prev_length
    new_width = prev_width // 2
    return (new_length, new_width)

