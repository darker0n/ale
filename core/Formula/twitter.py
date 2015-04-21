#!/usr/bin/env python

import webbrowser
import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def open(self):
        print(wcolors.color.GREEN + "Opening Twitter..." + wcolors.color.ENDC)
        webbrowser.open('https://twitter.com')

    def main(self):
        self.open()