from core import wcolors
from core import parser

from Formula import google
from Formula import amazon
from Formula import wiki


def main(com):
    print wcolors.color.RED + "Invalid command." + wcolors.color.ENDC + wcolors.color.GREEN + " You can:" + wcolors.color.ENDC
    print wcolors.color.GREEN + "[0] " + wcolors.color.ENDC + "Search Google for " + wcolors.color.DARKCYAN + parser.parse_request(
        com) + wcolors.color.ENDC
    print wcolors.color.GREEN + "[1] " + wcolors.color.ENDC + "Search Amazon for " + wcolors.color.DARKCYAN + parser.parse_request(
        com) + wcolors.color.ENDC
    print wcolors.color.GREEN + "[2] " + wcolors.color.ENDC + "Search Wikipedia for " + wcolors.color.DARKCYAN + parser.parse_request(
        com) + wcolors.color.ENDC
    print wcolors.color.GREEN + "[another key] " + wcolors.color.ENDC + "Skip" + wcolors.color.ENDC
    print
    command = raw_input(
        wcolors.color.YELLOW + "ale:" + wcolors.color.ENDC + wcolors.color.RED + "search" + wcolors.color.ENDC + wcolors.color.YELLOW + "> " + wcolors.color.ENDC).split()
    if command[0] == "0":
        formula = google.Formula(request=com[0:])
        formula.main()
    elif command[0] == "1":
        formula = amazon.Formula(request=com[0:])
        formula.main()
    elif command[0] == "2":
        formula = wiki.Formula(request=com[0:])
        formula.main()
    else:
        return 0