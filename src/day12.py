#!/usr/bin/python3

from aoc import repres

file = open("../data/day12.txt", "rt")
data = [ x for x in file.read().strip().split('\n') ]
file.close()

part2 = True
r  = 0

x = y = 0
wx,wy = (10,1) if part2 else (1,0)

for d in data:
	dir = d[0]
	steps = int(d[1:])
	if dir in "NSWE":
		dx = dy = 0
		if dir == 'N':
			dy = steps
		elif dir == 'S':
			dy = -steps
		elif dir == 'E':
			dx = steps
		elif dir == 'W':
			dx = -steps
		if part2:
			wx, wy = wx+dx, wy+dy
		else:
			x, y = x+dx, y+dy
	elif dir == 'F':
		x, y = x + steps*wx, y + steps*wy
	else:
		n = steps // 90
		if dir == 'L':
			n = -n
		for i in range(n % 4):
			t = wx
			wx = wy
			wy = -t

r = abs(x) + abs(y)

repres(r, part2)

