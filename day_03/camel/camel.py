camel = input('camelCase: ')

snake = ''
for c in camel:
    if c.isupper():
        c = '_' + c.lower()
    snake += c

print(f'snake_case: {snake}')
