# DONE BY ME :3

import random

def DiceRolling():   
 a = [1, 2, 3, 4, 5, 6]
 b = [1, 2, 3, 4, 5, 6]

 dice1 = random.choice(a)
 dice2 = random.choice(b)

 return(dice1, dice2)

while True:
 answer = input("Roll the dice? (y/n): ")
 if answer == 'y':
  print(DiceRolling())
 elif answer == 'n':
  print('Ending simulation.')
  break
 else: 
  print("Please, choose a valid choice!")