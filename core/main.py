#!/usr/bin/env python

import webbrowser
import readline
import os

from core import wcolors
from core import parser
from core import formules

search_engines = ["google", "maps", "youtube", "yahoo", "wiki", "notes", "amazon", "weather",
                  "facebook", "wolfram", "rotten", "translate"]

commands = ["remove", "rm", "exec"] + os.listdir("/Applications") + search_engines


def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


def start():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    print (wcolors.color.GREEN + "Welcome to ale, smart shell for more productive work." + wcolors.color.ENDC)


def main():
    while True:
        com = raw_input(wcolors.color.YELLOW + "ale> " + wcolors.color.ENDC).split()
        if len(com) == 0:
            main()

        # Opening applications
        if parser.parse_request(com[0:]).strip() in commands:
            print(wcolors.color.GREEN + "Opening => " + parser.parse_request(com[0:]).strip() + wcolors.color.ENDC)
            os.system("open -a /Applications/" + parser.word_space(parser.parse_request(com[0:]).strip()))

        # Searching command in Formules
        if com[0] + ".py" in formules.check_formules():
            os.system("python " + os.getcwd() + "/core/Formula/" + com[0] + ".py")

        elif com[0] == "google":
            print(
            wcolors.color.GREEN + "Searching in Google => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.google.com/search?q=' + parser.parse_request(com[1:]))
        elif com[0] == "maps":
            print(
            wcolors.color.GREEN + "Searching in Google Maps => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.google.com/maps/?q=' + parser.parse_request(com[1:]))
        elif com[0] == "youtube":
            print(
            wcolors.color.GREEN + "Searching in Youtube => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.youtube.com/results?search_query=' + parser.parse_request(com[1:]))
        elif com[0] == "yahoo":
            print(
            wcolors.color.GREEN + "Searching in Yahoo => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://search.yahoo.com/search?p=' + parser.parse_request(com[1:]))
        elif com[0] == "wiki":
            print(
            wcolors.color.GREEN + "Searching in Wikipedia => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://wikipedia.org/wiki/Special:Search/' + parser.parse_request(com[1:]))
        elif com[0] == "amazon":
            print(
            wcolors.color.GREEN + "Searching in Amazon => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('http://www.amazon.com/s?url=search-alias=aps&field-keywords=' + parser.parse_request(com[1:]))
        elif com[0] == "remove" or com[0] == "rm":
            print(wcolors.color.GREEN + "Removing => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            os.remove(com[1])
        elif com[0] == "exec":
            os.system(parser.parse_request(com[1:]))
        elif com[0] == "weather":
            print(
            wcolors.color.GREEN + "Opening Weather Underground for => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open(
                'http://www.wunderground.com/cgi-bin/findweather/hdfForecast?query=' + parser.parse_request(com[1:]))
        elif com[0] == "facebook":
            print(
            wcolors.color.GREEN + "Searching in Facebook => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.facebook.com/search/results.php?q=' + parser.parse_request(com[1:]))
        elif com[0] == "wolfram":
            print(
            wcolors.color.GREEN + "Searching in Wolfram => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.wolframalpha.com/input/?i=' + parser.parse_request(com[1:]))
        elif com[0] == "rotten":
            print(
            wcolors.color.GREEN + "Searching in Rotten Tomatoes => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('http://www.rottentomatoes.com/search/?search=' + parser.parse_request(com[1:]))
        elif com[0] == "translate":
            print(
            wcolors.color.GREEN + "Translating using Google Translate => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://translate.google.com/?text=' + parser.parse_request(com[1:]))
        else:
            print wcolors.color.RED + "Invalid command => " + parser.parse_request(com[
                                                                            0:]) + "." + wcolors.color.ENDC + wcolors.color.GREEN + " Trying search in Google." + wcolors.color.ENDC
            webbrowser.open('https://www.google.com/search?q=' + parser.parse_request(com[0:]))