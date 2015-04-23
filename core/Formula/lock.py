import os
from core import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def lock(self):
        print(wcolors.color.GREEN + "Screen locked." + wcolors.color.ENDC)
        os.system("/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend")

    def main(self):
        self.lock()