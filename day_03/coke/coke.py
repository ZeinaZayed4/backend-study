amount = 50

while amount > 0:
    print(f'Amount Due: {amount}')
    coins = int(input('Insert Coin: '))

    if coins in [5, 10, 25]:
        amount -= coins

print(f'Change Owed: {-amount}')
