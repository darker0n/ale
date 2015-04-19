#!/usr/bin/env python

from core import wcolors
from core import main

if __name__ == "__main__":
    try:
        main.main()  # main program
    except KeyboardInterrupt:
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Trying To Exit ..." + wcolors.color.ENDC)
        print(wcolors.color.YELLOW + "[*] Thank You For Using Ale =)" + wcolors.color.ENDC)