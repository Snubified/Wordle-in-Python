import os

# Enables ANSI colors in Windows Command Prompt / PowerShell
os.system("")

# Color presets (Background + Text)
YELLOW = "\033[103m\033[30m"  # Bright yellow bg, black text
GOLD = "\033[43m\033[30m"  # Standard yellow bg, black text
CYAN = "\033[106m\033[30m"  # Bright cyan bg, black text
GREEN = "\033[102m\033[30m"  # Bright green bg, black text
RESET = "\033[0m"


import random
from ascii import ascii_map
from ascii import ascii_map_y
from ascii import ascii_map_g
file = open("valid-wordle-words.txt", "r")
file2 = open("wordle-answers-alphabetical.txt", "r")

words = file.read().splitlines()
answers = file2.read().splitlines()

secret_word = random.choice(answers)
print("================================")
print("             WORDLE")
print("================================")
print("Guess the 5-letter word.")
print("You have 6 attempts.")
print()
print("🟩 = Correct letter and position")
print("🟨 = Correct letter, wrong position")
print("⬜ = Letter is not in the word")
print()

attempts = 6

alphabet_output = []

while attempts > 0:

    guess = input("Enter your guess: ").lower()


    if len(guess) != 5:
        print("Your word must have exactly 5 letters!")
        continue

    if not guess.isalpha or not guess.isascii():
        print("Please enter ASCII letters only!")
        continue

    if guess not in words:
        print("Not in word list!")
        continue

    result = ["⬜"] * 5
    remaining = list(secret_word)
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # First check correct letters in correct positions
    for row in range(7):
            for i in range(5):
                if guess[i] in ascii_map:
                    result = ascii_map[guess[i]].splitlines()[row]
                    if guess[i] == secret_word[i]:
                        result = ascii_map_g[guess[i]].splitlines()[row]
                    elif guess[i] in secret_word and guess[i] != secret_word[i]:
                        result = ascii_map_y[guess[i]].splitlines()[row]
                    alphabet = [letter for letter in alphabet if letter in guess]
                print(result, end="")
            print()  # moves to the next line after finishing a row
    alphabet_output += alphabet
    alphabet_output_sorted = sorted(set(alphabet_output))
    print(f"Used: {', '.join(alphabet_output_sorted)}")
    attempts -= 1

    if guess == secret_word:
        print()
        print("CONGRATULATIONS! YOU WON!")
        print("You guessed the word:", secret_word)
        break

    print("Attempts remaining:", attempts)
    print()

if attempts == 0 and guess != secret_word:
    print("GAME OVER")
    print("The correct word was:", secret_word)

print()
