#!/usr/bin/python3

from aoc import repres

file = open("../data/day03.txt", "rt")
data = [x for x in file.read().split('\n') if x != '']
file.close()

part2 = True

r  = 1
ly = len(data)
lx = len(data[0])

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] if part2 else [(3, 1)]

for dx, dy in slopes:
	x = y = trees = 0
	while y < ly:
		if data[y][x] == '#':
			trees += 1
		x += dx
		x %= lx
		y += dy
	r *= trees
    
repres(r, part2)

