# Vamos a comparar dos algoritmos de busqueda.
# Dentro de una lista ordenada vamos a buscar un numero. 

# Navie_search: Recorreremos todo el listado hasta encontrar el numero deseado.
# Binary_search: Dividimos la lista en dos para reducir el tiempo de busqueda.

import time
import random

def navie_search(lista, objetivo):
    for x in range(len(lista)):
        if lista[x] == objetivo: return x
    return -1

def binary_search(lista, objetivo, min = None, max = None):
    if min == None: min = 0
    if max == None: max = len(lista)
    if min > max: return -1
  
    mid = (min + max) // 2

    if objetivo == lista[mid]:
        return mid
    elif objetivo > lista[mid]:
        return binary_search(lista, objetivo, mid+1, max)
    else:
        return binary_search(lista, objetivo, min, mid-1)
    return -1

if __name__ == "__main__":
    lista = range(100000)
    objetivo = random.randint(0, 100000)

    start = time.time()
    for n in range(500):
        navie_search(lista , objetivo)
    end = time.time()
    print ("Total Navie Search: ", end - start)
    print ("Navie Search: ", (end - start)/500)

    start = time.time()
    for n in range(500):
        binary_search(lista , objetivo)
    end = time.time()
    print ("Total Binary Search: ", end - start)
    print ("Binary Search: ", (end - start)/500)
