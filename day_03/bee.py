WORDS = {'PAIR': 4, 'HAIR': 4, 'CHAIR': 5, 'GRAPHIC': 7}


def main():
    print('Welcome to Spelling Bee!\n')
    for word, points in WORDS.items():
            print(f'{word} was worth {points} points.')
    
    print('\nYour letters are: A I P C R H G')
    guess_game(WORDS)


def guess_game(words):
    total_points = 0

    while len(words) > 0:
        print(f'{len(words)} words left!')
        guess = input('Guess a word: ')

        if guess == 'GRAPHIC':
            total_points += words[guess]
            words.clear()
            print("You've won!")
        
        if guess in words.keys():
            print(f'Good job! You scored {words[guess]} points.')
            total_points += words[guess]
            words.pop(guess)
    
    print(f'Your total points: {total_points}')
    print("That's the game!")

main()
