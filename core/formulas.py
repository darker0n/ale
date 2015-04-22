#!/usr/bin/env python
import os
import parser


def formulas_list():
    return [w.replace('.py', "") for w in parser.clear_list(os.listdir(os.getcwd() + "/core/Formula"))]