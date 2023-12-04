import re
import math
import string
import math
from collections import Counter
from itertools import repeat

with open("day4.txt") as f:
    txt = f.read().splitlines()

len(txt)
re.findall(r'(?<=: ).+', txt[0])

scores = []
for _, value in enumerate(txt):
    x = re.findall(r'(?<=: ).+', value)
    win = re.split(r'\|', x[0])[0].split()
    card = re.split(r'\|', x[0])[1].split()

    matching = set(win).intersection(set(card))
    score = 2**(len(matching)-1)
    scores.append(score) 
sum(scores)
sum(map(math.floor, scores))

#part 2
dict(zip(range(1, len(txt)+1), repeat(1, len(txt)+1)))
cards_counts = Counter(dict(zip(range(1, len(txt)+1), repeat(1, len(txt)+1))))

#we're counting from 1 to match cards
for card, value in enumerate(txt, start=1):
    x = re.findall(r'(?<=: ).+', value)
    win = re.split(r'\|', x[0])[0].split()
    hand = re.split(r'\|', x[0])[1].split()
    matching = set(win).intersection(set(hand))
    n_matches = len(matching)
    start = card + 1
    stop = start + n_matches
    cards_counts = cards_counts + Counter(dict(zip(range(start, stop), repeat(cards_counts[card], len(matching)+1))))

len(cards_counts)
cards_counts.total()