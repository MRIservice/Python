#!/usr/bin/python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("\nRock Paper Scisors Game\n")
print("=============================================")
print(rock, paper, scissors + "\n\n")

# Converted "pick" to int to be consistant with computer generated picks

pick = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if pick == 0:
    print('You have Selected "Rock"')
    print(rock)
elif pick == 1:
    print('You have Selected "Paper"')
    print(paper)
elif pick == 2:
    print('You have Selected "Scissors"')
    print(scissors)
else:
    print("You did not make a valid selection")

opponet = random.randint(0, 2)

if opponet == 0:
    print('Opponet Selected "Rock"')
    print(rock)
elif opponet == 1:
    print('Opponet Selected "Paper"')
    print(paper)
elif opponet == 2:
    print('Opponet Selected "Scissors"')
    print(scissors)
else:
    print("Opponet did not make a Selection")
    print(opponet)

if pick == opponet:
    print("This Game was a Draw Play again")
elif pick == 0 and opponet == 1:
    print("You Lose!")
elif pick == 0 and opponet == 2:
    print("You Win!")
elif pick == 1 and opponet == 0:
    print("You Win!")
elif pick == 1 and opponet == 2:
    print("You Lose!")
elif pick == 2 and opponet == 0:
    print("You Win!")
elif pick == 2 and opponet == 1:
    print("You Lose!")
