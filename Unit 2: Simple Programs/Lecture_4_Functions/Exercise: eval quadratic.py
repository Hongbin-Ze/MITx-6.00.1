#Write a Python function,that returns the value of the quadratic a*x*x + b*x + c

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    eQ = a*x*x+b*x+c
    return eQ
