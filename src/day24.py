#!/snap/bin/pypy3

from aoc import repres

file = open("../data/day24.txt", "rt")
data = [x for x in file.read().strip().split('\n') ]
file.close()

part2 = True
r = 0

tile_grid = {}

for x in range(-70,70):
	for y in range(-70,70):
		tile_grid[(x,y)] = False

def get_tile(g, x, y):
	if not (x,y) in g.keys():
		return False
	return g[(x,y)]

def neighbours(x, y):
	ret = [(x+1,y), (x-1, y), (x, y-1), (x, y+1)]
	if y % 2 == 0:
		ret.append((x-1,y-1))
		ret.append((x-1,y+1))
	else:
		ret.append((x+1,y-1))
		ret.append((x+1,y+1))
	return ret

for d in data:
	x = y = 0
	i = 0
	l = len(d)
	while i < l:
		if d[i] == 'e':
			x += 1
		elif d[i] == 'w':
			x -= 1
		else:
			ns = d[i]
			i += 1
			we = d[i]
			if we == 'w' and y % 2 == 0:
				x -= 1
			elif we == 'e' and y % 2 == 1:
				x += 1
			if ns == 'n':
				y -= 1
			else:
				y += 1
		i += 1
	tile_grid[(x,y)] = not tile_grid[(x,y)]

if part2:
	for _ in range(100):
		black_counts = {}
		for (x,y) in tile_grid.keys():
			black_counts[(x,y)] = sum([1 for (xn,yn) in neighbours(x,y) if get_tile(tile_grid, xn, yn)])
		for (x,y) in tile_grid.keys():
			black = tile_grid[(x,y)]
			bn = black_counts[(x,y)]
			if black and (bn == 0 or bn > 2):
				tile_grid[(x,y)] = not tile_grid[(x,y)]
			elif not black and bn == 2:
				tile_grid[(x,y)] = not tile_grid[(x,y)]


r = len([x for x in tile_grid.values() if x])

repres(r, part2)
