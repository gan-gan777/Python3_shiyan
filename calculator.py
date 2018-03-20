#!/usr/bin/env python3
# 2018-03-20
# Personal Tax Calculator

import sys

# Tax Threshold
proint = int(3500)

# Exception Handling
try:
    str = sys.argv[1]
except:
    print("Parameter Error")

TI = 'Taxable Income'
TP = 'Tax Payable'

TI = int(str) - proint
if TI <= 0:
    print(format(0,".2f"))
elif TI <= 1500 and TI > 0:
    tax = format((TI * 0.03 - 0),".2f")
    print(tax)
elif TI > 1500 and TI <= 4500:
    tax = format((TI * 0.1 - 105),".2f")
    print(tax)
elif TI > 4500 and TI <= 9000:
    tax = format((TI * 0.2 - 555),".2f")
    print(tax)
elif TI > 9000 and TI <= 35000:
    tax = format((TI * 0.25 - 1005),".2f")
    print(tax)
elif TI > 35000 and TI <= 55000:
    tax = format((TI * 0.30 - 2755),".2f")
    print(tax)
elif TI > 55000 and TI <=80000:
    tax = format ((TI * 0.35 - 5505),".2f")
    print(tax)
elif TI > 80000:
    tax = format((TI * 0.45 - 13505),".2f")
    print(tax)
