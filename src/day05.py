#!/usr/bin/python3

from aoc import repres

file = open("../data/day05.txt", "rt")
data = [x[::-1] for x in file.read().strip().replace('B','1').replace('F','0').replace('R','1').replace('L','0').split('\n')]
file.close()

part2 = True
r  = 0
allseats = []

for d in data:
	row = 0
	for i,b in enumerate(d[3:]):
		row += (2 ** i)*int(b)
	seat = 0
	for i,b in enumerate(d[:3]):
		seat += (2 ** i)*int(b)
	allseats.append(row*8 + seat)

allseats.sort()

if part2:
	for i in range(len(allseats)):
		nextseat = allseats[i] + 1
		if allseats[i+1] != nextseat:
			r = nextseat
			break
else:
	r = allseats[-1]

repres(r, part2)

