#!/usr/bin/python3

from aoc import repres

file = open("../data/day01.txt", "rt")
data = [int(x) for x in file.read().split('\n') if x != '']
file.close()

part2 = True
r = 0
l = len(data)

for i1 in range(l):
	d1 = data[i1]
	for i2 in range(i1+1, l):
		d2 = data[i2]
		if part2:
			for i3 in range(i2+1, l):
				d3 = data[i3]
				if d1 + d2 + d3 == 2020:
					r = d1 * d2 * d3
					i1 = i2 = i3 = l
		else:
			if d1 + d2 == 2020:
				r = d1 * d2
				i1 = i2 = l

repres(r, part2)
