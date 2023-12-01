import re
import string

with open("day1.txt") as f:
    txt = f.read().splitlines()

len(txt)
[re.findall(r'\d', i) for i in txt[0:10]]

calibration = []
for i in range(len(txt)):
    m = re.findall(r'\d', txt[i])
    calibration.append(len(m))
min(calibration)
max(calibration)

calibration = []
for i in range(len(txt)):
    m = re.findall(r'\d', txt[i])
    if len(m)==1:
        calibration.append(int(m[0] + m[0]))
    else:
        calibration.append(int(m[0] + m[len(m)-1]))


print(sum(calibration))

#part 2
d = ['one', 'two', 'three']
map_obj = map(lambda x: re.findall(x, txt[18]), d)
for i in map_obj:
    print(i)
'|'.join(d)
pattern = '|'.join(d)
pattern = pattern + '|' + '|'.join(i for i in string.digits)

re.findall('|'.join(d), txt[18])
re.findall(pattern, txt[18])



num_map = dict(zip(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], 
                   [int(i) for i in string.digits]))
pattern = '|'.join(num_map.keys())
pattern = pattern + '|' + '|'.join(i for i in string.digits)
print(pattern)

calibration = []
for i in range(len(txt)):
    m = re.findall(pattern, txt[i])
    if len(m)==1:
        if m[0] in num_map.keys():
            digit = str(num_map[m[0]])
        else:
            digit = str(m[0])
        calibration.append(int(digit + digit))
    else:
        digit1 = m[0]
        digit2 = m[len(m)-1]
        if digit1 in num_map.keys():
            digit1 = str(num_map[digit1])
        if digit2 in num_map.keys():
            digit2 = str(num_map[digit2])
        calibration.append(int(digit1 + digit2))
print(sum(calibration))
calibration[20] #i'm not matching 'twone'


d = ['one', 'two', 'three']
re.findall('|'.join(d), txt[20])
txt[20].find('two')
txt[20].find('one')

[txt[20].find(i) for i in d]
[txt[20].rfind(i) for i in d]

[txt[i].find(i) for i in num_map.keys()]

calibration = []
for i in range(len(txt)):
    m = re.findall(pattern, txt[i])
    if len(m)==1:
        if m[0] in num_map.keys():
            digit = str(num_map[m[0]])
        else:
            digit = str(m[0])
        calibration.append(int(digit + digit))
    else:
        digit1 = m[0]
        last_find_word = [txt[i].rfind(j) for j in num_map.keys()]
        last_find_num = [txt[i].rfind(str(j)) for j in num_map.values()]
        #m = re.findall(pattern, ''.join(reversed(txt[i])))
        if max(last_find_word) > 0 and max(last_find_word) == max(last_find_word + last_find_num):
            m = re.findall(pattern, txt[i][max(last_find_word):])
        if max(last_find_num) > 0 and max(last_find_num) == max(last_find_word + last_find_num):
            m = re.findall(pattern, txt[i][max(last_find_num):])
        digit2 = m[0]
        if digit1 in num_map.keys():
            digit1 = str(num_map[digit1])
        if digit2 in num_map.keys():
            digit2 = str(num_map[digit2])
        calibration.append(int(digit1 + digit2))
print(sum(calibration))
calibration[20] #now this works


