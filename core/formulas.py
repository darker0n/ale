#!/usr/bin/env python
import os
import parser

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def formulas_list():
    return [w.replace('.py', "") for w in parser.clear_list(os.listdir(CURRENT_DIR + "/Formula"))]