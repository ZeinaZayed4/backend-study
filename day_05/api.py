import requests


def main():
    try:
        print('Search the Art Institute of Chicago!')
        artist = input('Artist: ')

        response = requests.get(
            'https://api.artic.edu/api/v1/artworks/search',
            {'q': artist}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return
    
    content = response.json()['data']
    for artwork in content:
        print(f"* {artwork['title']}")


main()
