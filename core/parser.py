#!/usr/bin/env python


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