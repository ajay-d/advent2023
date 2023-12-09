import re
import math
import string
import operator
import itertools
import collections

with open("day7.txt") as f:
    txt = f.read().splitlines()

#ever possible hand, sorted by rank highest to lowest (for sorting)
score = dict(zip([v for i,v in enumerate([''.join(x) for x in itertools.product('AKQJT98765432', repeat=5)])],
                 [i for i,v in enumerate([''.join(x) for x in itertools.product('AKQJT98765432', repeat=5)])]))

ranks = []
hands = []
bids = []
for i,v in enumerate(txt):
    h,b = v.split()
    element = sorted([h.count(i) for i in set(h)])
    ranks.append(tuple(element))
    hands.append(h)
    bids.append(int(b))

#these are the seven types of hands
collections.Counter(ranks)
bid_lookup = dict(zip(hands, bids))

list(collections.Counter(ranks))

ranks_ordered = [(5,), (1,4), (2,3), (1,1,3), (1,2,2), (1,1,1,2), (1,1,1,1,1)]
bids_ordered = []
hands_ordered = []
for r in ranks_ordered:
    vec_filter = [1 if x == r else 0 for x in ranks]
    hands_matched = list(itertools.compress(hands, vec_filter))
    hands_sorted = sorted(hands_matched, key = lambda x: score[x])
    for h in hands_sorted:
        bids_ordered.append(bid_lookup[h])
        hands_ordered.append(h)


sum(itertools.starmap(operator.mul, zip(bids_ordered, range(1000, 0, -1))))

#part 2

#ever possible hand, sorted by rank highest to lowest (for sorting)
score = dict(zip([v for i,v in enumerate([''.join(x) for x in itertools.product('AKQT98765432J', repeat=5)])],
                 [i for i,v in enumerate([''.join(x) for x in itertools.product('AKQT98765432J', repeat=5)])]))

rank_lookup = dict(zip(hands, ranks))

J = []
for i in hands:
    if 'J' in i:
        J.append(i)

collections.Counter([i.count('J') for i in J])
orig_rank = [rank_lookup[j] for j in J]
collections.Counter(orig_rank)

[i for i in J if rank_lookup[i]==(1,4)]

for j in J:
    other = [x for x in j if x!='J']
    for suit in set(other):
        j_other = j.replace('J', suit)
        element = sorted([j_other.count(x) for x in set(j_other)])
        ranks_ordered.index(tuple(element))
        if ranks_ordered.index(tuple(element)) < ranks_ordered.index(rank_lookup[j]):
            print('better')
            rank_lookup[j] = tuple(element)
            idx = hands.index(j)
            ranks[idx] = tuple(element)

new_rank = [rank_lookup[j] for j in J]
collections.Counter(new_rank)

ranks_ordered = [(5,), (1,4), (2,3), (1,1,3), (1,2,2), (1,1,1,2), (1,1,1,1,1)]
bids_ordered = []
hands_ordered = []
for r in ranks_ordered:
    vec_filter = [1 if x == r else 0 for x in ranks]
    hands_matched = list(itertools.compress(hands, vec_filter))
    hands_sorted = sorted(hands_matched, key = lambda x: score[x])
    for h in hands_sorted:
        bids_ordered.append(bid_lookup[h])
        hands_ordered.append(h)

sum(itertools.starmap(operator.mul, zip(bids_ordered, range(1000, 0, -1))))