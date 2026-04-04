import re

locations = {"+1": "United States and Canada", "+20": "Egypt", "+505": "Nicaragua"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    if matches := re.search(pattern, number):
        country_code = matches.group("country_code")
        if country_code in locations.keys():
            print(locations[country_code])
        else:
            print("Sorry. Your country is not supported.")
    else:
        print("Invalid.")


main()
