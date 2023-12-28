# Vamos a comparar dos algoritmos de busqueda.
# Dentro de una lista ordenada vamos a buscar un numero. 

# Navie_search: Recorreremos todo el listado hasta encontrar el numero deseado.
# Binary_search: Dividimos la lista en dos para reducir el tiempo de busqueda.

def navie_search(lista, objetivo):
    for x in range(len(lista)):
        if lista[x] == objetivo: return x
    return -1

if __name__ == "__main__":
    lista = range(100)
    objetivo = 40
    navie_search(lista , objetivo)

