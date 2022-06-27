# NATO PHONETIC ALPHABET 
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ").upper()

phonetic_list = [dictionary[letter] for letter in word]

print(phonetic_list)