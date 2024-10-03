#PROMEDIO SI PASO O NO PASO LA MATERIA

calificacion1 = int(input("Ingresa tu calificación 1: "))
calificacion2 = int(input("Ingresa tu calificación 2: "))
calificacion3 = int(input("Ingresa tu calificación 3: "))


if  0 >= calificacion1 <= 5 and 0 >= calificacion2 <= 5 and 0 >= calificacion3 <= 5:

    promedio = (calificacion1 + calificacion2 + calificacion3) / 3
    if promedio >= 3:
        print(f"Tu promedio es {promedio} y has aprobado la materia")
    else:
        print(f"Tu promedio es {promedio} y has reprobado la materia")

else:
    print("Calificación no válida")
