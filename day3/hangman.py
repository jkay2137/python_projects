import random

words_list = ["mouse", "melon", "camel", "letters"]

word = random.choice(words_list)

print(word)

blanks = []

for char in word:
    if char != " ":
        blanks.append("_")

print(blanks)

guess = input("Guess a letter: ").lower()

i = 0
while i < word.__len__():
    if guess == word[i]:
        blanks[i] = guess
    i += 1

print(blanks)