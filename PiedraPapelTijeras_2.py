# Condiciones del juego:
# Si elige una opcion que no es las que son dadas, imprime opcion invalida
# Debe darnos a opcion de continuar jugando 
# Piedra vence tijeras 
# Tijeras vence papel
# Papel vence piedra
# la maquina debe elegir una opcion tambien
# hacer todo paso por paso

import random

def jugar():
      
    piedra = 'piedra'
    papel = 'papel'
    tijeras = 'tijeras'

    opciones = [piedra, papel, tijeras]

    while True:
     comienzo = input('Jugamos? (si/no)').lower()
     if comienzo != 'si':
        print("Saliendo del juego...")
        break
     
     maquina = random.choice(opciones)
     jugador = input("Elija una opcion (piedra/papel/tijeras): ")

     if maquina == jugador:
       print("Empate!")
       
     elif (jugador == 'piedra' and maquina == 'tijeras') or (jugador == 'tijeras' and maquina == 'papel') or (jugador == 'papel' and maquina == 'piedra'):
        print("Ganaste!")
     elif jugador != opciones:
        print("Elija una opcion valida.")
     else: 
        denuevo = input("perdiste :( Seguir jugando? )")
        if denuevo != 'si':
           break
        


jugar()