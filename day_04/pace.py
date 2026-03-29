def main():
    pace = get_pace(26.0, 0)
    print(f'You need to run each mile in {round(pace, 2)} minutes.')


def get_pace(miles, minutes):
    if minutes <= 0:
        raise ValueError('Minutes must be greater than 0.')

    return minutes / miles


main()
