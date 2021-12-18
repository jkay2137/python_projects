# HANGMAN GAME
import random
import hangman_art.py
import hangman_words.py

# Printing logo in ASCII
print(hangman_art.logo)

# Variables 
stages = hangman_art.stages
words_list = hangman_words.word_list
word = random.choice(words_list)
n = word.__len__()
lives = 6

# Create blanks 
blanks = []
for char in word:
    if char != " ":
        blanks.append("_")
    else:
        blanks.append(" ")

# Guessing loop
while True:
    guess = input("Guess a letter: ").lower()
    i = 0
    while i < n:
        if guess == word[i]:
            blanks[i] = guess      
        i += 1

    if word.find(guess) == -1:
        lives -= 1
    
    print(' '.join(blanks))   
    print(stages[lives])

    # When should it end
    if lives == 0:
        print("You lose")
        break

    if "_" not in blanks:
        print("You win")
        break
