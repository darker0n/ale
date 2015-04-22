import subprocess
import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def restart(self):
        print(wcolors.color.GREEN + "Restarting..." + wcolors.color.ENDC)
        subprocess.call(['osascript', '-e', 'tell app "System Events" to restart'])

    def main(self):
        self.restart()