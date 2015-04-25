#!/usr/bin/env python

import readline
import os
import imp
import subprocess

from core import wcolors
from core import parser
from core import formulas
from core import invalid_command
from core import aliase


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# List with all formula files
formulas_list = formulas.formulas_list()
# List with all applications
applications = parser.applications_list()
# List with aliases
aliases = os.listdir(CURRENT_DIR + "/Aliases")

commands = applications + formulas_list + aliases


def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


# Start message.
# Completer function (complete command with Tab)
def start():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    print (wcolors.color.GREEN + "Welcome to ale, smart command line launcher for OS X." + wcolors.color.ENDC)


def main():
    while True:
        com = raw_input(wcolors.color.YELLOW + "ale> " + wcolors.color.ENDC).split()

        if len(com) == 0:
            main()

        # Searching command in Formules
        elif com[0] in formulas.formulas_list():
            module = imp.load_source(com[0], CURRENT_DIR + "/Formula/" + com[0] + ".py")
            formula = module.Formula(request=com[1:])
            formula.main()

        # Searching command in Aliases
        elif com[0] in aliases:
            aliase.open_formula(com)

        # Searching in Applications
        elif parser.parse_request(com[0:]).strip() in applications:
            print(wcolors.color.GREEN + "Opening => " + parser.parse_request(com[0:]).strip() + wcolors.color.ENDC)
            os.system("open -a /Applications/" + parser.word_space(parser.parse_request(com[0:]).strip()) + ".app")

        # Trying execute command in default shell
        else:
            try:
                subprocess.call(com)
            except OSError:
                invalid_command.main(com)