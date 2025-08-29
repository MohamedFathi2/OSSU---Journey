# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(letters_guessed) == 0 : return False
    count = 0
    setOfChar = set(secret_word)
    for letter in letters_guessed:
        if letter in setOfChar:
            count += 1
    return count == len(setOfChar)

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(letters_guessed) == 0:
        toReturn = ""
        for _ in range(len(secret_word)):
            toReturn += "*"
        return toReturn
    toReturn = ""
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            toReturn += secret_word[i]
        else:
            toReturn += "*"
    return toReturn
    

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(letters_guessed) == 0:
        return string.ascii_lowercase
    letters = list(string.ascii_lowercase)
    for l in set(letters_guessed):
        letters.remove(l)
    return ''.join(letters)
    
def get_random_letter(secret_word, letters_guessed):
    random_letter = ""
    for letter in secret_word:
        if letter not in letters_guessed:
            random_letter = letter
            break
    return random_letter
    
def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    totalGuesses = 10
    letters_guessed = []
    while totalGuesses > 0:
        if has_player_won(secret_word, letters_guessed):
            print("--------------")
            print("Congratulations, you won!")
            total_score = (totalGuesses + 4 * len(set(secret_word))) + (3 * len(secret_word))
            print(f"Your total score for this game is: {total_score}")
            break
        print("--------------")
        print(f"You have {totalGuesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        curr = input("Please guess a letter: ")
        if curr == '!' and with_help:
            if totalGuesses < 4:
                print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
            else:
                totalGuesses -= 3
                randomLetter = get_random_letter(secret_word, letters_guessed)
                print(f"Letter revealed: {randomLetter}")
                letters_guessed.append(randomLetter)
                print(get_word_progress(secret_word, letters_guessed))
        elif len(curr) != 1 or curr not in string.ascii_letters:
            print("Oops! That is not a valid letter. Please input a letter from")
            print("the alphabet:", get_word_progress(secret_word, letters_guessed))
        else:
            curr = curr.lower()
            if curr not in secret_word:
                print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                letters_guessed.append(curr)
                if curr in ('a', 'e', 'i', 'o', 'u'):
                    totalGuesses -= 2
                else:
                    totalGuesses -= 1
            else:
                if curr in letters_guessed:
                    print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
                else: 
                    letters_guessed.append(curr)
                    print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
                    # print("----------")
    if totalGuesses <= 0:
        print("--------------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    secret_word = "hi"
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

