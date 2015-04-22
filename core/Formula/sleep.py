import subprocess
from core import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def sleep(self):
        print(wcolors.color.GREEN + "Going to sleep..." + wcolors.color.ENDC)
        subprocess.call(['osascript', '-e', 'tell app "System Events" to sleep'])

    def main(self):
        self.sleep()