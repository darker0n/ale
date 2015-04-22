import subprocess
import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def logout(self):
        print(wcolors.color.GREEN + "Logging out..." + wcolors.color.ENDC)
        subprocess.call(['osascript', '-e', 'tell app "System Events" to log out'])

    def main(self):
        self.logout()