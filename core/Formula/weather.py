import webbrowser
import wcolors

from core import parser


class Formula():
    def __init__(self, request):
        self.request = request

    def search(self):
        print(
            wcolors.color.GREEN + "Opening Weather Underground for => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                self.request[0:]) + wcolors.color.ENDC)
        webbrowser.open(
            'http://www.wunderground.com/cgi-bin/findweather/hdfForecast?query=' + parser.parse_request(self.request[0:]))

    def main(self):
        self.search()