#Done by me :3

import random

numero = random.randint(1, 100)

while True:

    respuesta = int(input("Adivina un numero del 1 al 100: ")) #No nos deja hacer mas adivinaciones a menos de que lo poganmos dentro de un while, donde el ciclo se va reptiendo, y nos deja eleegir nuevamente.

    if respuesta > numero:
        print("Tu respuesta es muy alta!")
    elif respuesta < numero:
        print("Tu respuesta es muy baja!")
    elif respuesta == numero:
        print("Tu respuesta es correcta, felicidades! Adivinaste :D")