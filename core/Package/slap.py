from core import wcolors
import os


class Package():
    def __init__(self, request):
        self.request = request
        self.name = "Slap"
        self.version = "0.1.24"

    def install(self):
        print(wcolors.color.GREEN + "Installing => " + wcolors.color.ENDC + wcolors.color.RED + self.name + wcolors.color.ENDC)
        os.system("curl -sL https://raw.githubusercontent.com/slap-editor/slap/master/install.sh | sh")
