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
    guessNumber = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print("I am thinking of a word that is %i letters long.\n" %len(secretWord))
    
    while guessNumber > 0:
        
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("-------------")
            print("Congratulations, you won!\n")
            break
        else:
            print("-------------")
            print("You have %i guesses left." %guessNumber)
            availableLetter = getAvailableLetters(lettersGuessed)
            print("Available letters: %s " %availableLetter)
            guess = str(input("Please guess a letter:")).lower()
            if guess in secretWord and guess not in  lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess: %s' %getGuessedWord(secretWord, lettersGuessed))
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter: %s" %getGuessedWord(secretWord, lettersGuessed))
            elif guess not in secretWord:
                print("Oops! That letter is not in my word: %s" %getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess)
                guessNumber -= 1
            
            if guessNumber == 0:
                print("-------------")
                print('Sorry, you ran out of guesses. The word was %s' %secretWord)
                break
