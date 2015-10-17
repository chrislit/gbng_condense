#!/usr/bin/env python3

# gnbg_condense.py by Chris Little, 2014
# Creative Commons: CC0 licensed (https://creativecommons.org/publicdomain/zero/1.0/)

# A simple script to condense years of Google Books Ngrams data into a single
# line per n-gram. This is useful if you care about frequency across the whole
# corpus, but don't particularly care about frequency by year.
#
# It also strips POS tags from words (but this is easily disabled) and
# omits words without any Latin letters.
#
# There are three variables to set:
#  -- start_year: a year, before which n-grams will be discarded
#  -- nmin: the lower bound n value for n-grams
#  -- nmax: the upper bound n value for n-grams
#
# The script assumes that it is run in a directory with sub-directories named
# "1gram", "2gram", etc. and produces files named "en_1grams.txt", etc. for
# each requested value of n.

from collections import Counter
import re
import os
import gzip

start_year = 1900
nmin = 1
nmax = 1

for n in range(nmin, nmax+1):
    ndir = './{0}gram/'.format(str(n))
    # files = sorted(filter(lambda fn: re.search('\-[a-z_]{1,2}\.gz$', fn), os.listdir(ndir)))
    files = sorted(filter(lambda fn: re.search('.gz$', fn), os.listdir(ndir)))

    with open('en_{0}grams.txt'.format(str(n)), 'w', encoding='utf-8') as outf:
        for fn in files:
            print(fn)

            overall = Counter()
            distinct = Counter()

            with gzip.open(ndir+fn, 'rt', encoding='utf-8') as inf:

                for l in inf:
                    l = l.strip().split('\t')
                    if len(l) > 3:

                        w = l[0]

                        # ignore words before start_year
                        date = int(l[1])
                        if date >= start_year:
                            # strip POS
                            w = re.sub(r'_(NOUN|VERB|ADJ|ADV|PRON|DET|ADP|NUM|CONJ|PRT|\.|X).*', '', w)

                            # omit words without Latin letters
                            if w and re.search('[A-Za-z]', w):
                                #print(l)
                                overall[w] += int(l[2])
                                distinct[w] += int(l[3])

                words = sorted(overall.keys())
                for w in words:
                    outf.write(w + '\t' + str(overall[w]) + '\t' + str(distinct[w]) + '\n')
