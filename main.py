# hangman game
import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_set = set(word)
    used_word = set()
    alphabet = set(string.ascii_uppercase)
    lives = 6

    while len(word_set) > 0 and lives > 0:
        print('You have ', lives, 'lives left and you have used these letters:', ' '.join(used_word))

        word_list = [letter if letter in used_word else '-' for letter in word]
        print('Current word: ', ''.join(word_list))
        user_letter = input('Guess the letter: ').upper()
        if user_letter in alphabet - used_word:
            used_word.add(user_letter)
            if user_letter in word_set:
                word_set.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_word:
            print('This letter is used, try another one.')
        else:
            print('Invalid characters. Please try again.')
    if lives > 0:
        print(f'You have guessed {word} correctly')
    else:
        print('You lost as you died and the word was ',word)


hangman()