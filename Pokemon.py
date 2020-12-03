import random
import time


class Pokemon:
    def __init__(self, nombre, tipo, ataque, agilidad):
        self.nombre = nombre
        self.tipo = tipo
        self.agilidad = agilidad
        self.ataque = ataque
        self.vida = 100


p1 = Pokemon("Charizard", "Fuego", 15, 1)
p2 = Pokemon("Venusaur", "Planta", 15, 1)
p3 = Pokemon("Blastoise", "Agua", 15, 1)
p4 = Pokemon("Pikachu", "Eléctrico", 5, 5)


def eficacia_tipo(pokemon1, tipo1, pokemon2, tipo2):
    if pokemon1.tipo == "Fuego" and pokemon2.tipo == "Planta":
        time.sleep(2)
        print(f"Los ataques de {pokemon1.nombre} ({tipo1}) "
              f"son muy eficaces frente a {pokemon2.nombre} {pokemon2.tipo2}!\n")
        pokemon1.ataque *= 2
    elif pokemon2.tipo == "Fuego" and pokemon1.tipo == "Planta":
        time.sleep(2)
        print(f"Los ataques de {pokemon2.nombre} ({tipo2}) "
              f"son muy eficaces frente a {pokemon1.nombre} ({tipo1})!\n")
        pokemon2.ataque *= 2
    elif pokemon1.tipo == "Agua" and pokemon2.tipo == "Fuego":
        time.sleep(2)
        print(f"Los ataques de {pokemon1.nombre} ({tipo1}) "
              f"son muy eficaces frente a {pokemon2.nombre} ({tipo2})!\n")
        pokemon1.ataque *= 2
    elif pokemon2.tipo == "Agua" and pokemon1.tipo == "Fuego":
        time.sleep(2)
        print(f"Los ataques de {pokemon2.nombre} ({tipo2}) "
              f"son muy eficaces frente a {pokemon1.nombre} ({tipo1})!\n")
        pokemon2.ataque *= 2
    elif pokemon1.tipo == "Planta" and pokemon2.tipo == "Agua":
        time.sleep(2)
        print(f"Los ataques de {pokemon1.nombre} ({tipo1}) "
              f"son muy eficaces frente a {pokemon2.nombre} ({tipo2})!\n")
        pokemon1.ataque *= 2
    elif pokemon2.tipo == "Planta" and pokemon1.tipo == "Agua":
        time.sleep(2)
        print(f"Los ataques de {pokemon2.nombre} ({tipo2}) "
              f"son muy eficaces frente a {pokemon1.nombre} ({tipo1})!\n")
        pokemon1.ataque *= 2
    elif pokemon1.tipo == "Eléctrico" and pokemon2.tipo == "Agua":
        time.sleep(2)
        print(f"Los ataques de {pokemon1.nombre} ({tipo1}) "
              f"son muy eficaces frente a {pokemon2.nombre} ({tipo2})!\n")
        pokemon1.ataque *= 2
    elif pokemon2.tipo == "Eléctrico" and pokemon1.tipo == "Agua":
        time.sleep(2)
        print(f"Los ataques de {pokemon2.nombre} ({tipo2}) "
              f"son muy eficaces frente a {pokemon1.nombre} ({tipo1})!\n")
        pokemon2.ataque *= 2


def esquive1(pokemon1):
    if pokemon1.agilidad == 1:
        dado = random.randint(1, 10)
        i = 2
        if dado == i:
            return True
    elif pokemon1.agilidad == 2:
        dado = random.randint(1, 8)
        i = 2
        if dado == i:
            return True
    elif pokemon1.agilidad == 3:
        dado = random.randint(1, 6)
        i = 2
        if dado == i:
            return True
    elif pokemon1.agilidad == 4:
        dado = random.randint(1, 4)
        i = 2
        if dado == i:
            return True
    elif pokemon1.agilidad == 5:
        dado = random.randint(1, 2)
        i = 2
        if dado == i:
            return True


def esquive2(pokemon2):
    if pokemon2.agilidad == 1:
        dado = random.randint(1, 10)
        i = 2
        if dado == i:
            return True
    elif pokemon2.agilidad == 2:
        dado = random.randint(1, 8)
        i = 2
        if dado == i:
            return True
    elif pokemon2.agilidad == 3:
        dado = random.randint(1, 6)
        i = 2
        if dado == i:
            return True
    elif pokemon2.agilidad == 4:
        dado = random.randint(1, 4)
        i = 2
        if dado == i:
            return True
    elif pokemon2.agilidad == 5:
        dado = random.randint(1, 2)
        i = 2
        if dado == i:
            return True


def combate(pokemon1, pokemon2):
    pokemon1.vida = 100
    pokemon2.vida = 100
    turno = random.randint(1, 2)

    print(f"\n===={pokemon1.nombre} VS {pokemon2.nombre}====\n")
    print("Que empiece el combate!!!\n")
    eficacia_tipo(pokemon1, pokemon1.tipo, pokemon2, pokemon2.tipo)

    while pokemon1.vida > 0 and pokemon2.vida > 0:
        time.sleep(4)
        if turno == 1:
            if esquive1(pokemon1):
                print(f"{pokemon2.nombre} esquivó el ataque de {pokemon1.nombre}!")
            else:
                pokemon2.vida -= pokemon1.ataque
                if pokemon2.vida > 0:
                    print(f"{pokemon1.nombre} ataca! {pokemon2.vida} Puntos de Salud restantes para {pokemon2.nombre}.")
                else:
                    print(f"{pokemon1.nombre} ataca y {pokemon2.nombre} se debilitó! "
                          f"{pokemon1.nombre} es el ganador!")
            print("\n==== SIGUIENTE RONDA ====")
            turno = 2
        else:
            if esquive1(pokemon2):
                print(f"{pokemon1.nombre} esquivó el ataque de {pokemon2.nombre}!")
            else:
                pokemon1.vida -= pokemon2.ataque
                if pokemon1.vida > 0:
                    print(f"{pokemon2.nombre} ataca! {pokemon1.vida} Puntos de Salud restantes para {pokemon1.nombre}.")
                else:
                    print(f"{pokemon2.nombre} ataca y {pokemon1.nombre} se debilitó! "
                          f"{pokemon2.nombre} es el ganador!")
            print("\n==== SIGUIENTE RONDA ====")
            turno = 1


print(p1.nombre, "-", p2.nombre, "-", p3.nombre, "-", p4.nombre)

jugador = input("Escoge tu Pokémon! ").lower()
if jugador == "charizard":
    combate(p1, random.choice([p2, p3, p4]))
elif jugador == "venusaur":
    combate(p2, random.choice([p1, p3, p4]))
elif jugador == "blastoise":
    combate(p3, random.choice([p1, p2, p4]))
else:
    combate(p4, random.choice([p1, p2, p3]))
