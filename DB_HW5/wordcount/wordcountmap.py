#!/usr/bin/env python3


import sys

# In Hadoop streaming, the mapper converts the input data into strings of text and pipes it to the stdin.
# And the mapper pipes the output of the key-value pair to the stdout.

for line in sys.stdin:  # Reads input data line by line
    line = line.strip()  # Removes whitespace from string
    word_list = line.split()  # Splits a string into a word list.

    for word in word_list:
        count = 1
        print('{0}\t{1}'.format(word, count))  # word = key, count = value
