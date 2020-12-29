#Python Hangman Game
# 12/28/2020
# it's about to be the 29th bc it's really late

#libraries
import random
import time

# http://www.mit.edu/~ecprice/wordlist.10000

def random_word():
    with open("wordlist.10000.txt","r") as f:
        text_file = f.read()
        words = list(text_file.split())
        word = random.choice(words)
    return word


def guesses():
    player_guess = int(input("how many guesses do you want to have (5-15)?\n"))
    if player_guess > 16 or player_guess <= 4:
        print("that's not between 5-15")
        return guesses()
    else:
        return player_guess


def player_guess():
    word = random_word()
    print(word)
    disguised_word = len(word) * '_'

    word = list(word) # this is the new part
    disguised_word = list(disguised_word)

    guess = 0
    num_of_guesses = guesses()
    already_guessed = []

    while guess < num_of_guesses:
        player_guessing = input("guess your first letter")
        player_guessing = player_guessing.lower()

        if player_guessing in word and player_guessing not in already_guessed:
            already_guessed.append(player_guessing)
            index_pos = [i for i, x in enumerate(word) if x == player_guessing]

            for i in index_pos:
                disguised_word[i] = player_guessing
            print(''.join(disguised_word))

            print("You have", num_of_guesses, "tries left.")


        elif player_guessing in already_guessed:
            print("you already entered that letter, try a new one")

        else:
            guess = guess + 1
            print("oh no, letter not in word!")
            print("You have", (num_of_guesses-guess), "tries left")
            print(''.join(disguised_word))

print(player_guess())

