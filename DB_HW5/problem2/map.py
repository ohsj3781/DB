#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",")  # Splits a string into a list.

    name = tuple_list[0]
    goal = tuple_list[1]
    assist = tuple_list[2]

    print('{0}\t{1}'.format(name, goal+','+assist))
