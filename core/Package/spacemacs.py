from core import wcolors
import os


class Package():
    def __init__(self, request):
        self.request = request
        self.name = "Spacemacs"
        self.version = "24.5.1"

    def install(self):
        print(wcolors.color.GREEN + "Installing => " + wcolors.color.ENDC + wcolors.color.RED + self.name + wcolors.color.ENDC)
        os.system("git clone --recursive http://github.com/syl20bnr/spacemacs ~/.emacs.d")
