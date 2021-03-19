import random
import os

passwords = []

while True:
    phrases = input("Please press enter to add phrases: ")
    passwords.append(phrases)
    choice = input("would you like to start the game? yes/no: ")
    #State machine
    if choice != 'no':
        break
Random_choice = random.choice(passwords)
print('_' * len(Random_choice))
guess = input("What's your guess?:")

os.system('cls')
#Checking if there is a letter in phrase
def letter_placeing():
    for Random_choice in guess:
            if guess in Random_choice:
                print(guess)

if guess in Random_choice:
    letter_placeing()

if guess == Random_choice:
    print("yes")
else:
    def hang_man():
        Word = 'hangman'
        for guess in Word:
            if guess not in Random_choice:
                print(Word)
hang_man()