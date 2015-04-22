#!/usr/bin/env python

import readline
import os
import imp
import subprocess

from core import wcolors
from core import parser
from core import formulas
from core import invalid_command

# List with all formulas
formulas_list = parser.clear_list(formulas.formulas_list())
# List with all applications
applications = parser.applications_list()

commands = applications + formulas_list


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
        elif com[0] + ".py" in formulas.check_formulas():
            module = imp.load_source(com[0], "core/Formula/" + com[0] + ".py")
            formula = module.Formula(request=com[1:])
            formula.main()

        # Opening applications
        elif parser.parse_request(com[0:]).strip() in applications:
            print(wcolors.color.GREEN + "Opening => " + parser.parse_request(com[0:]).strip() + wcolors.color.ENDC)
            os.system("open -a /Applications/" + parser.word_space(parser.parse_request(com[0:]).strip()) + ".app")
        else:
            try:
                subprocess.call(com)
            except OSError:
                invalid_command.main(com)