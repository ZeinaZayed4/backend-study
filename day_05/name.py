from sys import argv, exit

if len(argv) < 2:
    exit('Too few arguments.')
# elif len(argv) > 2:
#     exit('Too many arguments.')

for arg in argv[1:]:
    print('Hello, my name is', arg)
