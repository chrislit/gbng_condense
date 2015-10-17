# gbng_condense
Google Books Ngram data condenser


**gnbg_condense.py** by Chris Little, 2014

Creative Commons: CC0 licensed (https://creativecommons.org/publicdomain/zero/1.0/)
But note, data derived from Google Books Ngrams are licensed (by Google) as CC BY: (https://creativecommons.org/licenses/by/3.0/)

I'm throwing this on GitHub in case it's useful to anyone. The code isn't
particularly pretty, there's no CLI, and it wasn't really intended for public
consumption. YMMV, etc.


A simple script to condense years of Google Books Ngrams data into a single
line per n-gram. This is useful if you care about frequency across the whole
corpus, but don't particularly care about frequency by year.

It also strips POS tags from words (but this is easily disabled) and
omits words without any Latin letters.

There are three variables to set:
- start_year: a year, before which n-grams will be discarded
- nmin: the lower bound n value for n-grams
- nmax: the upper bound n value for n-grams

The script assumes that it is run in a directory with sub-directories named
"1gram", "2gram", etc. and produces files named "en_1grams.txt", etc. for
each requested value of n.
