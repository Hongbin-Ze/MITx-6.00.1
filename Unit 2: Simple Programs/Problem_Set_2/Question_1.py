def balanceYear(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Parameters
    ----------
    balance : int
        the outstanding balance on the credit card
    annualInterestRate : float
        annual interest rate as a decimal
    monthlyPaymentRate : float
        minimum monthly payment rate as a decimal
        
    Returns
    -------
    remainingBalance    
        Remaining balance
    '''
    for i in range(0,12):
       minMonthlyPay = round(balance * monthlyPaymentRate, 2)
       unpaidBalance = round(balance - minMonthlyPay, 2)
       Interest = round(annualInterestRate / 12.0 *unpaidBalance, 2)
       remainingBalance = round(Interest + unpaidBalance, 2)
       balance = remainingBalance
    
    return remainingBalance

remain_balance = balanceYear(balance, annualInterestRate, monthlyPaymentRate)
print("Remaining balance:%.2f" %remain_balance)
