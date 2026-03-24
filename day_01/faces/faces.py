def main():
    string = input()
    print(convert(string))


def convert(to):
    to = to.replace(':)', '🙂')
    to = to.replace(':(', '🙁')
    return to


main()
