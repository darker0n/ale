from core import wcolors


class Formula():
    def __init__(self, request):
        self.request = request

    def main(self):
        print wcolors.color.GREEN + "Version => " + wcolors.color.PURPLE + "0.1.1" + wcolors.color.ENDC