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
maxid = allseats[-1]

if part2:
	for i in range(allseats[0]+1, maxid):
		if not i in allseats:
			r = i
			break
else:
	r = maxid

repres(r, part2)

