#!/usr/bin/env python
import os


def check_formulas():
    return os.listdir(os.getcwd() + "/core/Formula")


def formulas_list():
    return [w.replace('.py', "") for w in os.listdir(os.getcwd() + "/core/Formula")]