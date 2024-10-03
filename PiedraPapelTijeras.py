
#No acepta nada que no sea piedra, papel o tijeras
# piedra > papel, tijeras > papel, tijeras > piedra
# La maquina debe elegir una opcion tambien
# Debe preguntarnos si queremos seguir jugando

import random

def jugar():

    piedra = 'piedra'
    papel = 'papel'
    tijeras = 'tijeras'

    opciones = [piedra, papel, tijeras]

    while True:
     
      comienzo = input("Deseas jugar? (si/no): ")

      eleccion_maquina = random.choice(opciones)
      eleccion_jugador = input("Elija una de las optiones -> (piedra/papel/tijeras): ")
      
      if comienzo == 'si':
        (eleccion_jugador == piedra and eleccion_maquina == tijeras) or (eleccion_jugador == tijeras and eleccion_maquina == papel) or (eleccion_jugador == papel and eleccion_maquina == piedra)
        print("Ganaste, bien hecho!")

jugar()