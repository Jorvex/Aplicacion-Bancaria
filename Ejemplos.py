# Ejemplo de una función


""""
def multiplicacion(num1, num2):
    return num1 * num2


print(multiplicacion(2, 5))
"""

# Calculadora


"""
num1 = float(input("Escribe un número: "))
oper = input("Escribe el operador: ")
num2 = float(input("Escribe otro número: "))

if oper == "*":
    print("El resultado es: " + str(num1 * num2))
elif oper == "/":
    print("El resultado es: " + str(num1 / num2))
elif oper == "+":
    print("El resultado es: " + str(num1 + num2))
elif oper == "-":
    print("El resultado es: " + str(num1 - num2))
else:
    print("Escribe uno de estos operadores:\n + - * /")
"""

"""
dias_semana = "Lunes,Martes,Miercoles,Jueves,Sabado,Domingo".split(",")
for dia in dias_semana:
    if dia == "Jueves":
        print(True)
        break
"""

# Encriptador de frases


"""
caracter_elegido = "x"


def encriptador(frase, caracter):
    frase_encriptada = ""
    for letra in frase:
        if letra in "AEIOUaeiouÁÉÍÓÚáéíóú":
            if letra.isupper():
                frase_encriptada += caracter.upper()
            else:
                frase_encriptada += caracter.lower()
        else:
            frase_encriptada += letra
    return frase_encriptada


print(encriptador(input("Escribe una frase para encriptarla: "), caracter_elegido))
"""

# Ejemplo Función


"""
def masejemplotodavia(ejemplo1):
    print(f"Tengo el número {ejemplo1}")
    ejemplo1 += 5
    print(ejemplo1)
    return ejemplo1

ejemplo = 0
masejemplotodavia(ejemplo)
print(ejemplo)
"""

# Gestión de archivos

"""
archivo = open("C:users\Jordi Cruz\Desktop\prueba.txt", "x")
archivo.write("Hola, esto es un ejemplo\n"
              "de lo que se puede escribir.")

archivo.close()

# os.remove("C:users\Jordi Cruz\Desktop\prueba.txt")
"""

lista = [18,42,58,32,19,18,0,4,198,32,81]
lista.sort()


def busqueda_binaria(valor):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        puntero = (inicio + final) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None


def buscar_valor(valor):
    resultado = busqueda_binaria(valor)
    if resultado is None:
        print("El resultado no ha aparecido en la búsqueda.")
    else:
        print(f"El valor {valor} se encuentra en la posición {resultado}")


print(lista)
print(buscar_valor(19))
