import os
from core import parser


class Formula():
    def __init__(self, request):
        self.request = request

    def execute(self):
        os.system(parser.parse_request(self.request[1:]))

    def main(self):
        self.execute()