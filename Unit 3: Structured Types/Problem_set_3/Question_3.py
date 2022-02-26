#Note that this function should return the letters in alphabetical order, as in the example above.

#For this function, you may assume that all the letters in lettersGuessed are lowercase.

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    stringA = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            stringA += i
    return stringA
