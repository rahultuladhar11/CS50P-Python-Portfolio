from pyfiglet import Figlet
figlet = Figlet()
import sys
import random

arg_len = len(sys.argv)
fontlist = figlet.getFonts()

if arg_len not in [1, 3]:
    sys.exit("Error")

if arg_len == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Error")
    if sys.argv[2] not in fontlist:
        sys.exit("Error")
    figlet.setFont(font = sys.argv[2])

elif arg_len == 1:
    random_font = random.choice(fontlist)
    figlet.setFont(font = random_font)

str = input("Input: ")
print(figlet.renderText(str))
