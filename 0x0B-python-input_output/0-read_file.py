#!/usr/bin/python3
"""
Function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """read file in utf8 using  with """
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
