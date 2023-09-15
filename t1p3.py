#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created Sept 13th 2023
# This program is a random number guessing game.

import random

# logic for the game
def num_guesser(guess):
    correct_num = random.randint(1, 100)
    if guess == correct_num:
        print("\nCongrats! You got it right!")
    else:
        print("\nSorry, your guess is", abs(guess - correct_num), "numbers off!\n")
        print(correct_num, "was the correct number.")

# main, introduces the user and prompts them to play the game.
def main():

    print("\nWelcome to Number Guesser!\n")

    guess_str = input("Guess a Number between 1-100: ")
    try:
        guess = int(guess_str)
        num_guesser(guess)
    except:
        print("\nError, Please run again and enter a number.")

    print("\nDone.")

if __name__ == "__main__":
    main()
