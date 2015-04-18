#!/usr/bin/env python
import webbrowser
import readline

commands = ["google"]


def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)
while True:
    com = raw_input("ale> ").split()
    if com[0] == "google":
        webbrowser.open('https://www.google.ru/?q=' + com[1] + '#newwindow=1&q=' + com[1])