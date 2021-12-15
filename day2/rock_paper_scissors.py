import random

player_choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors\n"))
computer_choice = random.randint(0, 2)

if player_choice == 0 and computer_choice == 1:
    print("Your choice is rock\n\nComputer choice is paper\nYou lose")
elif player_choice == 0 and computer_choice == 2:
    print("Your choice is rock\n\nComputer choice is scissors\nYou win")
elif player_choice == 1 and computer_choice == 0:
    print("Your choice is paper\n\nComputer choice is rock\nYou win")
elif player_choice == 1 and computer_choice == 2:
    print("Your choice is paper\n\nComputer choice is scissors\nYou lose")
elif player_choice == 2 and computer_choice == 0:
    print("Your choice is scissors\n\nComputer choice is rock\nYou lose")
elif player_choice == 2 and computer_choice == 1:
    print("Your choice is scissors\n\nComputer choice is paper\nYou win")
elif player_choice == computer_choice:
    print("Draw")
else:
    print("ERROR")