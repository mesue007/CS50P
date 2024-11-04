import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

if sys.argv[1] != ("-f" or "--font"):
    sys.exit("Please input -f or --font as first argument")

elif len(sys.argv) == 3:
    f = sys.argv[2]

    figlet.setFont(font=f)

    s = input("Input: ")

    print(figlet.renderText(s))

elif len(sys.argv) == 1:
    f = choice(figlet.getFonts())

    figlet.setFont(font=f)

    s = input("Input: ")

    print(figlet.renderText(s))
