#!/bin/sh
# McIlroy's shell pipeline to solve the Knuth-McIlroy problem
# -- enhanced version to handle contractions
# -- incorporates bug fix done in wordcount.sh
# See here: http://www.leancrew.com/all-this/2011/12/more-shell-less-egg/
# 
# Problem spec:
# Read a file of text, determine the n most frequently used words, and
# print out a sorted list of those words along with their frequencies.
# 
# This is a modified version of Doug McIlroy's shell pipeline solution;
# the Python solution for this enhanced version is in ewordcount.py.
# 
# In the spirit of McIlroy's own concise documentation of his pipeline,
# here is what the first four lines (the ones I added) do:
# 
# * Convert quotes at start of words to spaces
# * Convert quotes at start of lines to spaces
# * Convert quotes at end of words to spaces
# * Convert quotes at end of lines to spaces
# 
# The only other change is to the sixth (formerly first of McIlroy's,
# second of the bug-fixed version--see wordcount.sh for notes on the bug
# fix) line, to include any remaining quotes (which will be those in words
# that are contractions) in the list of characters not converted to
# newlines

sed s/[^A-Za-z]\'/\ / |
sed s/^\'/\ / |
sed s/\'[^A-Za-z]/\ / |
sed s/\'$/\ / |
sed '/^$/d' |
tr -cs \'A-Za-z '\n' |
tr A-Z a-z |
sort |
uniq -c |
sort -rn |
sed ${1}q
