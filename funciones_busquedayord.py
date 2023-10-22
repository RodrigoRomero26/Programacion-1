def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array

def counting_sort(array):
    max_val = max(array)
    count = [0] * (max_val + 1)
    for num in array:
        count[num] += 1
    sorted_arr = []
    for i in range(max_val + 1):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1
    return sorted_arr

def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1

def binary_search(array, element):
    array = bubblesort(array)  #Se ordena el array de manera ascendente, si no, la busqueda binaria no funciona
    inicio = 0
    fin = len(array) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if array[medio] == element:
            return medio
        elif array[medio] < element:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
