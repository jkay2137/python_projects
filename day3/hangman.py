import random

words_list = ["mouse", "melon", "camel", "letters"]

r = random.randint(0, words_list.__len__() - 1)

word = words_list[r]

print(word)