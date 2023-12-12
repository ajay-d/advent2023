import re
import math
import string
import operator
import itertools
import collections

with open("day9.txt") as f:
    txt = f.read().splitlines()

txt[0]
x=[int(i) for i in txt[0].split()]

x1 = x[1:]
x2 = x[:-1]
list(itertools.starmap(operator.sub, zip(x1,x2)))

vec_next = []
vec_last = []
for i, v in enumerate(txt):
    cur_vec = [int(i) for i in txt[i].split()]
    vec = cur_vec
    #all_zero = all(list(filter(lambda x: x==0, vec)))
    all_zero = all([1 if x==0 else 0 for x in vec])
    last = vec[-1]
    vec_last.append(last)
    vec_add = []
    while not all_zero:
        vec0 = vec[1:]
        vecm1 = vec[:-1]
        diff = list(itertools.starmap(operator.sub, zip(vec0,vecm1)))
        s = sum(diff)
        vec_add.append(diff[-1])
        vec = diff
        #all_zero = all(list(filter(lambda x: x==0, vec)))
        all_zero = all([1 if x==0 else 0 for x in vec])
    print(diff)
    print(len(list(filter(lambda x: x==0, vec))))
    vec_next.append(sum(vec_add))

len(vec_last)
len(vec_next)
list(itertools.starmap(operator.add, zip(vec_last,vec_next)))
sum(itertools.starmap(operator.add, zip(vec_last,vec_next)))

# all(list(filter(lambda x: x==0, vec)))
# all(list(itertools.filterfalse(lambda x: x==0, vec)))
# len(list(itertools.filterfalse(lambda x: x==0, vec)))
# len(list(filter(lambda x: x==0, vec)))

#Part 2
vec_next = []
vec_first = []
vec_diff = []
vec_first_sum = []
for i, v in enumerate(txt):
    cur_vec = [int(i) for i in txt[i].split()]
    vec = cur_vec
    #all_zero = all(list(filter(lambda x: x==0, vec)))
    all_zero = all([1 if x==0 else 0 for x in vec])
    last = vec[-1]
    vec_last.append(last)
    vec_first = []
    vec_first.append(vec[0])
    while not all_zero:
        vec0 = vec[1:]
        vecm1 = vec[:-1]
        diff = list(itertools.starmap(operator.sub, zip(vec0,vecm1)))
        s = sum(diff)
        vec_first.append(diff[0])
        vec_diff.append(diff[-1])
        vec = diff
        #all_zero = all(list(filter(lambda x: x==0, vec)))
        all_zero = all([1 if x==0 else 0 for x in vec])
    for i in range(len(vec_first)-1, 0, -1):
        last1 = vec_first.pop()
        last2 = vec_first.pop()
        diff = last2-last1
        vec_first.append(diff)
    print(vec_first)
    vec_first_sum.append(*vec_first)

sum(vec_first_sum)
