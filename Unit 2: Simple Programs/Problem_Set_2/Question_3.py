def compute_balance (balance, annualInterestRate, fixedMonthlyPay):
    '''
    Parameters
    ----------
    balance : int
        the outstanding balance on the credit card
    annualInterestRate : float
        annual interest rate as a decimal
    fixedMonthlyPay : float
        monthlypay

    Returns
    -------
    updatedBalance : float
    '''
    numberOfMonths = 12
    monthlyPaymentRate = annualInterestRate / 12.0
    prevBalance = balance
    for month in range(0,numberOfMonths):
        monthlyUnpaidBalance = prevBalance - fixedMonthlyPay
        updatedBalance = monthlyUnpaidBalance + (monthlyPaymentRate*monthlyUnpaidBalance)
        prevBalance = updatedBalance        
    return updatedBalance

def compute_low_and_up(balance, annualInterestRate):
    '''
    Parameters
    ----------
    balance : int
        the outstanding balance on the credit card
    annualInterestRate : float
        annual interest rate as a decimal

    Returns
    -------
    monthlyPayLow : float
    monthlyPayUp : float
    '''
    monthlyPaymentRate = annualInterestRate/12.0
    monthlyPayLow = balance / 12.0
    monthlyPayUp = balance * (1 + monthlyPaymentRate) ** 12 / 12.0
    return monthlyPayLow, monthlyPayUp


def compute_minMonthPay(balance, annualInterestRate):
    '''
    Parameters
    ----------
    balance : int
        the outstanding balance on the credit card
    annualInterestRate : float
        annual interest rate as a decimal

    Returns
    -------
    minMonthPay : float
    '''
    monthlyPayLow,monthlyPayUp = compute_low_and_up(balance, annualInterestRate)
    while True:
        minMonthPay = (monthlyPayLow + monthlyPayUp) / 2.0
        updatedBalance = compute_balance(balance, annualInterestRate, minMonthPay)
        if abs(monthlyPayUp - monthlyPayLow) <= 0.01:
            return minMonthPay
        if updatedBalance > 0:
            monthlyPayLow = minMonthPay
        elif updatedBalance < 0:
            monthlyPayUp = minMonthPay
            
minMonthPay = compute_minMonthPay(balance, annualInterestRate)
print(" Lowest Payment: %0.2f" %minMonthPay)
