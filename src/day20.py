#!/usr/bin/python3

from math import sqrt
from aoc import repres
from copy import deepcopy

file = open("../data/day20.txt", "rt")
data = [x.strip() for x in file.read().strip().split('\n\n')]
file.close()

part2 = False

def edges(tile):
	ts = len(tile)
	e1 = []
	e3 = []
	for y in range(ts):
		e1.append(tile[y][0])
		e3.append(tile[y][ts-1])
	e1 = "".join(e1)
	e3 = "".join(e3)
	e2 = tile[ts-1]
	e4 = tile[0]
	e1r = "".join([e for e in reversed(e1)])
	e2r = "".join([e for e in reversed(e2)])
	e3r = "".join([e for e in reversed(e3)])
	e4r = "".join([e for e in reversed(e4)])
	return [e1, e2, e3, e4, e1r, e2r, e3r, e4r]

def remove_border(tile):
	return [x[1:-1] for x in tile[1:-1]]

def fliph(tile):
	t = tile[:]
	for y in range(len(tile)):
		t[y] = tile[y][::-1]
	return t

def flipv(tile):
	return [x for x in reversed(tile)]

def rotate(tile):
	ts = len(tile)
	nt = []
	for x in range(ts):
		nr = []
		for y in range(ts):
			nr.append(tile[ts-y-1][x])
		nt.append("".join(nr))
	return nt

tiles = {}

for d in data:
	tile = d.split('\n')
	tile_id = int(tile[0][5:9])
	tile = tile[1:]
	tiles[tile_id] = tile

corners = []
matches = {}

positioned = [x for x in tiles.keys()][:1]
inx = 0

while inx < len(tiles):
	i = positioned[inx]
	t = tiles[i]
	matched = [0, 0, 0, 0]
	t_edges = edges(t)[:4]
	for j,ot in tiles.items():
		if j == i:
			continue
		for k, e in enumerate(t_edges):
			if e in edges(ot):
				mi = edges(ot).index(e)
				rotate_num = (mi - 2 - k) % 4
				hflip = (k < 2 and (mi == 1 or mi == 7)) or (k > 1 and (mi == 3 or mi == 5))
				vflip = (k < 2 and (mi == 0 or mi == 6)) or (k > 1 and (mi == 2 or mi == 4))
				assert j not in positioned or (rotate_num == 0 and not hflip and not vflip)
				if hflip:
					ot = fliph(ot)
				if vflip:
					ot = flipv(ot)
				for _ in range(rotate_num):
					ot = rotate(ot)
				tiles[j] = ot
				if not j in positioned:
					positioned.append(j)
				matched[k] = j
	if matched.count(0) == 2:
		corners.append(i)
	matches[i] = matched
	inx += 1

r = 1

for c in corners:
	r *= c
	matched = matches[c]
	if matched[0] == 0 and matched[3] == 0:
		next_tile = c

repres(r, part2)

part2 = True

for i,t in tiles.items():
	tiles[i] = remove_border(t)

x = y = 0
picture_size = int(sqrt(len(tiles)))*len(tiles[next_tile])
picture = [[' ']*picture_size for _ in range(picture_size)]

while len(tiles) > 0:
	t = tiles[next_tile]
	for yt in range(len(t)):
		for xt in range(len(t)):
			picture[y+yt][x+xt] = t[yt][xt]
	matched = matches[next_tile]
	del tiles[next_tile]
	if matched[0] == 0:
		next_down = matched[1]
	if matched[2] == 0:
		next_tile = next_down
		x = 0
		y += 8
	else:
		next_tile = matched[2]
		x += 8

monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

monster_x = len(monster[0])
monster_y = len(monster)

for tr in range(8):
	old_picture = deepcopy(picture)
	hflip = tr > 3
	rotate_num = tr % 4
	if hflip:
		picture = fliph(picture)
	for _ in range(rotate_num):
		picture = rotate(picture)

	monsters = 0
	for x in range(0, picture_size - monster_x):
		for y in range(0, picture_size - monster_y):
			monster_found = True
			for mx in range(monster_x):
				for my in range(monster_y):
					if monster[my][mx] == '#' and picture[y+my][x+mx] == '.':
						monster_found = False
			if monster_found:
				monsters += 1
				for mx in range(monster_x):
					for my in range(monster_y):
						if monster[my][mx] == '#':
							picture[y+my][x+mx] = 'O'
	if monsters > 0:
		r = sum([x.count('#') for x in picture])
		break
	picture = old_picture

repres(r, part2)
