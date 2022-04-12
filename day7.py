import random
import urllib.request
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
#Description of the wordle game
# Make a Wordle game.
# Description: Wordle is a single player game, in which a user is required to guess a 5-letter hidden word in 6 Attempts.
# *The user makes a first guess.(E.G: "Skate").
# * Print out a progress guide, like this. "√××√+",
# * "√" Indicates that the letter at that position was guessed correctly.
# * "+" indicates that the letter at that position is in the hidden word, but in a different position.
# * "×" indicates that the letter at that position is wrong, and isn't in the hidden word.
# *This process is repeated until the user either guesses the hidden word correctly—in which case, he Wins!—, or exhausts his 6 Attempts, losing.
# *The "hidden word" is generated randomly from a list of 5-letter words hard-coded by you.

def generate_five_letter_words():
    ### The goal of this function is to generate valid five letter words as some words are not english words, hence unacceptable. It takes no argument but it returns a list of valid 5 letter english words. Although every single word might not be represented but it does a fair job. I believe it wouldn't be a good game if "ghrui" passes as a word.###
    list_of_valid_five_letter_word = []
    word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
    response = urllib.request.urlopen(word_site)
    txt = response.read()
    WORDS = txt.splitlines()

    for word in WORDS:
        if len(word.decode("utf-8")) == 5:
            list_of_valid_five_letter_word.append(word.decode("utf-8").lower())
    return list_of_valid_five_letter_word

five_letter_words = ["BAKED", "SORRY", "FUNNY", "PRINT", "ALTAR"]
ruler = "_"
GAME_POSITION = "Progress: _ _ _ _ _"
SECRET_WORD = random.choice(five_letter_words)



def greeting():
    ###This function initates the game and welcomes you.
    WELCOME_MESSAGE = f"The rules of the game is very simple!\n INSTRUCTIONS \n {ruler * 15} \n 1. You have 6 attempts to guess a secret word : For each of your attempt, you'll have a guide that'll show you how close you are to the word you are trying to guess.\n 2. The guides are:\n - '√' Indicates that the letter at that position was guessed correctly.\n - '+' indicates that the letter at that position is in the hidden word, but in a different position. \n - '×' indicates that the letter at that position is wrong, and isn't in the hidden word. \n \n 3. The words to be guessed is just five letters. So try your best. \n \n BEST OF LUCK!"
    print("Welcome to Ajibola Special Wordle's challenge!")
    print(WELCOME_MESSAGE)
    
def beginning_input(position):
    ###This function initializes the game by telling you to type start and proceeding further"
    user_input = input("Kindly type start to begin...\n")
    if user_input.lower() == "start":
        print(position)
        print("Wait a little, game is loading .....")
    else:
        exit()

def main(secret_word):
    ### This function implements the essentials of the game, the logic is checked here and all that fancy stuff. it also references other functions to be used in the code###
    greeting()
    beginning_input(GAME_POSITION)
    win_state = False
    attempt = 0
    five_lettered_words = generate_five_letter_words()
    correct_letter, correct_letter_wrong_pos, wrong_letter = ("√", "+", "×")
    while not win_state and attempt < 6:
        GUESSED_WORD = input("Kindly guess a word!\n")
        current_state = GUESSED_WORD[:]
        #print(current_state) - trying to understand why current_state isn't getting replaced with what i want it to replace with 
        if GUESSED_WORD.lower() == secret_word.lower():
            attempt += 1
            print(f"You WIN! You correctly guessed the secret word after {attempt} attempts")
            win_state = True
        if len(GUESSED_WORD) != 5:
            print("You are meant to guess a five letter word, try again!")
            attempt += 1
        if GUESSED_WORD not in five_lettered_words:
            print("Please input a valid word. \n")
            attempt += 1
        else:
            for letter in GUESSED_WORD.lower():
                for secret_letter in secret_word.lower():
                    if letter == secret_letter and GUESSED_WORD.lower().find(letter) == secret_word.lower().find(secret_letter):
                        current_state = current_state.replace(letter, correct_letter)
                    elif letter == secret_letter and GUESSED_WORD.lower().find(letter) != secret_word.lower().find(secret_letter):
                        current_state = current_state.replace(letter, correct_letter_wrong_pos)
                current_state = current_state.replace(letter, wrong_letter)
            print(f"Guessed word: {GUESSED_WORD}")
            print(f"Progress status: {current_state}")


            attempt += 1
    if win_state:
        exit()
    else:
        print(f"Sadly, the number of attempt is up!")
        



    




if __name__ == '__main__':
    main(SECRET_WORD)






