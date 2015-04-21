#!/usr/bin/env python

import webbrowser
import wcolors
from core import parser


class Formula():
    def __init__(self, request):
        self.request = request

    def open(self):
        print(wcolors.color.GREEN + "Opening Twitter..." + wcolors.color.ENDC)
        webbrowser.open('https://twitter.com')

    def search(self):
        print(wcolors.color.GREEN + "Searching in Twitter => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(self.request[0:]) + wcolors.color.ENDC)

        webbrowser.open('https://twitter.com/search?q=' + parser.parse_request(self.request[0:]))

    def main(self):
        if len(self.request) > 0:
            self.search()
        else:
            self.open()