#!/usr/bin/python3

from aoc import repres

file = open("../data/day05.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = True
r  = 0
allseats = []

for d in data:
	rowstr = d[-4::-1]
	row = 0
	for i,b in enumerate(rowstr):
		bv = 1 if b == 'B' else 0
		row += (2 ** i)*bv
	seatstr = d[:-4:-1]
	seat = 0
	for i,b in enumerate(seatstr):
		bv = 1 if b == 'R' else 0
		seat += (2 ** i)*bv
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

