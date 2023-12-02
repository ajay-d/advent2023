import re
import string

with open("day2.txt") as f:
    txt = f.read().splitlines()

len(txt)
txt[0].split(':')
txt[0].split(':')[1].split(';')
txt[0].split(':')[1].split(';')[0].split(',')
txt[0].split(':')[1].split(';')[0].split(',')[0].split()

impossible_games = []
for i in range(len(txt)):
    games = txt[i].split(':')[1].split(';')
    for game in games:
        cubes = game.split(',')
        for cube in cubes:
            if cube.find('red') > 0:
                if int(re.findall(r'\d+', cube)[0]) > 12:
                    impossible_games.append(i)
            if cube.find('green') > 0:
                if int(re.findall(r'\d+', cube)[0]) > 13:
                    impossible_games.append(i)
            if cube.find('blue') > 0:
                if int(re.findall(r'\d+', cube)[0]) > 14:
                    impossible_games.append(i)

impossible_games
set(impossible_games)
set(range(len(txt)))
valid_games = set(range(len(txt))).difference(set(impossible_games))
#counting starts at 1
sum({i+1 for i in valid_games})

#part 2
power_prod = []
for i in range(len(txt)):
    games = txt[i].split(':')[1].split(';')
    red, blue, green = 0, 0, 0
    for game in games:
        cubes = game.split(',')
        for cube in cubes:
            if cube.find('red') > 0:
                red_i = int(re.findall(r'\d+', cube)[0])
                if red_i > red:
                    red = red_i
            if cube.find('green') > 0:
                green_i = int(re.findall(r'\d+', cube)[0])
                if green_i > green:
                    green = green_i
            if cube.find('blue') > 0:
                blue_i = int(re.findall(r'\d+', cube)[0])
                if blue_i > blue:
                    blue = blue_i
    power = red * blue * green
    power_prod.append(power)
print(sum(power_prod))