import re
import math
import string
import operator
import itertools

with open("day6.txt") as f:
    txt = f.read().splitlines()

len(txt)
times = [int(i) for i in re.sub(r'[^\d|\s]', '', txt[0]).split()]
dist = [int(i) for i in re.sub(r'[^\d|\s]', '', txt[1]).split()]

win_count = []
for t,d in zip(times, dist):
    total_time = t
    speeds = list(range(1, t))
    time_left = [total_time - s for s in speeds]
    dist_travel = itertools.starmap(operator.mul, zip(speeds, time_left))
    win = [1 for dist in dist_travel if dist > d]
    print(win)
    win_count.append(sum(win))

list(itertools.accumulate(win_count, operator.mul))

#part2
time = int(re.sub(r'[^\d]', '', txt[0]))
dist = int(re.sub(r'[^\d]', '', txt[1]))

speeds = range(1, time)
time_left = [time - s for s in speeds]
dist_travel = itertools.starmap(operator.mul, zip(speeds, time_left))
win = [1 for d in dist_travel if d > dist]
sum(win)