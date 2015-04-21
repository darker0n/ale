import webbrowser
import wcolors
from core import parser


class Formula():
    def __init__(self, request):
        self.request = request

    def search(self):
        print(wcolors.color.GREEN + "Searching in Google Images => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(self.request[0:]) + wcolors.color.ENDC)

        webbrowser.open('https://www.google.com/search?q=' + parser.parse_request(self.request[0:]) + "&tbm=isch")

    def main(self):
        self.search()