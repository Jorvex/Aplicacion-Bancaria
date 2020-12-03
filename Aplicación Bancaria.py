# Aplicación Bancaria


def ingresar_dinero(saldo_total):
    saldo_ingresado = int(input("Introduce la cantidad que deseas ingresar: "))
    if saldo_ingresado <= 0:
        print(f"'{saldo_ingresado}' no es válido.")
        ingresar_dinero(saldo_total)
    else:
        if confirmar_operaciones("ingresar", saldo_ingresado):
            saldo_total += saldo_ingresado
            print("\nOperación realizada con éxito.\n")
            menu(saldo_total)
        else:
            print("\nOperación cancelada, volviendo al menú principal...\n")
            menu(saldo_total)


def extraer_dinero(saldo_total):
    saldo_extraido = int(input("Introduce la cantidad que deseas extraer: "))
    if saldo_extraido > 0:
        if saldo_total - saldo_extraido >= 0:
            if confirmar_operaciones("extraer", saldo_extraido):
                saldo_total -= saldo_extraido
                print("\nOperación realizada con éxito.\n")
                menu(saldo_total)
            else:
                print("\nOperación cancelada, volviendo al menú principal...\n")
                menu(saldo_total)
        else:
            print("¡No dispones de fondos suficientes!")
            extraer_dinero(saldo_total)
    else:
        print(f"'{saldo_extraido}' no es válido.")
        extraer_dinero(saldo_total)


def consultar_saldo(consulta_saldo):
    print(f"Tu saldo actual es de {consulta_saldo}€.\n")
    menu(consulta_saldo)


def confirmar_operaciones(operacion, cantidad):
    si_no = input(f"Estás seguro que deseas {operacion} {cantidad}€? S/N\n").upper()
    if si_no == "S":
        return True
    elif si_no == "N":
        return False
    else:
        print("Has introducido una opción incorrecta, "
              "vuelve a intentarlo con 'S' para confirmar o 'N' para cancelar la operación.")
        return confirmar_operaciones(operacion, cantidad)


def menu(saldo):
    print("1. Consultar el saldo.")
    print("2. Ingresar dinero.")
    print("3. Extraer dinero.")
    print("4. Salir de la aplicación...")
    pregunta = input()
    if pregunta == "1":
        consultar_saldo(saldo)
    elif pregunta == "2":
        ingresar_dinero(saldo)
    elif pregunta == "3":
        extraer_dinero(saldo)
    elif pregunta == "4":
        print("Saliendo de la aplicación...")
    else:
        print(f"'{pregunta}' no es una opción válida, utiliza los números '1', '2', '3' y '4'"
              f" para navegar por los menús.\n")
        menu(saldo)


saldo_inicial = 0
print("Bienvenido a mi aplicación bancaria en pruebas, que deseas hacer? "
      "(Utiliza los números para acceder a las opciones)\n")
menu(saldo_inicial)
