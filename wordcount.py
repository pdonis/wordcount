#!/usr/bin/env python
# Python program to solve the Knuth-McIlroy problem
# See here: http://www.leancrew.com/all-this/2011/12/more-shell-less-egg/
# 
# Problem spec:
# Read a file of text, determine the n most frequently used words, and
# print out a sorted list of those words along with their frequencies.
# 
# McIlroy's 6-line shell pipeline solution is in wordcount.sh for comparison.
# Of course this Python solution is more than 6 lines, but it still reuses
# standard tools instead of custom-coding; we are basically replicating the
# shell pipeline in Python (except that we lowercase before translating since
# that turns out to be easier with the Python tools at hand)


from collections import defaultdict
from re import compile, sub


# Hack to make sure every byte except lowercase ASCII gets translated to a space

rexp = compile(r"[^a-z]")


def uniq(words):
    """Return dict of words vs. occurrences from iterable of words.
    """
    counts = defaultdict(lambda: 0)
    for word in words:
        counts[word] += 1
    return counts


def pipeline(s, n):
    """Return sorted list of n most used words in s, handling contractions.
    
    Note that we sort by both word count and word to match the behavior of
    the shell pipeline (multiple words with the same count are output in
    reverse alphabetical order).
    """
    return sorted(
        uniq(
            sub(rexp, " ", s.lower())
            .split()
        ).iteritems(), key=lambda x: (x[1], x[0]), reverse=True)[:n]


if __name__ == '__main__':
    import sys
    
    for w, f in pipeline(sys.stdin.read(), int(sys.argv[1])):
        # Match the shell pipeline output format
        print str(f).rjust(7), w
