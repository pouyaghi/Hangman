import random
from hangman_words import word_list 

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guesses = False
    guessed_letters = []
    guessed_words = []
    tries = 6