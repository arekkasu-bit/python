print("Bienvenido a la cafetería")
print("1. Café")
print("2. Té")
print("3. Chocolate caliente")

opcion = int(input("Por favor, elige una opción (1-3): "))

match opcion:
    case 1:
        tamaño = input("¿Qué tamaño de café quieres? (pequeño, mediano, grande): ")
        if tamaño == "pequeño":
            print("Has elegido un café pequeño.")
        elif tamaño == "mediano":
            print("Has elegido un café mediano.")
        elif tamaño == "grande":
            print("Has elegido un café grande.")
        else:
            print("Opción no válida.")
    case 2:
        print("Has elegido té.")
    case 3:
        print("Has elegido chocolate caliente.")
    case _:
        print("Opción no válida.")
