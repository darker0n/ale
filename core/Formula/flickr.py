import webbrowser
from core import wcolors
from core import parser


class Formula():
    def __init__(self, request):
        self.request = request

    def search(self):
        print(wcolors.color.GREEN + "Searching in Flickr => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(self.request[0:]) + wcolors.color.ENDC)

        webbrowser.open('https://www.flickr.com/search/?q=' + parser.parse_request(self.request[0:]))

    def main(self):
        self.search()