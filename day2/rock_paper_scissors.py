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

choose = [rock, paper, scissors]

player_choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors\n"))
computer_choice = random.randint(0, 2)

if player_choice == 0 and computer_choice == 1:
    print(f"You: {choose[player_choice]}\nComputer: {choose[computer_choice]}\nYou lose")
elif player_choice == 0 and computer_choice == 2:
    print(f"You: {choose[player_choice]}\nComputer: {choose[computer_choice]}\nYou win")
elif player_choice == 1 and computer_choice == 0:
    print(f"You: {choose[player_choice]}\nComputer: {choose[computer_choice]}\nYou win")
elif player_choice == 1 and computer_choice == 2:
    print(f"You: {choose[player_choice]}\nComputer: {choose[computer_choice]}\nYou lose")
elif player_choice == 2 and computer_choice == 0:
    print(f"You: {choose[player_choice]}\nComputer: {choose[computer_choice]}\nYou lose")
elif player_choice == 2 and computer_choice == 1:
    print(f"You: {choose[player_choice]}\nComputer: {choose[computer_choice]}\nYou win")
elif player_choice == computer_choice:
    print(f"You: {choose[player_choice]}\nComputer: {choose[computer_choice]}\nDraw")
else:
    print("ERROR")