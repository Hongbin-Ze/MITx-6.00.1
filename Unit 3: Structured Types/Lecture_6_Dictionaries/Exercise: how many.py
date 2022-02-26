#We want to write some simple procedures that work on dictionaries to return information.

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sum = 0
    for animal in aDict.values():
        sum += len(animal)
        
    return sum
