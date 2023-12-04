import re
import math
import string

with open("day3.txt") as f:
    txt = f.read().splitlines()

#How to find numbers
nums = re.findall(r'\d+', txt[0])
[re.search(num, txt[0]) for num in nums]

#How to find symbols
re.findall(r'[\D]+', txt[1])
syms = re.findall(r'[^\d\.]+', txt[1])
[re.search(re.escape(sym), txt[1]) for sym in syms]

#Need to match repeated symbols seperately.  
m = re.finditer('#', txt[1])
[i for i in m]

[m[0] for m in re.finditer(r'\d+', txt[1])]
[m.span(0) for m in re.finditer(r'\d+', txt[1])]
[m.span(0) for m in re.finditer(r'[^\d\.]+', txt[1])]

span = [m.span(0) for m in re.finditer(r'\d+', txt[1])]
[list(range(s[0], s[1])) for s in span]

nums_all = []
for row in range(len(txt)):
    row_nums = [int(m[0]) for m in re.finditer(r'\d+', txt[row])]
    nums_all += row_nums
print(len(nums_all))

parts = []
for row in range(len(txt)):
    #nums = re.findall(r'\d+', txt[row])
    #nums_points = [re.search(num, txt[row]).span(0) for num in nums]
    #syms = re.findall(r'[^\d\.]+', txt[row])
    #syms_points = [re.search(re.escape(sym), txt[row].span(0)) for sym in syms]

    #Every number is a span of points in the x direction
    #I need to check all digits within each number
    nums = [m[0] for m in re.finditer(r'\d+', txt[row])]
    nums_span = [m.span(0) for m in re.finditer(r'\d+', txt[row])]
    digits_span = [list(range(s[0], s[1])) for s in nums_span]
    
    #Every symbol is a single point
    syms = [m[0] for m in re.finditer(r'[^\d\.]+', txt[row])]
    syms_span = [m.span(0) for m in re.finditer(r'[^\d\.]+', txt[row])]
    syms_points = [(row, s[0]) for s in syms_span]
    if row > 0:
        syms_prior = [m[0] for m in re.finditer(r'[^\d\.]+', txt[row-1])]
        syms = syms + syms_prior
        syms_span = [m.span(0) for m in re.finditer(r'[^\d\.]+', txt[row-1])]
        syms_points = syms_points + [(row-1, s[0]) for s in syms_span]
    if row < len(txt)-1:
        syms_after = [m[0] for m in re.finditer(r'[^\d\.]+', txt[row+1])]
        syms = syms + syms_after
        syms_span = [m.span(0) for m in re.finditer(r'[^\d\.]+', txt[row+1])]
        syms_points = syms_points + [(row+1, s[0]) for s in syms_span]
    for num_idx in range(len(nums)):
        #I need a flag to break out multiple loops?
        found = False
        num_cur = nums[num_idx]
        digits = digits_span[num_idx]
        for digit in digits:
            digit_point = (row, digit)
            for sym_idx in range(len(syms)):
                sym_point = syms_points[sym_idx]
                if math.dist(digit_point, sym_point) <= math.sqrt(2):
                    print(f'number={num_cur}')
                    print(f'distance={math.dist(digit_point, sym_point)}')
                    print(f'symbol={syms[sym_idx]}')
                    print(f'symbol location={sym_point}\n')
                    parts.append(num_cur)
                    found = True
                    break
            if found==True:
                #don't check other digits for same number
                break


len(parts)
sum(int(p) for p in parts)

#same but neater - no flag
parts = []
for row in range(len(txt)):
    #Every number is a span of points in the x direction
    #I need to check all digits within each number
    nums = [m[0] for m in re.finditer(r'\d+', txt[row])]
    nums_span = [m.span(0) for m in re.finditer(r'\d+', txt[row])]
    digits_span = [list(range(s[0], s[1])) for s in nums_span]
    
    #Every symbol is a single point
    syms = [m[0] for m in re.finditer(r'[^\d\.]+', txt[row])]
    syms_span = [m.span(0) for m in re.finditer(r'[^\d\.]+', txt[row])]
    syms_points = [(row, s[0]) for s in syms_span]
    if row > 0:
        syms_prior = [m[0] for m in re.finditer(r'[^\d\.]+', txt[row-1])]
        syms = syms + syms_prior
        syms_span = [m.span(0) for m in re.finditer(r'[^\d\.]+', txt[row-1])]
        syms_points = syms_points + [(row-1, s[0]) for s in syms_span]
    if row < len(txt)-1:
        syms_after = [m[0] for m in re.finditer(r'[^\d\.]+', txt[row+1])]
        syms = syms + syms_after
        syms_span = [m.span(0) for m in re.finditer(r'[^\d\.]+', txt[row+1])]
        syms_points = syms_points + [(row+1, s[0]) for s in syms_span]
    for num_idx in range(len(nums)):
        num_cur = nums[num_idx]
        digits = digits_span[num_idx]
        for digit in digits:
            digit_point = (row, digit)
            for sym_idx in range(len(syms)):
                sym_point = syms_points[sym_idx]
                if math.dist(digit_point, sym_point) <= math.sqrt(2):
                    print(f'number={num_cur}')
                    print(f'distance={math.dist(digit_point, sym_point)}')
                    print(f'symbol={syms[sym_idx]}')
                    print(f'symbol location={sym_point}\n')
                    parts.append(num_cur)
                    break
            else:
                continue
            break
len(parts)
sum(int(p) for p in parts)

#Part 2
[m[0] for m in re.finditer(r'\*', txt[1])]

from collections import Counter

gear_count = Counter()
num_list = {}
for row in range(len(txt)):
    #Every number is a span of points in the x direction
    #I need to check all digits within each number
    nums = [m[0] for m in re.finditer(r'\d+', txt[row])]
    nums_span = [m.span(0) for m in re.finditer(r'\d+', txt[row])]
    digits_span = [list(range(s[0], s[1])) for s in nums_span]
    
    #Every symbol is a single point
    syms = [m[0] for m in re.finditer(r'\*', txt[row])]
    syms_span = [m.span(0) for m in re.finditer(r'\*', txt[row])]
    syms_points = [(row, s[0]) for s in syms_span]
    if row > 0:
        syms_prior = [m[0] for m in re.finditer(r'\*', txt[row-1])]
        syms = syms + syms_prior
        syms_span = [m.span(0) for m in re.finditer(r'\*', txt[row-1])]
        syms_points = syms_points + [(row-1, s[0]) for s in syms_span]
    if row < len(txt)-1:
        syms_after = [m[0] for m in re.finditer(r'\*', txt[row+1])]
        syms = syms + syms_after
        syms_span = [m.span(0) for m in re.finditer(r'\*', txt[row+1])]
        syms_points = syms_points + [(row+1, s[0]) for s in syms_span]
    for num_idx in range(len(nums)):
        num_cur = nums[num_idx]
        digits = digits_span[num_idx]
        for digit in digits:
            digit_point = (row, digit)
            for sym_idx in range(len(syms)):
                sym_point = syms_points[sym_idx]
                if math.dist(digit_point, sym_point) <= math.sqrt(2):
                    print(f'number={num_cur}')
                    print(f'symbol location={sym_point}\n')
                    gear_count[sym_point]+=1
                    if sym_point in num_list.keys():
                        num_list[sym_point] = num_list[sym_point] + [num_cur]
                    else:
                        num_list[sym_point] = [num_cur]
                    break
            else:
                continue
            break

gears_ok = []
for k,v in gear_count.items():
    if v==2:
        gears_ok.append(k)

gear_prod = []
for ok in gears_ok:
    gear_prod.append(int(num_list[ok][0]) * int(num_list[ok][1]))

print(sum(gear_prod))