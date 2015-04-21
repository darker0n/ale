#!/usr/bin/env python

import webbrowser
import readline
import os
import imp

from core import wcolors
from core import parser
from core import formules


search_engines = ["google", "maps", "youtube", "yahoo", "wiki", "notes", "amazon", "weather",
                  "facebook", "wolfram", "rotten", "translate"]

applications = os.listdir("/Applications")

commands = ["remove", "rm", "exec"] + applications + search_engines


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

        # Searching command in Formules
        elif com[0] + ".py" in formules.check_formules():
            module = imp.load_source(com[0], "core/Formula/" + com[0] + ".py")
            formula = module.Formula(request=com[1:])
            formula.main()

        # Opening applications
        elif parser.parse_request(com[0:]).strip() in applications:
            print(wcolors.color.GREEN + "Opening => " + parser.parse_request(com[0:]).strip() + wcolors.color.ENDC)
            os.system("open -a /Applications/" + parser.word_space(parser.parse_request(com[0:]).strip()))
        else:
            print wcolors.color.RED + "Invalid command => " + parser.parse_request(com[
                                                                                   0:]) + "." + wcolors.color.ENDC + wcolors.color.GREEN + " Trying search in Google." + wcolors.color.ENDC
            webbrowser.open('https://www.google.com/search?q=' + parser.parse_request(com[0:]))