import inflect

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

text = "Adieu, adieu, to "
p = inflect.engine()
if len(names) == 1:
    print(f"{text}{names[0]}")
elif len(names) == 2:
    text += p.join(tuple(names), sep=" and")
    print(text)
else:
    text += p.join(tuple(names), sep=",")
    print(text)
