#!/bin/sh
# McIlroy's shell pipeline to solve the Knuth-McIlroy problem
# See here: http://www.leancrew.com/all-this/2011/12/more-shell-less-egg/
# 
# Problem spec:
# Read a file of text, determine the n most frequently used words, and
# print out a sorted list of those words along with their frequencies.
# 
# This is Doug McIlroy's six-line shell pipeline solution, for comparison
# with the Python solution in wordcount.py.

tr -cs A-Za-z '\n' |
tr A-Z a-z |
sort |
uniq -c |
sort -rn |
sed ${1}q
