#!/usr/bin/env python

import webbrowser
import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def open(self):
        print(wcolors.color.GREEN + "Opening Gmail..." + wcolors.color.ENDC)
        webbrowser.open('https://mail.google.com/mail')

    def main(self):
        self.open()