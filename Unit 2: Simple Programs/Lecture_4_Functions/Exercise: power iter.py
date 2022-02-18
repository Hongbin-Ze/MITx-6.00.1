#Write an iterative function iterPower(base, exp) that calculates the exponential  by simply using successive multiplication. 
#For example, iterPower(base, exp) should compute  by multiplying base times itself exp times. Write such a function below.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    result = base
    if exp == 0:
        return 1
    while exp > 1:
        result *= base
        exp -= 1
    return result
