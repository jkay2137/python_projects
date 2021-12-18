import random

words_list = ["mouse", "melon", "camel", "letters"]

word = random.choice(words_list)

n = word.__len__()

print(word)

blanks = []

for char in word:
    if char != " ":
        blanks.append("_")
    else:
        blanks.append(" ")

end = False

while not end:
    guess = input("Guess a letter: ").lower()
    i = 0
    while i < n:
        if guess == word[i]:
            blanks[i] = guess     
        i += 1

    j = 0
    for char in blanks:
        if char == "_":
            j += 1
    if j == 0:
        end = True

    print(blanks)

print("You win")