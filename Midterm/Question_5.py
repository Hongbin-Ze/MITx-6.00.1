def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    resultlist = []
    
    for key in aDict.keys():
        if aDict[key] == target:
            resultlist.append(key)
    
    return resultlist
