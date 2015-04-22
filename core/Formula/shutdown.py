import subprocess
import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def shutdown(self):
        print(wcolors.color.GREEN + "Shutting down..." + wcolors.color.ENDC)
        subprocess.call(['osascript', '-e', 'tell app "System Events" to shut down'])

    def main(self):
        self.shutdown()