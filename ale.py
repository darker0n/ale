#!/usr/bin/env python
import webbrowser
import readline
from core import wcolors

commands = ["google", "maps"]


def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


def main():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    while True:
        com = raw_input(wcolors.color.YELLOW + "ale> " + wcolors.color.ENDC).split()
        if com[0] == "google":
            print(wcolors.color.GREEN + "Searching in Google => " + wcolors.color.ENDC + wcolors.color.RED + com[1] + wcolors.color.ENDC)
            webbrowser.open('https://www.google.com/search?q=' + com[1])
        elif com[0] == "maps":
            print(wcolors.color.GREEN + "Searching in Google Maps => " + wcolors.color.ENDC + wcolors.color.RED + com[1] + wcolors.color.ENDC)
            webbrowser.open('https://www.google.com/maps/?q=' + com[1])
        else:
            print wcolors.color.RED + "Invalid command => " + com[0] + "." + wcolors.color.ENDC + wcolors.color.GREEN + " Trying search in Google." + wcolors.color.ENDC
            webbrowser.open('https://www.google.com/search?q=' + com[0])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Trying To Exit ..." + wcolors.color.ENDC)
        print(wcolors.color.YELLOW + "[*] Thank You For Using Infinity =)" + wcolors.color.ENDC)