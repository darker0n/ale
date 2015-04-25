from core import wcolors
from core import parser

from Formula import google
from Formula import amazon
from Formula import wiki


def main(com):
    print wcolors.color.RED + "Invalid command." + wcolors.color.ENDC + wcolors.color.GREEN + " You can:" + wcolors.color.ENDC
    print wcolors.color.GREEN + "['] " + wcolors.color.ENDC + "Search Google for " + wcolors.color.DARKCYAN + parser.parse_request(
        com) + wcolors.color.ENDC
    print wcolors.color.GREEN + "[;] " + wcolors.color.ENDC + "Search Wikipedia for " + wcolors.color.DARKCYAN + parser.parse_request(
        com) + wcolors.color.ENDC
    print wcolors.color.GREEN + "[l] " + wcolors.color.ENDC + "Search Amazon for " + wcolors.color.DARKCYAN + parser.parse_request(
        com) + wcolors.color.ENDC
    print wcolors.color.GREEN + "[enter] " + wcolors.color.ENDC + "Skip" + wcolors.color.ENDC
    print
    command = raw_input(
        wcolors.color.YELLOW + "ale:" + wcolors.color.ENDC + wcolors.color.RED + "search" + wcolors.color.ENDC + wcolors.color.YELLOW + "> " + wcolors.color.ENDC).split()
    if len(command) == 0:
        return 0
    if command[0] == "'":
        formula = google.Formula(request=com[0:])
        formula.main()
    elif command[0] == "l":
        formula = amazon.Formula(request=com[0:])
        formula.main()
    elif command[0] == ";":
        formula = wiki.Formula(request=com[0:])
        formula.main()
    else:
        return 0