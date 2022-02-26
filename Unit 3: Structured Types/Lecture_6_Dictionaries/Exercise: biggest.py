#This time, write a procedure, called biggest, 
#which returns the key corresponding to the entry with the largest number of values associated with it. 
#If there is more than one such entry, return any one of the matching keys.

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = 0
    result = None
    if aDict == {}:
        return result
    else:
        for i in aDict.keys():
            if len(aDict[i]) >= count:
                count = len(aDict[i])
                result = i
    return result
