#!/usr/bin/python3

from aoc import repres

file = open("../data/day05.txt", "rt")
data = [int("0b" + x, 2) for x in file.read().strip().replace('B','1').replace('F','0').replace('R','1').replace('L','0').split('\n')]
file.close()

part2 = True
r  = 0

data.sort()

if part2:
	for i in range(len(data)):
		nextseat = data[i] + 1
		if data[i+1] != nextseat:
			r = nextseat
			break
else:
	r = data[-1]

repres(r, part2)

