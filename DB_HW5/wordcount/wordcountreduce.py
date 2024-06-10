#!/usr/bin/env python3
import sys

# In Hadoop streaming, the reducer gets the data form the stdin.
# And the reducer pipes the output of the results to the stdout.
last_word = None
counts = 0

# Gets key_value pairs grouped by key
# Gets key_value pairs one by one
for word_count in sys.stdin:
    word_count = word_count.strip()  # Removes whitespace from key_value string
    # Splits a key_value string into a key and a value.
    word, count = word_count.split("\t")
    count = int(count)

    # If the key (word) is the same, the count increases.
    if last_word == word:
        counts += count
    else:
        if last_word:  # last_word is not none
            print("%s: %s" % (last_word, counts))
        counts = count
        last_word = word

if last_word:  # last_word is not none
    print("%s: %s" % (last_word, counts))