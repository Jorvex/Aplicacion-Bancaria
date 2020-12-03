# Juego de adivinar el número aleatorio.


import random
numero = random.randint(1,10)
intentos = 3

frase_inicial = "Intenta adivinar un número del 1 al 10, tienes 3 intentos!\n"
adivina = int(input(frase_inicial))

while intentos > 0:
    if adivina == numero:
        print("Genial! Lo has adivinado!")
        break
    else:
        intentos -=1
        if intentos >= 2:
            if adivina > numero:
                print(f"Incorrecto! Prueba con un número más pequeño...\nTe quedan {intentos} intentos")
                adivina = int(input())
            else:
                print(f"Incorrecto! Prueba con un número más grande...\nTe quedan {intentos} intentos")
                adivina = int(input())
        elif intentos == 1:
            if adivina > numero:
                print(f"Incorrecto! Prueba con un número más pequeño...\nTe queda {intentos} intento")
                adivina = int(input())
            else:
                print(f"Incorrecto! Prueba con un número más grande...\nTe queda {intentos} intento")
                adivina = int(input())
        else:
            yes_no = input("Has fallado 3 veces! Quieres volver a jugar? Y/N\n").lower()
            if yes_no == "y":
                intentos = 3
                adivina = None
                adivina = int(input(frase_inicial))
            else:
                print("Gracias por jugar!")
