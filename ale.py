#!/usr/bin/env python
import webbrowser
import readline
import os
from core import wcolors

commands = ["google", "maps", "youtube", "yahoo", "gmail", "wiki", "notes", "amazon"]


def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


def parse_request(arr):
    request = ""
    for x in arr:
        request += x + " "
    return request


def main():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    while True:
        com = raw_input(wcolors.color.YELLOW + "ale> " + wcolors.color.ENDC).split()
        if com[0] == "google":
            print(wcolors.color.GREEN + "Searching in Google => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.google.com/search?q=' + parse_request(com[1:]))
        elif com[0] == "maps":
            print(wcolors.color.GREEN + "Searching in Google Maps => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.google.com/maps/?q=' + parse_request(com[1:]))
        elif com[0] == "youtube":
            print(wcolors.color.GREEN + "Searching in Youtube => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.youtube.com/results?search_query=' + parse_request(com[1:]))
        elif com[0] == "yahoo":
            print(wcolors.color.GREEN + "Searching in Yahoo => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://search.yahoo.com/search?p=' + parse_request(com[1:]))
        elif com[0] == "gmail":
            print(wcolors.color.GREEN + "Opening Gmail..." + wcolors.color.ENDC)
            webbrowser.open('https://mail.google.com/mail')
        elif com[0] == "wiki":
            print(wcolors.color.GREEN + "Searching in Wikipedia => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://wikipedia.org/wiki/Special:Search/' + parse_request(com[1:]))
        elif com[0] == "notes":
            print(wcolors.color.GREEN + "Opening Notes..." + wcolors.color.ENDC)
            os.system("open -a /Applications/Notes.app")
        elif com[0] == "amazon":
            print(wcolors.color.GREEN + "Searching in Amazon => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('http://www.amazon.com/s?url=search-alias=aps&field-keywords=' + parse_request(com[1:]))
        else:
            print wcolors.color.RED + "Invalid command => " + parse_request(com[0:]) + "." + wcolors.color.ENDC + wcolors.color.GREEN + " Trying search in Google." + wcolors.color.ENDC
            webbrowser.open('https://www.google.com/search?q=' + parse_request(com[0:]))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Trying To Exit ..." + wcolors.color.ENDC)
        print(wcolors.color.YELLOW + "[*] Thank You For Using Ale =)" + wcolors.color.ENDC)