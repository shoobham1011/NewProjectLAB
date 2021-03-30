'''
Price of a house is $1M. If buyer has good credit,
they need to put down 10% otherwise they need to put down 20%
print down the payment.
'''

buyer_credit = True

price = 1000000

if buyer_credit:
    down_pay = 0.1 * price
else:
    down_pay = 0.2 * price

print(f'Down payment is ${down_pay}')