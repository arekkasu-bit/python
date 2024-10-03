numerador = input("Digite o numerador: ")
denominador = input("Digite o denominador: ")

if numerador.isdigit() and denominador.isdigit():
    numerador = int(numerador)
    denominador = int(denominador)
    resultado = numerador / denominador
    if denominador != 0:
        print(f"El resultado de la division es: {resultado}")
    else:
        print("No se puede dividir por cero")
else:
    print("Por favor, digite un número válido")
