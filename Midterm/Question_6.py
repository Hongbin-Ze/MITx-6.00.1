def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    result = 0
    
    def open(t):
        newlist = []
        for i in t:
            if type(i) == int:
                newlist.append(i)
            else:
                newlist += open(i) 
        return newlist
    
    openlist = open(t)
    for i in openlist:
        if result < i:
            result = i
            
    return result
