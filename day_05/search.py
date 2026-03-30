from museum.artworks import get_artworks
from museum.artists import get_artists


def main():
    artwork = input('Artwork: ')
    artworks = get_artworks(artwork, 3)
    for art in artworks:
        print(f'* {art}')

    artist = input('Artist: ')
    artists = get_artists(artist, 3)
    for art in artists:
        print(f'* {art}')


main()
