# PROGRAMA QUE PIDE UN TEXTO Y LO IMPRIME
texto = input("Ingresa un texto: ").upper()
textoCondicion = "HOLA"



if texto == textoCondicion:
    print("SON IGUALES")
else:
    print("NO SON IGUALES")

# ADICION DEL ELIF

texto2 = input("Ingresa un texto: ").lower() # O .lower


if texto.isupper():
    print("El texto esta en mayusculas")
elif texto.islower():
    print("El texto esta en espacio")
else:
    print("El texto no esta en mayusculas ni en espacio")

# VERIFICAR SI ES SOLO TEXTO O NUMERO

# numeroRomano = input("Ingresa un numero ROMANO: ").upper()
# if numeroRomano.isnumeric():
#     print(f"Tu numero es {numeroRomano}")
# else:
#     print("Por favor ingresa un numero de celular valido")
# Ⅻ

# VERIFICAR IS DIGIT

digitoUsuario = input("Ingresa un digito: ")

if digitoUsuario.isdigit():
    print(f"Tu digito es {digitoUsuario}")
else:
    print("Por favor ingresa un digito valido")
