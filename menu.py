import random
from time import time



def menu():
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

    # print(aleatorios)
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
                    comparaciones = 0

                    t0 = time()
                    lista, comparaciones = insertionSort(aleatorios)
                    t1 = time()

                    print ("Lista ordenada:")
                    # print (lista, "\n")

                    print ("Tiempo: {0:f} segundos".format(t1 - t0))
                    print ("Comparaciones:", comparaciones)
                    break
                if case(2):

                    break
                if case(3):

                    break
                if case(4):

                    break
                if case(5):

                    break
                if case(6):

                    break
            break
        except ValueError:
            print("\n\n¡Opción invalida!\n\n")


def insertionSort(lista):
    n = len(lista)
    global comparaciones
    comparaciones = 0

    for i in range(1, n):
        val = lista[i]
        j = i

        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1
            comparaciones += 1

        lista[j] = val
    return lista, comparaciones

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
