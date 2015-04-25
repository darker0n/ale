import os
from core import aleinst

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class Formula():
    def __init__(self, request):
        self.request = request

    def search(self):
        package = aleinst.Aleinst(request=self.request[0:])
        package.search()

    def main(self):
        self.search()