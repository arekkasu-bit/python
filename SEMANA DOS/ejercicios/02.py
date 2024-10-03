# PAR O IMPAR MEJORADO
numeroUsuario = input("Ingresa un numero: ")

if numeroUsuario.isdigit():

    numeroUsuario = int(numeroUsuario)

    if numeroUsuario % 2 == 0:
        print(f"El numero {numeroUsuario} es par\n")
    else:
        print(f"Tu numero {numeroUsuario} es impar\n")
else:
    print("Por favor ingresa un numero valido")
