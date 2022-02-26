#For this problem, you are free to use spacing in any way you wish 
#our grader will only check that the letters and underscores are in the proper order; 
#it will not look at spacing. We do encourage you to think about usability when designing.

#For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ''
    for i in secretWord:
        if i not in lettersGuessed:
            string += "_ "
        else:
            string += i
    return string
