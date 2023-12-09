import re
import math
import string
import operator
import itertools
import collections

with open("day8.txt") as f:
    txt = f.read().splitlines()

instr = txt[0]
nodes = txt[2:]

nodes[0].split()[0]
re.findall(r'(?<== ).+', nodes[0])
re.findall(r'\w+', nodes[0])

lookup = dict(zip(
    [re.findall(r'\w+', i)[0] for i in nodes],
    [re.findall(r'\w+', i)[1:] for i in nodes]
))

lr = {'L': 0, 'R': 1}

cnt = 0
cur_loc = 'AAA'
while cur_loc != 'ZZZ':
    for i in instr:
        choices = lookup[cur_loc]
        next_move = choices[lr[i]]
        cur_loc = next_move
        cnt += 1
        if cur_loc == 'ZZZ':
            break
print(cnt)

#part 2
[i for i in lookup.keys() if i.endswith('A')]
[i for i in lookup.keys() if i.endswith('Z')]

start_locs = [i for i in lookup.keys() if i.endswith('A')]
end_locs = [i for i in lookup.keys() if i.endswith('Z')]
info = dict.fromkeys(start_locs)
for loc in start_locs:
    start_loc = loc
    cnt = 0
    while not loc.endswith('Z'):
        for i in instr:
            choices = lookup[loc]
            next_move = choices[lr[i]]
            loc = next_move
            cnt += 1
            if loc.endswith('Z'):
                info[start_loc] = (cnt, loc)
                break
#how long it take each starting position to reach end individually
print(info)
[v[0] for k,v in info.items()]

list(itertools.accumulate([v[0] for k,v in info.items()], operator.mul))
math.lcm(20093, 12169)

#check
cnt = 0
cur_loc = ['GNA', 'FCA']
while len(cur_loc) != len([i for i in cur_loc if i.endswith('Z')]):
    for i in instr:
        choices = [lookup[cur] for cur in cur_loc]
        next_move = [c[lr[i]] for c in choices]
        cur_loc = next_move
        cnt += 1
        if len([i for i in cur_loc if i.endswith('Z')]) == 2:
            break

#Take the LCM for the steps is takes each starting spot to reach a Z
math.lcm(*[v[0] for k,v in info.items()])


# ####This works, but would take forever....
# cnt = 0
# cur_loc = [i for i in lookup.keys() if i.endswith('A')]
# zmax = 0
# while len(cur_loc) != len([i for i in cur_loc if i.endswith('Z')]):
#     for i in instr:
#         choices = [lookup[cur] for cur in cur_loc]
#         next_move = [c[lr[i]] for c in choices]
#         cur_loc = next_move
#         cnt += 1
#         if len([i for i in cur_loc if i.endswith('Z')]) == 6:
#             break
#     if len([i for i in cur_loc if i.endswith('Z')]) > zmax:
#         zmax = len([i for i in cur_loc if i.endswith('Z')])
#         print(f'Count: {cnt}')
#         print(f'Z Count: {zmax}')

