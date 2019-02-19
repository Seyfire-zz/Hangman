# Hangman game
# -----------------------------------


import random
import string

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


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    display = ''
    for c in secretWord:
        if c not in lettersGuessed:
            display = display + '_ '
        else:
            display = display + c
    return display


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = []
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available.append(letter)
    return ''.join(available)


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
    '''
    def is_guess_correct(guess, secretWord):
        '''
        guess: the letter the user has just guessed
        secretWord: the word (string) the user is trying to guess
        returns: Bool. True if guess is in secretWord. False otherwise.
        '''
        if guess in secretWord:
            return True
        else:
            return False


    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.\n-----------')
    tries_left = 8
    lettersGuessed = []

    # Main game loop
    while tries_left > 0 and (not isWordGuessed(secretWord, lettersGuessed)):
        print('You have ' + str(tries_left) + ' guesses left.')
        print('Available letters : ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        if guess not in string.ascii_lowercase:
            print('Please only guess letters a - z, silly.\n-----------')
            continue
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed) + '\n-----------')
            continue
        lettersGuessed.append(guess)
        if is_guess_correct(guess, secretWord):
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed) + '\n-----------')
            continue
        elif not is_guess_correct(guess, secretWord):
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed) + '\n-----------')
            tries_left -= 1
            continue

    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
