#!/usr/bin/python3

from aoc import repres
file = open("../data/day11.txt", "rt")
data = [ list(x) for x in file.read().strip().split('\n') ]
file.close()

part2 = True
r  = 0

xs = len(data[0])
ys = len(data)

dirs = [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (1, -1), (-1, 1), (1, 1)]

while True:
	neighbours = [[0] * xs for y in range(ys)]
	for y in range(ys):
		for x in range(xs):
			n = 0
			if data[y][x] == '.':
				continue
			for (dx, dy) in dirs:
				nx, ny = x, y
				while True:
					nx += dx
					ny += dy
					if 0 <= nx < xs and 0 <= ny < ys:
						if data[ny][nx] == '#':
							n += 1
							break
						elif data[ny][nx] == 'L':
							break
					else:
						break
					if not part2:
						break
			neighbours[y][x] = n
	still = True
	occupied = 0
	for y in range(ys):
		for x in range(xs):
			if data[y][x] == '.':
				continue
			if data[y][x] == 'L' and neighbours[y][x] == 0:
				data[y][x] = '#'
				still = False
			elif data[y][x] == '#' and neighbours[y][x] >= (5 if part2 else 4):
				data[y][x] = 'L'
				still = False
			if data[y][x] == '#':
				occupied += 1
	if still:
		r = occupied
		break

repres(r, part2)

