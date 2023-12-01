#!/usr/bin/python3
import sys

list_argument = sys.argv
no_argument = len(list_argument) - 1


if no_argument > 1:
    print("{} arguments:".format(no_argument))
    for i in range(1, no_argument + 1):
        print("{}: {}".format(i, list_argument[i]))
elif no_argument == 0:
    print("{} arguments.".format(no_argument))
else:
    print("{} arguments:".format(no_argument))
    print("{}: {}".format(no_argument, list_argument[1]))
