The Wordcount Problem
=====================

Here are some scripts relating to the "word count problem" that was the
subject of a memorable exchange between Donald Knuth and Doug McIlroy.
See
[here](http://blog.peterdonis.com/opinions/still-another-nerd-interlude.html)
for context.

Files Included
--------------

McIlroy's original 6-line shell pipeline is in ``wordcount.sh``.

My Python solution to the same original problem is in ``wordcount.py``.

My extended Python solution that correctly handles contractions is in
``ewordcount.py``.

An extended shell pipeline that correctly handles contractions is in
``ewordcount.sh``.

A test text file for use as input is in ``wordcounttest.txt``.

The expected outputs of the two versions, when run on the test text
file, are in ``wordcount.out`` and ``ewordcount.out``. Note that the
outputs include *all* of the words in the file; I generated them by
using a large number (150) as the argument to each script.
