import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) in range(1, 4):
    if len(sys.argv) == 1:
        a = input("Input: ")
        f = random.choice(fonts)
        figlet.setFont(font=f)
        print("Output: ", figlet.renderText(a))

    else:
        if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        else:
            a = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print("Output: ", figlet.renderText(a))
else:
    sys.exit(1)
