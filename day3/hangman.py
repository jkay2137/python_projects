# HANGMAN GAME
import random

# Hangman ASCII
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Variables 
words_list = ["mouse", "melon", "camel", "letters"]
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
        print(lives)
    
    print(' '.join(blanks))   
    print(stages[lives])

    # When should it end
    if lives == 0:
        print("You lose")
        break

    if "_" not in blanks:
        print("You win")
        break
