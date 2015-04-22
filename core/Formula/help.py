#!/usr/bin/env python

import webbrowser
from core import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def open(self):
        print(wcolors.color.GREEN + "Opening Ale Wiki..." + wcolors.color.ENDC)
        webbrowser.open('https://github.com/darker0n/ale/wiki')

    def main(self):
        self.open()