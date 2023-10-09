# Reto #0: EL FAMOSO "FIZZ BUZZ"


"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 
"""


def fizzBuuz():

    numeros = list(range(1, 101))

    for numero in numeros:
        multiplo_3 = numero % 3
        multiplo_5 = numero % 5

        if multiplo_3 == 0 and multiplo_5 == 0:
            numero = "fizzbuzz"
        elif multiplo_5 == 0:
            numero = "buzz"
        elif multiplo_3 == 0:
            numero = "fizz"

        print(numero)


fizzBuuz()
