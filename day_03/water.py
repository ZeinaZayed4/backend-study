from soil import sample


def main():
    days = 0

    while True:
        moisture = sample()
        days += 1
        print(f'Day {days}: Moisture is {moisture}%')

        if moisture < 20:
            print('Time to water!')
            break


main()
