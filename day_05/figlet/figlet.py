from sys import argv, exit
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
elif len(argv) == 3:
    if argv[1] not in ["-f", "--font"]:
        exit("Invalid usage")
    if argv[2] not in Figlet().getFonts():
        exit("Invalid usage")

    figlet.setFont(font=argv[2])
else:
    exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
