import re
import math
import string
import itertools
import numpy as np

with open("day5.txt") as f:
    txt = f.read().splitlines()

def mtch(x):
    m = re.search(r'map', x)
    if m:
        return 1
    else:
        return 0
list(map(mtch, txt))
list(map(mtch, txt)).index(1)
list(map(mtch, txt)).count(1)

d,s,r = 50, 98, 2
list(range(d, d+r))
m = dict(zip(list(range(d, d+r)), list(range(s, s+r))))

seeds = re.sub(r'[^\d|\s]', '', txt[0]).split()
seeds = [int(s) for s in seeds]
headers = list(map(mtch, txt))
cnt = list(map(mtch, txt)).count(1)
idx = list(range(len(txt)))

map_start = [i for i in idx if headers[i]==1]
map_end = map_start[1:]
map_end.append(len(txt) + 1)

for i in range(cnt):
    map_values = txt[map_start[i]+1 : map_end[i]-1]
    print(map_values)


for i in range(cnt):
    map_values = txt[map_start[i]+1 : map_end[i]-1]
    new_seeds = []
    for _, val in enumerate(map_values):
        d, s, r = map(int, val.split())
        src = range(s, s+r)
        diff = d-s
        found = [seed for seed in seeds if seed in range(s, s+r)]
        s1 = [seed+diff for seed in seeds if seed in range(s, s+r)] #new mapping
        s2 = [seed for seed in seeds if seed not in range(s, s+r)] #not mapped
        new_seeds = new_seeds + s1
        seeds = list(set(s2).difference(set(new_seeds)))
    print(seeds)
    seeds = new_seeds + seeds

print(min(seeds))
seeds

#part 2
with open("day5-sample.txt") as f:
    txt = f.read().splitlines()

with open("day5.txt") as f:
    txt = f.read().splitlines()

headers = list(map(mtch, txt))
cnt = list(map(mtch, txt)).count(1)
idx = list(range(len(txt)))

list(itertools.compress(txt, headers))

map_start = [i for i in idx if headers[i]==1]
map_end = map_start[1:]
map_end.append(len(txt) + 1)

#we'll go through the mapping in reverse
map_start.reverse()
map_end.reverse()

seeds = re.sub(r'[^\d|\s]', '', txt[0]).split()
seeds = [int(s) for s in seeds]

pairs = list(itertools.batched(seeds, 2))
pairs = [(x, x+y) for x, y in pairs]
seed_range = itertools.starmap(range, pairs)
seed_list = list(seed_range)

#we only care about the lowest location
#so start at 0 and do the mapping in reverse.  Then check to see if it's in the starting seed list.  
startlocation = 0
while True:
    location = startlocation
    for i in range(cnt):
        map_values = txt[map_start[i]+1 : map_end[i]-1]
        for _, val in enumerate(map_values):
            d, s, r = map(int, val.split())
            dest = range(d, d+r)
            diff = d-s
            if location in dest:
                location -= diff
                break
    if [True for x in seed_list if location in x]:
        print(startlocation, location)
        break
    else:
        startlocation += 1
    if startlocation % 1_000_000 == 0:
        print(startlocation)
