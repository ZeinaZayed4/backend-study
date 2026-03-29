'''
- Continue:
    This statement is used to skip over the execution part of the loop on a certain condition.
    After that, it transfers the control to the beginning of the loop.
    Basically, it skips its following statements and continues with the next iteration of the loop.
- Pass:
    As the name suggests pass statement simply does nothing.
    We use pass statement to write empty loops.
    Pass is also used for empty control statements, functions and classes.
'''

text = 'cat'

for c in text:
    if c == 'a':
        print('Pass')
        pass
    print(c)

'''PASS OUTPUT
c
Passed
a
t
'''

print()
for c in text:
    if c == 'a':
        print('Continue')
        continue
    print(c)

'''CONTINUE OUTPUT
c
Continue
t
'''
