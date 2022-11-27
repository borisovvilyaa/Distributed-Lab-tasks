import random

class WordGen:
    def random_word(words):
        return random.choice (words)
    def wordGen():
        with open('word.txt', 'r') as file:
            words = file.readlines()
            words = [s.strip("\n") for s in words]
        words_mas = []
        for i in range(12):
            words_mas.append(WordGen.random_word(words))


        str_word = ' '.join(words_mas)
        return str_word
    def printGen(word):
        print(word)
    
