from random import *


def main():
    coin = choice(['heads', 'tails'])
    print(coin)

    cards = ['jack', 'queen', 'king']
    shuffle(cards)
    print(cards)

    guess(randint(1, 10))


def guess(n):
    while True:
        g = int(input("What's your number? "))
        if g == n:
            print('You got it!')
            break
        

main()
