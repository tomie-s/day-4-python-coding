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

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

if human_choice >= 3 or human_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
  print(game_images[human_choice])
  
  print("Computer chose:")
  print(game_images[computer_choice])
  
  if int(human_choice) == int(computer_choice):
    print("It's a draw")
  elif int(human_choice) == 0 and int(computer_choice) == 2:
    print("You win")
  elif int(human_choice) == 2 and int(computer_choice) == 0:
    print("You lose")
  elif int(human_choice) > int(computer_choice):
    print("You win")
