import random, threading
import numpy as np
from time import time
# import math



def menu():
    global comparaciones, num_cantidad
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
                    num_cantidad = 1000000
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

    num_hilos = num_cantidad // 1000
    # print(aleatorios)
    # print ("Tiempo: {0:f} segundos".format(t1 - t0))

    while True:
        print("\n\n[METODOS DE ORDENAMIENTO EN PYTHON] \n")
        print("1.[Insercion (insertionsort)]")
        print("2.[Mezcla (merge)]")
        print("3.[montones (heap sort)]")
        print("4.[rapido (quicksort)]")
        print("5.[conteo (couting sort)]")
        print("6.[radix sort]\n\n")
        print("[THREADS]")
        print("7.[Insercion (insertionsort)]")
        print("8.[Mezcla (merge)]")
        print("9.[montones (heap sort)]")
        print("10.[rapido (quicksort)]")
        print("11.[conteo (couting sort)]")
        print("12.[radix sort]")
        try:
            option = input("\nElige tu opción: ")

            if int(option) > 12:
                option = 'num'

            option = int(option)
            while switch(option):
                if case(1):
                    t0 = time()
                    t2 = time()
                    lista = insertionSort(aleatorios)
                    t1 = time()

                    break
                if case(2):
                    t0 = time()
                    t2 = time()
                    lista = mergeSort(aleatorios)
                    t1 = time()

                    break
                if case(3):
                    t0 = time()
                    t2 = time()
                    lista = heapsort(aleatorios)
                    t1 = time()

                    break
                if case(4):
                    t0 = time()
                    t2 = time()
                    lista = quicksort(aleatorios, 0, len(aleatorios)-1)
                    t1 = time()

                    break
                if case(5):
                    t0 = time()
                    t2 = time()
                    lista = countingsort(aleatorios)
                    t1 = time()

                    break
                if case(6):
                    t0 = time()
                    t2 = time()
                    lista = radixsort(aleatorios)
                    t1 = time()

                    break
                if case(7):
                    t0 = time()
                    t2 = time()
                    lista = np.array_split(aleatorios,num_hilos)

                    for i in range(0, num_hilos):
                        hilo = threading.Thread(target=insertionSort, args=(lista[i],))
                        hilo.setDaemon = True
                        hilo.start()

                    for i in range(0, num_hilos):
                        hilo.join()

                    lista = np.concatenate(lista)
                    lista = insertionSort(lista)
                    t1 = time()

                    break
                if case(8):
                    t0 = time()
                    t2 = time()
                    lista = np.array_split(aleatorios,num_hilos)

                    for i in range(0, num_hilos):
                        hilo = threading.Thread(target=mergeSort, args=(lista[i],))
                        hilo.setDaemon = True
                        hilo.start()

                    for i in range(0, num_hilos):
                        hilo.join()

                    lista = np.concatenate(lista)
                    lista = mergeSort(lista)
                    t1 = time()

                    break
                if case(9):
                    t0 = time()
                    t2 = time()
                    lista = np.array_split(aleatorios,num_hilos)

                    for i in range(0, num_hilos):
                        hilo = threading.Thread(target=heapsort, args=(lista[i],))
                        hilo.setDaemon = True
                        hilo.start()

                    for i in range(0, num_hilos):
                        hilo.join()

                    lista = np.concatenate(lista)
                    lista = heapsort(aleatorios)
                    t1 = time()

                    break
                # if case(10):
                #     t0 = time()
                #     t2 = time()
                #     lista = np.array_split(aleatorios,num_hilos)
                #
                #     for i in range(0, num_hilos):
                #         hilo = threading.Thread(target=insertionSort, args=(lista[i],))
                #         hilo.setDaemon = True
                #         hilo.start()
                #
                #     for i in range(0, num_hilos):
                #         hilo.join()
                #
                #     lista = np.concatenate(lista)
                #     lista = insertionSort(lista)
                #     t1 = time()
                #
                #     break
                # if case(11):
                #     t0 = time()
                #     t2 = time()
                #     lista = np.array_split(aleatorios,num_hilos)
                #
                #     for i in range(0, num_hilos):
                #         hilo = threading.Thread(target=insertionSort, args=(lista[i],))
                #         hilo.setDaemon = True
                #         hilo.start()
                #
                #     for i in range(0, num_hilos):
                #         hilo.join()
                #
                #     lista = np.concatenate(lista)
                #     lista = insertionSort(lista)
                #     t1 = time()
                #
                #     break
                # if case(12):
                #     t0 = time()
                #     t2 = time()
                #     lista = np.array_split(aleatorios,num_hilos)
                #
                #     for i in range(0, num_hilos):
                #         hilo = threading.Thread(target=insertionSort, args=(lista[i],))
                #         hilo.setDaemon = True
                #         hilo.start()
                #
                #     for i in range(0, num_hilos):
                #         hilo.join()
                #
                #     lista = np.concatenate(lista)
                #     lista = insertionSort(lista)
                #     t1 = time()
                #
                #     break
            break
        except ValueError:
            print("\n\n¡Opción invalida!\n\n")

    print ("Lista ordenada:")
    print (lista, "\n")
    t3 = time()

    print ("Tiempo: {0:f} segundos".format(t1 - t0))
    print ("Tiempo: {0:f} segundos".format(t3 - t2))

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
    global comparaciones
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
        comparaciones += 1
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
def countingsort(unsorted):
   result = [0] * len(unsorted)
   low = min(unsorted)      # we don't care if this is positive or negative any more!
   high = max(unsorted)
   count_array = [0 for i in range(low, high+1)]
   for i in unsorted:
      count_array[i-low] += 1             # use an offset index
   for j in range(1, len(count_array)):
      count_array[j] += count_array[j-1]
   for k in reversed(unsorted):
      result[count_array[k-low] - 1] = k  # here too
      count_array[k-low] -= 1             # and here
   return result
################################################################################
def radix_sort_nonneg(lst):
    RADIX = 10
    last_iteration = False
    radix_power = 1
    while not last_iteration:
        # split into buckets
        buckets = [[] for _ in range(RADIX)]
        last_iteration = True  # unless we find it isn't
        for el in lst:
            # find the digit corresponding to radix_power
            #  example with radix_power = 1000; el = 123456
            #  el % (radix_power*RADIX) == 123456 % 10000 == 3456
            #  3456 // radix_power == 3456 // 1000 == 3
            digit = el % (radix_power*RADIX) // radix_power
            buckets[digit].append(el)
            if el >= radix_power*RADIX:
                last_iteration = False

        # flatten
        lst = [el for bucket in buckets for el in bucket]
        radix_power *= RADIX
    return lst


def radixsort(lst):
    positive_ints = radix_sort_nonneg( x for x in lst if x >= 0)
    negative_ints = radix_sort_nonneg(-x for x in lst if x <  0)
    return [-x for x in reversed(negative_ints)] + positive_ints
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
