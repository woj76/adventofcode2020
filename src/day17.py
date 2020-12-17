#!/usr/bin/python3

from aoc import repres


file = open("../data/day17.txt", "rt")
data = [ x for x in file.read().strip().split('\n')]
file.close()

part2 = True

grid = {}

x = y = z = w = 0
x_min = y_min = z_min = -1

x_max = len(data[0]) + 1
z_max = 2
w_min = -1 if part2 else 0
w_max = 2 if part2 else 1

for d in data:
	x = 0
	for c in d:
		if c == '#':
			grid[(x,y,z,w)] = 1
		x += 1
	y += 1

y_max = y + 1

for _ in range(6):
	cube = [(x,y,z,w) for x in range(x_min,x_max) for y in range(y_min,y_max) for z in range(z_min, z_max) for w in range(w_min,w_max)]
	neighbors = {}
	for x,y,z,w in cube:
		cords = [(x1,y1,z1,w1) for x1 in [x-1,x,x+1] for y1 in [y-1,y,y+1] for z1 in [z-1,z,z+1] for w1 in [w-1,w,w+1] if x1 != x or y1 != y or z1 != z or w1 != w]
		neighbors[(x,y,z,w)] = 0
		for c in cords:
			if c in grid.keys():
				neighbors[(x,y,z,w)] += 1
	for x,y,z,w in cube:
		n = neighbors[(x,y,z,w)]
		if (x,y,z,w) in grid.keys():
			if n < 2 or n > 3:
				del grid[(x,y,z,w)]
		else:
			if n == 3:
				grid[(x,y,z,w)] = 1
	x_min -= 1
	x_max += 1
	y_min -= 1
	y_max += 1
	z_min -= 1
	z_max += 1
	if part2:
		w_min -= 1
		w_max += 1

repres(sum(grid.values()), part2)
