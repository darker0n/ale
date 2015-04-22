import os
from core import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def clear(self):
        print(wcolors.color.GREEN + "Cleaning trash..." + wcolors.color.ENDC)
        os.system("trash-empty")

    def main(self):
        self.clear()