import random


def make_password_list():
    passwords = []
    while True:
        # adding .strip() to it to get rid of any newline characters that may be there
        password = input("Please enter a password to add: ").strip()
        passwords.append(password)

        # made language more clear,
        # stripped it for reasons above,
        # made it lowercase for case-insensitivity
        choice = input("finished adding passwords? yes/no: ").strip().lower()
        if choice == 'yes':
            break
    return passwords


passwords = make_password_list()
Random_choice = random.choice(passwords)
print('_' * len(Random_choice))
guess = input("What's your guess?:")


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
        for letter in Word:
            if guess not in Random_choice:
                print(letter)
                return letter



hang_man()