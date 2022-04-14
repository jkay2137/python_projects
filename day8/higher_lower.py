# Higher Lower Game
import art
import game_data
import random

con = True
data = game_data.data
r_temp = random.randint(0, data.__len__() - 1)
first_obj = data[r_temp]
second_obj = ""
counter = 0

def rand_num(first_obj):
    r = random.randint(0, data.__len__() - 1)
    while first_obj == data[r]:
        r = random.randint(0, data.__len__() - 1)
    return r    

def compare(choice):
    global first_obj
    global second_obj
    if choice == "A":
        return first_obj["follower_count"] > second_obj["follower_count"]
    elif choice == "B":
        return first_obj["follower_count"] < second_obj["follower_count"]

while con:
    second_obj = data[rand_num(first_obj)]    
    print(art.logo)
    print(f"Compare A: {first_obj['name']}, {first_obj['description']}, from {first_obj['country']}. {first_obj['follower_count']}")
    print(art.vs)
    print(f"Against B: {second_obj['name']}, {second_obj['description']}, from {second_obj['country']}. {second_obj['follower_count']}")
    choice = input("Who has more followers? [A/B]: ").upper()

    print(compare(choice))



    break
