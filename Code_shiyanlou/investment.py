#!/usr/bin/env/python 3
amount = float(input('Enter amount: '))
inrate = float(input('Enter Interest rate: '))
peroid = int(input('Enter peroid: '))
value = 0
year = 1
while year <= peroid:
        value = amount + (inrate * amount)
        print("Year {} Rs.{:.2f}".format(year, value))
        amount = value
        year += 1
