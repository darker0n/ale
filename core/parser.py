#!/usr/bin/env python
import os


def parse_request(arr):
    request = ""
    for x in arr:
        request += x + " "
    return request


def word_space(path):
    path = path.split(" ")
    new_path = ""
    i = 0
    for x in path:
        if len(path) - i == 1:
            new_path += x
        else:
            new_path += x + "\\ "
            i += 1
    return new_path


def clear_list(list):
    for f in list:
        if f.startswith('.') or f.endswith("__") or f.endswith(".pyc"):
            list.remove(f)
    return list


def applications_list():
    return clear_list([w.replace('.app', "") for w in os.listdir("/Applications")])