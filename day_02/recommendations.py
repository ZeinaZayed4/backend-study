def main():
    difficulty = input('Difficult of Casual? ')

    if not (difficulty == 'Difficult' or difficulty == 'Casual'):
        print('Enter a valid difficulty.')
        return

    players = input('Multiplayer or Single-player? ')

    if not (players == 'Multiplayer' or players == 'Single-player'):
        print('Enter a valid number of players.')
        return

    if difficulty == 'Difficult' and players == 'Multiplayer':
        print('Poker')
    elif difficulty == 'Difficult' and players == 'Single-player':
        print('Klondike')
    elif difficulty == 'Casual' and players == 'Multiplayer':
        print('Hearts')
    else:
        print('Clock')


def recommend(game):
    print(f'You might like {game}!')


main()
