#!/usr/bin/python3

# Import necesary modules
import os
import random
from hangman_art import logo
from hangman_art import stages


def hangman():
    # Make word list make number of lives
    wordlist = ["one", "two", "three", "four", "five"]
    lives = (len(stages))-1

# Print starting logo
    print(logo)

# Pick a random word from the list
    word = random.choice(wordlist)
    len_word = len(word)

# Make guess list
    guess_list = ["_"]*len_word

# Convert lists to strings
    guess_list_string = ''.join(guess_list)
    word_string = ''.join(word)

# print lives and display current score/results
    print(f"You have {lives} lives remaining")
    print(f"{guess_list}\n")

# continue while lives are greater than 0 or word has been guessed
    while lives > 0 and (word_string != guess_list_string):

        # input guess
        guess = input("Pick a letter: ").lower()

# check to see if guess is in word
        if guess in word:
            for letter in word:
                if guess == letter:
                    index = word.index(guess)
                    guess_list[index] = guess
        else:
            lives -= 1

# Clear screen and redraw
        os.system('clear')
        print(logo)
        print(stages[lives])
        print(f"You have {lives} lives remaining")
        print(guess_list)

        guess_list_string = ''.join(guess_list)
        word_string = ''.join(word)

# print final messages
    if word_string == guess_list_string:
        print(f"\nYou Win! the word is '{word_string}'\n")
    else:
        print(f"\nYou Lose! the word is '{word_string}'\n ")

# ask if yoou want to play again
    play = input("Do you want to play HangMan? 'y' or 'n'").lower()

    if play == 'y':
        hangman()


# start program/function
hangman()
