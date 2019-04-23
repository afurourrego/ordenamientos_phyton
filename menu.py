




def menu():
    print("[METODOS DE ORDENAMIENTO EN PYTHON] \n")

    while True:
        print("1.[Insercion (insertion sort)]")
        print("2.[Mezcla (merge)]")
        print("3.[montones (heap sort)]")
        print("4.[rapido (quicksort)]")
        print("5.[conteo (couting sort)]")
        print("6.[radix sort]")
        try:
            option = input("\nElige tu opción: ")
            option = int(option)
            while switch(option):
                if case(1):

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
