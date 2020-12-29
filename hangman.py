# Python Hangman Game

# print("Hi how are you! This is a python script of classical game Hangman"
#       "\nThe word to guess is represented by a row of dashes"
#       "\nIf the player guess a letter which exists in the word, the script writes it in all its correct positions"
#       "\nThe player has 10 turns to guess the word")
#


# how many guesses the player has

# def guesses():
#     player_guess = int(input("how many guesses do you want to have (5-15)?\n"))
#     if player_guess > 16 or player_guess <= 4:
#     if player_guess > 16 or player_guess <= 4:
#         print("that's not between 1-20")
#         return guesses()
#     else:
#         return player_guess
#
#
# print("the number of guesses you have to play this game is ", guesses())


# choose a random word

import random
random_words = ("watar","airpad","bathraom","spaan")
word = random.choice(random_words)


def player_guess():
    word = random.choice(random_words)
    print(word)
    word_length = len(word)
    disguised_word = word_length * '_'
    word = list(word) # this is the new part
    disguised_word = list(disguised_word)
    print(disguised_word)
    guess = 5
    already_guessed = []
    while guess < 10:
        player_guessing = input("guess your first letter")
        player_guessing = player_guessing.lower()

        if player_guessing in word and player_guessing not in already_guessed:
            already_guessed.append(player_guessing)
            # print("you already entered that letter, try a new one")
            index_pos = [i for i, x in enumerate(word) if x == player_guessing]
            print(index_pos)
            print(player_guessing)
            for i in index_pos:
                disguised_word[i] = player_guessing
            print(''.join(disguised_word))
        elif player_guessing in already_guessed:
            print("you already entered that letter, try a new one")

        else:

            guess = guess + 1
            print("oh no wrong")



print(player_guess())

