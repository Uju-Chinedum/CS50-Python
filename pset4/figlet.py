import sys
from pyfiglet import Figlet, FontNotFound
import random

figlet = Figlet()

try:
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        if len(sys.argv) == 1:
            font = random.choice(figlet.getFonts())
        elif len(sys.argv) == 3:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                font = sys.argv[2]
            else:
                sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

    figlet.setFont(font = font)
    user = input()
    print(figlet.renderText(user))

except FontNotFound:
    sys.exit("Invalid Usage")