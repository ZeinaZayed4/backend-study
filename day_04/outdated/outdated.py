months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input('Date: ')

        if date[0].isalpha(): 
            month_name, day, year = date.split()
            if ',' not in day:
                continue
            day = int(day.replace(',', ''))
            year = int(year)

            if month_name not in months:
                continue
            month = months.index(month_name) + 1
        else:
            month, day, year = date.split('/')
            month, day, year = int(month), int(day), int(year)

        if not (1 <= month <= 12) or not (1 <= day <= 31):
            continue

        break
    except ValueError:
        pass

print(f'{year:04}-{month:02}-{day:02}')
