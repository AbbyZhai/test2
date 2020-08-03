def LowestPaymentInOneYear(balance, annualInterestRate,LowestPayment=10):
    #LowestPayment = 10
    if balance <= 0:
        print(LowestPayment,round(balance,2))
        return 'Lowest Payment: {}'.format(LowestPayment)

    else:
        unpayBlance = balance - LowestPayment
        balance = unpayBlance * (1 + annualInterestRate/12.0)
        #balance = (balance - LowestPayment) * (1 + annualInterestRate/12.0)
        LowestPayment = LowestPayment + 10
        return LowestPaymentInOneYear(balance, annualInterestRate,LowestPayment)

print(LowestPaymentInOneYear(4773,0.2))
