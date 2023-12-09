import re
import math
import string
import operator
import itertools
import collections

with open("day7.txt") as f:
    txt = f.read().splitlines()

len(txt)
txt[0]
h,b = txt[0].split()
[h.count(i) for i in set(h)]
h='444AA'
[h.count(i) for i in set(h)]

cnt = []
for i,v in enumerate(txt):
    h,b = v.split()
    cnt.append(len(set(h)))

collections.Counter(cnt)

score = dict(zip([v for i,v in enumerate(''.join(reversed('AKQJT987654321')))],
                 [i for i,v in enumerate(''.join(reversed('AKQJT987654321')))]))
score = dict(zip([v for i,v in enumerate('AKQJT987654321')],
                 [i for i,v in enumerate('AKQJT987654321')]))
sorted('32T3K', key = lambda x: score[x])


len(list(itertools.combinations_with_replacement('AKQJT987654321', 5)))
len(list(itertools.product('AKQJT987654321', repeat=5)))


cnt = []
hands = []
bids = []
for i,v in enumerate(txt):
    h,b = v.split()
    element = sorted([h.count(i) for i in set(h)])
    cnt.append(tuple(element))
    hands.append(h)
    bids.append(b)
#these are the seven types of hands
collections.Counter(cnt)
len(collections.Counter(cnt))

[int(x==(1,1,1,2)) for x in cnt]
[1 for x in cnt if x == (1,1,1,2)]
[1 if x == (1,1,1,2) else 0 for x in cnt]

score = dict(zip([v for i,v in enumerate(itertools.product('AKQJT987654321', repeat=5))],
                 [i for i,v in enumerate(itertools.product('AKQJT987654321', repeat=5))]))
score = dict(zip([v for i,v in enumerate([''.join(x) for x in itertools.product('AKQJT987654321', repeat=5)])],
                 [i for i,v in enumerate([''.join(x) for x in itertools.product('AKQJT987654321', repeat=5)])]))

vec_filter = [1 if x == (1,4) else 0 for x in cnt]
l = list(itertools.compress(hands, vec_filter))
sorted(l, key = lambda x: score[x])


#check for Js
ranks = []
hands = []
bids = []
for i,v in enumerate(txt):
    h,b = v.split()
    if 'J' in h:
        element = sorted([h.count(i) for i in set(h)])
        ranks.append(tuple(element))
        hands.append(h)
        bids.append(int(b))
collections.Counter(ranks)