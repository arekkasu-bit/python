lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))


tipo_triangulo = ""


if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    tipo_triangulo = "Lados no válidos"
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    tipo_triangulo = "Los lados no forman un triángulo"
elif   lado1 == lado2 == lado3:
    tipo_triangulo = "Equilátero"

else:
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"

# Salida
print(f"El triángulo es: {tipo_triangulo}")
