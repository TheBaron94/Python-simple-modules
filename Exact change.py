# lab 3.13
# Adam Schmidt
# A program to figure out change.

amount = int(input())
dollar = 0
quart = 0
dime = 0
nick = 0
pen = 0

if amount <= 0:
    print('No change')
else:
    while amount >= 100:
        dollar = dollar + 1
        amount = amount - 100
    while amount >= 25:
        quart = quart + 1
        amount = amount - 25
    while amount >= 10:
        dime = dime + 1
        amount = amount - 10
    while amount >= 5:
        nick = nick + 1
        amount = amount - 5
    while amount >= 1:
        pen = pen + 1
        amount = amount - 1
    if dollar == 1:
        print(dollar, 'Dollar')
    elif dollar > 1:
        print(dollar, 'Dollars')
    if quart == 1:
        print(quart, 'Quarter')
    elif quart > 1:
        print(quart, 'Quarters')
    if dime == 1:
        print(dime, 'Dime')
    elif dime > 1:
        print(dime, 'Dimes')
    if nick == 1:
        print(nick, 'Nickel')
    elif nick > 1:
        print(nick, 'Nickels')
    if pen == 1:
        print(pen, 'Penny')
    elif pen > 1:
        print(pen, 'Pennies')
