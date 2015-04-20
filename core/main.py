#!/usr/bin/env python

import webbrowser
import readline
import os
from core import wcolors

commands = ["google", "maps", "youtube", "yahoo", "gmail", "wiki", "notes", "amazon", "remove", "rm", "exec", "weather",
            "facebook", "emptytrash", "wolfram", "rotten", "translate"] + os.listdir("/Applications")


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


def word_space(path):
    path = path.split(" ")
    new_path = ""
    i = 0
    for x in path:
        if len(path) - i == 1:
            new_path += x
        else:
            new_path += x + "\\ "
            i += 1
    return new_path


def start():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    print (wcolors.color.GREEN + "Welcome to ale, smart shell for more productive work." + wcolors.color.ENDC)


def main():
    while True:
        com = raw_input(wcolors.color.YELLOW + "ale> " + wcolors.color.ENDC).split()
        if len(com) == 0:
            main()
        if parse_request(com[0:]).strip() in commands:
            print(wcolors.color.GREEN + "Opening => " + parse_request(com[0:]).strip() + wcolors.color.ENDC)
            os.system("open -a /Applications/" + word_space(parse_request(com[0:]).strip()))
        elif com[0] == "google":
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
        elif com[0] == "remove" or com[0] == "rm":
            print(wcolors.color.GREEN + "Removing => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            os.remove(com[1])
        elif com[0] == "exec":
            os.system(parse_request(com[1:]))
        elif com[0] == "weather":
            print(wcolors.color.GREEN + "Opening Weather Underground for => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('http://www.wunderground.com/cgi-bin/findweather/hdfForecast?query=' + parse_request(com[1:]))
        elif com[0] == "facebook":
            print(wcolors.color.GREEN + "Searching in Facebook => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.facebook.com/search/results.php?q=' + parse_request(com[1:]))
        elif com[0] == "emptytrash":
            print(wcolors.color.GREEN + "Cleaning trash..." + wcolors.color.ENDC)
            os.system("trash-empty")
        elif com[0] == "wolfram":
            print(wcolors.color.GREEN + "Searching in Wolfram => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://www.wolframalpha.com/input/?i=' + parse_request(com[1:]))
        elif com[0] == "rotten":
            print(wcolors.color.GREEN + "Searching in Rotten Tomatoes => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('http://www.rottentomatoes.com/search/?search=' + parse_request(com[1:]))
        elif com[0] == "translate":
            print(wcolors.color.GREEN + "Translating using Google Translate => " + wcolors.color.ENDC + wcolors.color.RED + parse_request(com[1:]) + wcolors.color.ENDC)
            webbrowser.open('https://translate.google.com/?text=' + parse_request(com[1:]))
        else:
            print wcolors.color.RED + "Invalid command => " + parse_request(com[0:]) + "." + wcolors.color.ENDC + wcolors.color.GREEN + " Trying search in Google." + wcolors.color.ENDC
            webbrowser.open('https://www.google.com/search?q=' + parse_request(com[0:]))