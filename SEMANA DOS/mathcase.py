numero = input("Ingresa por favor un digito: ")

# PROBAR TAMBIEN CON NUMERO
match numero:
    case "2":
        print("Tu numero es 2")
    case "3":
        print("Tu numero es 3")
    case _:
        print("Tu numero no es 3")
