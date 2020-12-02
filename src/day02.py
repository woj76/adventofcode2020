#!/usr/bin/python3

from aoc import repres

file = open("../data/day02.txt", "rt")
data = [x for x in file.read().split('\n') if x != '']
file.close()

part2 = True

r = 0

for d in data:
    pwline = d.split(' ')
    password = pwline[2]
    letter = pwline[1][0]
    bounds = [int(x) for x in pwline[0].split('-')]
    if part2:
        letter1 = password[bounds[0]-1]
        letter2 = password[bounds[1]-1]
        if (letter1 == letter) ^ (letter2 == letter):
            r += 1
    else:
        occurences = password.count(letter)
        if occurences >= bounds[0] and occurences <= bounds[1]:
            r += 1

repres(r, part2)

