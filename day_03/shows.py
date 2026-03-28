SHOWS = [
    ' Avatar: the last airbender',
    'Ben 10',
    'Arthur',
    ' Spongebob Squarepants',
    'Phineas and ferb',
    'Kim possible',
    'Jimmy Neutron',
    'the Proud family'
]


def main():
    cleaned_shows = [show.strip().title() for show in SHOWS]
    print('\n'.join(cleaned_shows))


main()
