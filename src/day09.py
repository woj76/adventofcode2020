#!/usr/bin/python3

from aoc import repres

file = open("../data/day09.txt", "rt")
data = [ int(x) for x in file.read().strip().split('\n')]
file.close()

part2 = True
r  = 0
l = len(data)

for i in range(25, l):
	v = data[i]
	sdata = data[:i]
	sums = [ True for x in sdata for y in sdata if x != y and x + y == v]
	if len(sums) == 0:
		r = v
		break

if part2:
	for i in range(0, l-1):
		for j in range(i+1, l):
			sdata = data[i:j+1]
			if sum(sdata) == r:
				r = min(sdata) + max(sdata)
				i, j = l-1, l # outer break

repres(r, part2)

