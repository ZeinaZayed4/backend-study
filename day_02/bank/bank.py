greeting = input('Greeting: ').lower().strip()

if greeting.startswith('hello') or greeting.startswith('hello,'):
    print('$0')
elif greeting.startswith('h'):
    print('$20')
else:
    print('$100')
