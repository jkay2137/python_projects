# HANGMAN GAME
import random
import hangman_art
import hangman_words

# Printing logo in ASCII
print(hangman_art.logo)

# Variables 
stages = hangman_art.stages
words_list = hangman_words.word_list
word = random.choice(words_list)
n = word.__len__()
lives = 6
used_letters = ""

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
    
    if used_letters.find(guess) == -1:
        used_letters += guess + " "
    else:
        print(f"You've already guessed {guess}")

    i = 0
    while i < n:
        if guess == word[i]:
            blanks[i] = guess       
        i += 1

    print(f"Used letters: {used_letters}")    
    print(' '.join(blanks))   
    
    if word.find(guess) == -1:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(stages[lives])

    # When should it end
    if lives == 0:
        print("You lose")
        print(f"The word was {word}")
        break

    if "_" not in blanks:
        print("You win")
        print(f"The word was {word}")
        break
