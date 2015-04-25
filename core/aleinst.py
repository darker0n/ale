#!/usr/bin/env python
import os
import imp

from core import parser
from core import wcolors


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class Aleinst():
    def __init__(self, request):
        self.request = request

    def package_list(self):
        return [w.replace('.py', "") for w in parser.clear_list(os.listdir(CURRENT_DIR + "/Package"))]

    def usage(self):
        print "Usage: aleinst [package]"

    def search(self):
        if len(self.request) > 0:
            print(
                wcolors.color.GREEN + "Searching in Ale Packages => " + wcolors.color.ENDC + wcolors.color.RED + parser.parse_request(
                    self.request[0:]) + wcolors.color.ENDC)
            if self.request[0] in self.package_list():
                module = imp.load_source(self.request[0], CURRENT_DIR + "/Package/" + self.request[0] + ".py")
                package = module.Package(request=self.request[0:])
                package.main()
        else:
            print wcolors.color.RED + "Error: No arguments." + wcolors.color.ENDC
            self.usage()