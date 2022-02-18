minMonthPay = 0
unpaidBalance = 1
monthlyInterestRate = annualInterestRate/12.0

while unpaidBalance > 0:
    minMonthPay += 10
    unpaidBalance = balance
    
    for month in range(1, 13):
        unpaidBalance = (unpaidBalance - minMonthPay)*(1+monthlyInterestRate)

print(" Lowest Payment: %i" %minMonthPay)
