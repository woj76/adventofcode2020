#!/usr/bin/python3

from aoc import repres

file = open("../data/day10.txt", "rt")
data = [ int(x) for x in file.read().strip().split('\n')]
file.close()

part2 = True

r  = 0

data.sort()
data.append(data[-1]+3)

last = diff1 = diff1s = diff3 = 0
combos = 1

for d in data:
	gap = d - last
	if  gap == 1:
		diff1 += 1
		if part2:
			diff1s += 1
	elif gap == 3:
		diff3 += 1
		if part2:
			s = 1 if diff1s < 2 else 2 if diff1s == 2 else 4 if diff1s == 3 else 7
			diff1s = 0
			combos *= s
	last = d

if part2:
    r = combos
else:
    r = diff1 * diff3

repres(r, part2)

