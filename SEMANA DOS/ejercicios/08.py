import random as r

numeroAleatorio = r.randint(1,20)
numeroUsuario = int(input("Adivina el numero entre 1 y 20: "))
if numeroUsuario ==  numeroAleatorio:
    print("¡Felicidades! Adivinaste el número")
else:
    print(f"Lo siento, el número era {numeroAleatorio}")
