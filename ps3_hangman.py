# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def underscored(list):
    '''
    Assume list is a list
    it returns a new list of underscores. The number of underscore is teh number of item in list
    '''
    newList = []
    for i in range(len(list)):
        newList.append('_')
    return newList


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    i=0
    guess= True
    while guess==True and i<len(secretWord):
        if secretWord[i] in lettersGuessed:
            guess = True
            i+=1
        else:
            guess = False
            break
    return guess


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    i = 0
    gameStatus = underscored(secretWord)
    while i<len(secretWord):
        if secretWord[i] in lettersGuessed:
            gameStatus[i] = secretWord[i] 
            i+=1
        else:
            i+=1
    gameStatus = ''.join(gameStatus)
    return gameStatus


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet.remove(letter)
            
    return ''.join(alphabet)   

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is" + " " + str(len(secretWord)) + " " + "letters long.")
    print("-----------")
    print("You have 8 guesses left.")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")
    lettersGuessed = []
    mistakesMade = 0
    right = 0
    while right<len(secretWord) and mistakesMade<=8:
        guess = input("Please guess a letter:")
        guess = guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:")
            print("You have" + " " + str(8- mistakesMade) + " " + "guesses left")
            getAvailableLetters(lettersGuessed)
        else:
            if guess not in secretWord:
                print("You have" + " " + str(8- mistakesMade) + " " + "guesses left")
                getGuessedWord(secretWord, lettersGuessed)
                print(getAvailableLetters(lettersGuessed))
                print("Oops! That letter is not in my word:" + " " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
                lettersGuessed.append(guess)
                mistakesMade+=1
            else:
                guess in secretWord
                lettersGuessed.append(guess)
                right=+1
                getGuessedWord(secretWord, lettersGuessed)
                if "_" not in getGuessedWord(secretWord, lettersGuessed):
                    right=len(secretWord)
                print("You have" + " " + str(8- mistakesMade) + " " + "guesses left")
                getGuessedWord(secretWord, lettersGuessed)
                print(getAvailableLetters(lettersGuessed))
                print("Good guess:" + " " + getGuessedWord(secretWord, lettersGuessed))
                print("-----------")
    if isWordGuessed(secretWord, lettersGuessed):
        return print("Congratulations, you won!")
    else:
        return print("Sorry, you ran out of guesses. The word was" + " " + secretWord)
    
        

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
