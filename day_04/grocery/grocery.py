grocery = {}

while True:
    try:
        item = input().upper()

        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print()
        break

keys = sorted(grocery.keys())

for value in keys:
    print(f'{grocery[value]} {value}')
