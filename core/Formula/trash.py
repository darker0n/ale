import subprocess
import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def trash(self):
        print(wcolors.color.GREEN + "Opening trash..." + wcolors.color.ENDC)
        subprocess.call(['osascript', '-e', 'tell app "Finder" to open trash'])

    def main(self):
        self.trash()