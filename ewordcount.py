#!/usr/bin/env python
# Python program to solve the Knuth-McIlroy problem
# -- enhanced version to handle contractions
# See here: http://www.leancrew.com/all-this/2011/12/more-shell-less-egg/
# 
# Problem spec:
# Read a file of text, determine the n most frequently used words, and
# print out a sorted list of those words along with their frequencies.
# 
# The enhanced version of McIlroy's shell pipeline solution is in ewordcount.sh
# for comparison.


from string import lowercase, maketrans
from collections import defaultdict
from re import compile, sub


# Hacks to make sure every byte except lowercase ASCII and apostrophe gets translated to a space

_h, _t = maketrans("", "").split("'")
_sfrom = ''.join([_h] + _t.split(lowercase))
_sto = ' ' * len(_sfrom)

table = maketrans(_sfrom, _sto)

rexp1 = compile(r"([^A-Za-z])\'")
rexp2 = compile(r"\'([^A-Za-z])")


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
            sub(rexp2, " ", sub(rexp1, " ", s))
            .lower()
            .translate(table)
            .split()
        ).iteritems(), key=lambda x: (x[1], x[0]), reverse=True)[:n]


if __name__ == '__main__':
    import sys
    
    for w, f in pipeline(sys.stdin.read(), int(sys.argv[1])):
        # Match the shell pipeline output format
        print str(f).rjust(7), w
