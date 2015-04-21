import webbrowser
import wcolors

from core import parser


class Formula():
    def __init__(self, request):
        self.request = request

    def search(self):
        print(
            wcolors.color.GREEN + "Searching in Wolfram => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                self.request[0:]) + wcolors.color.ENDC)
        webbrowser.open('https://www.wolframalpha.com/input/?i=' + parser.parse_request(self.request[0:]))

    def main(self):
        self.search()