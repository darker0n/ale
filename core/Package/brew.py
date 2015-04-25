from core import wcolors
import os


class Package():
    def __init__(self, request):
        self.request = request
        self.name = "Brew"

    def install(self):
        print(wcolors.color.GREEN + "Installing => " + wcolors.color.ENDC + wcolors.color.RED + self.name + wcolors.color.ENDC)
        os.system("ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"")

    def main(self):
        self.install()