#PRIMERO

# Solicitar peso y altura
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el Índice de Masa Corporal (IMC)
imc = peso / (altura ** 2)

# Clasificar el IMC
if imc < 18.5:
    print(f"Tu IMC es {imc}. Estás en la categoría de bajo peso.")
elif imc >= 18.5 and imc < 24.9:
    print(f"Tu IMC es {imc}. Estás en la categoría de peso normal.")
elif imc >= 24.9 and imc < 29.9:
    print(f"Tu IMC es {imc}. Estás en la categoría de sobrepeso.")
else:
    print(f"Tu IMC es {imc}. Estás en la categoría de obesidad.")

# OR




primerProducto = float(input("Ingrese el precio del primer producto: "))
segundoProducto = float(input("Ingrese el precio del segundo producto: "))
tercerProducto = float(input("Ingrese el precio del tercer producto: "))

edad = int(input("Ingresa tu edad: "))
es_miembro = input("¿Tienes tarjeta de miembro? (si/no): ").lower() == "si"


# Verificar si es elegible para el descuento

totalCompra = primerProducto + segundoProducto + tercerProducto

if not edad > 65 or es_miembro:
    totalCompra = totalCompra-(totalCompra * 0.9)
    print(f"tu compra con el descuento es de: {totalCompra}")
# if edad > 65 or es_miembro:
#     totalCompra = totalCompra-(totalCompra * 0.9)
#     print(f"tu compra con el descuento es de: {totalCompra}")
else:
    print(f"Tu compra no tendra descuento, debes pagar: {totalCompra}")

