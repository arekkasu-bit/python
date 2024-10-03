# PROGRAMA QUE DETECTE SI UN NUMERO ESTA EN UN RANGO Y SI ES PAR O IMPAR

numeroUsuario = int(input("Introduce un número: "))

if numeroUsuario in range(101):
    print("El número está en el rango de 0 a 100")
else:
    print("El número no está en el rango de 0 a 100")
