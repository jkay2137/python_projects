# BlackJack Game 
import art
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack", "As"]
player_cards = []
croupier_cards = []
player_score = 0
croupier_score = 0


def random_card(choice):
    global player_score
    global croupier_score

    temp_card = random.choice(cards)
    
    if choice == "player":
        player_cards.append(temp_card)
        player_score += calculate_score(choice, temp_card)
    elif choice == "croupier":
        croupier_cards.append(temp_card)
        croupier_score += calculate_score(choice, temp_card)

def calculate_score(choice, temp_card):
    if temp_card in [2, 3, 4, 5, 6, 7, 8, 9,10]:
        return temp_card
    elif temp_card in ["Jack", "Queen", "King"]:
        return 10
    elif temp_card == "As":
        if choice == "croupier":
            if croupier_cards.__len__() <= 2:
                return 11
            else:
                return 1
        elif choice == "player":
            if player_cards.__len__() <= 2:
                return 11
            else:
                return 1

def compare_scores():
    if player_score > 21 and croupier_score > 21:
        return "Croupier win!"
    elif player_score > 21:
        return "Croupier win!"
    elif croupier_score > 21:
        return "You win!"
    elif croupier_score < player_score:
        return "You win!"
    else:
        return "Croupier win!"
        

while True:
    choice = input("Dou you want to play a game of BlackJack? [y/n]: ")
    con = True 
    player_cards = []
    croupier_cards = []
    player_score = 0
    croupier_score = 0

    if choice == "n":
        break
    elif choice == "y":
        print(art.logo)

        for i in range(2):
            random_card("player")
        random_card("croupier")

        while con:
            print("Your cards: " + str(player_cards))
            print("Computer cards: " + str(croupier_cards))
            print(player_score)
            print(croupier_score)
            choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if choice == 'n':
                con = False
            elif choice == 'y':
                random_card("player")

                if player_score > 21:
                    con = False

        while croupier_score < 17 and croupier_score < player_score:
            random_card("croupier")
        print(player_score)
        print(croupier_score)
        print("Your final cards: " + str(player_cards))
        print("Computer's final cards: " + str(croupier_cards))
        print(compare_scores())
