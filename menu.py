import random
from time import time
import math



def menu():
    global comparaciones
    comparaciones = 0

    print("[METODOS DE ORDENAMIENTO EN PYTHON] \n")

    while True:
        print("Ingrese cuantos numeros aleatorios desea obtener\n")
        print("1.[1 millon]")
        print("2.[2 millones]")
        print("3.[5 millones]")
        print("4.[10 millones]")
        print("5.[20 millones]")
        try:
            option = input("\nElige tu opción: ")

            if int(option) > 5:
                option = 'num'

            option = int(option)
            while switch(option):
                if case(1):
                    num_cantidad = 50
                    break
                if case(2):
                    num_cantidad = 2000000
                    break
                if case(3):
                    num_cantidad = 5000000
                    break
                if case(4):
                    num_cantidad = 10000000
                    break
                if case(5):
                    num_cantidad = 20000000
                    break
            break
        except ValueError:
            print("\n\n¡Opción invalida!\n\n")
    t0 = time()

    aleatorios = [random.randint(-99999,99999) for _ in range(num_cantidad)]

    t1 = time()

    print(aleatorios)
    print ("Tiempo: {0:f} segundos".format(t1 - t0))

    while True:
        print("\n\n[METODOS DE ORDENAMIENTO EN PYTHON] \n")
        print("1.[Insercion (insertionsort)]")
        print("2.[Mezcla (merge)]")
        print("3.[montones (heap sort)]")
        print("4.[rapido (quicksort)]")
        print("5.[conteo (couting sort)]")
        print("6.[radix sort]")
        try:
            option = input("\nElige tu opción: ")

            if int(option) > 6:
                option = 'num'

            option = int(option)
            while switch(option):
                if case(1):
                    t0 = time()
                    lista = insertionSort(aleatorios)
                    t1 = time()

                    break
                if case(2):
                    t0 = time()
                    lista = mergeSort(aleatorios)
                    t1 = time()

                    break
                if case(3):
                    t0 = time()
                    lista = heapsort(aleatorios)
                    t1 = time()

                    break
                if case(4):
                    t0 = time()
                    lista = quicksort(aleatorios, 0, len(aleatorios)-1)
                    t1 = time()

                    break
                if case(5):
                    t0 = time()
                    lista = countingsort(aleatorios, 99999)
                    t1 = time()

                    break
                if case(6):
                    t0 = time()
                    lista = radixsort(aleatorios)
                    t1 = time()

                    break
            break
        except ValueError:
            print("\n\n¡Opción invalida!\n\n")

    print ("Lista ordenada:")
    print (lista, "\n")

    print ("Tiempo: {0:f} segundos".format(t1 - t0))
    print ("Comparaciones:", comparaciones)
################################################################################
def insertionSort(lista):
    n = len(lista)
    global comparaciones

    for i in range(1, n):
        val = lista[i]
        j = i

        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1
            comparaciones += 1

        lista[j] = val
    return lista
################################################################################
def mergeSort(lista):

    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergeSort(izquierda)
    derecha = mergeSort(derecha)

    return merge(izquierda, derecha)

def merge(listaA, listaB):
    global comparaciones

    lista_nueva = []
    a = 0
    b = 0

    while a < len(listaA) and b < len(listaB):
        comparaciones += 1

        if listaA[a] < listaB[b]:
            lista_nueva.append(listaA[a])
            a += 1
        else:
            lista_nueva.append(listaB[b])
            b += 1

    while a < len(listaA):
        lista_nueva.append(listaA[a])
        a += 1

    while b < len(listaB):
        lista_nueva.append(listaB[b])
        b += 1

    return lista_nueva
################################################################################
def heapsort(A):
    def sift_down(A, parent, upto):
        larger = 2 * parent + 1
        while larger < upto:
            if A[larger] < A[larger + 1]:
                larger += 1
            if A[larger] > A[parent]:
                A[larger], A[parent] = A[parent], A[larger]
                parent = larger
                larger = 2 * parent + 1
            else:
                break
    last_node = len(A) - 1
    last_parent = last_node // 2
    [ sift_down(A, i, last_node) for i in range(last_parent, -1, -1) ]
    for i in range(last_node, 0, -1):
        if A[0] > A[i]:
            A[0], A[i] = A[i], A[0]
            sift_down(A, 0, i - 1)
    return A
################################################################################
def quicksort(lista, izq, der):
    if izq < der:
    	pivote_indice = particion(lista, izq, der)
    	quicksort(lista, izq, pivote_indice-1)
    	quicksort(lista, pivote_indice+1, der)
    return lista

def particion(lista, izq, der):
    global comparaciones

    pivote = lista[der]
    indice = izq


    for i in range(izq, der):
        comparaciones += 1

        if lista[i] <= pivote:
            lista[indice], lista[i] = lista[i], lista[indice]
            indice += 1

    lista[indice], lista[der] = lista[der], lista[indice]
    return indice
################################################################################
def countingsort(array1, max_val):
    global comparaciones
    m = max_val
    count = [0] * m

    for a in array1:
    # count occurences
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i += 1
            comparaciones += 1

    return array1
################################################################################

################################################################################

################################################################################



################################################################################
#SWITCH
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

if __name__ == "__main__":
    menu()
