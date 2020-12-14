#!/usr/bin/python3

from aoc import repres

file = open("../data/day14.txt", "rt")
data = [ x for x in file.read().strip().split('\n') ]
file.close()

part2 = True

mem = {}
mask = ''

def mask_part1(m, v):
	v |= int(m.replace('X', '0'), 2)
	v &= int(m.replace('X', '1'), 2)
	return v

for d in data:
	if d[:4] == "mask":
		mask = d[7:]
	else:
		d = d[4:]
		[a, v] = [int(x) for x in d.split('] = ')]
		if part2:
			a = mask_part1(mask.replace('0', 'X'), a)
			tmask = mask.replace('X', 'Y').replace('1', 'X').replace('0', 'X')
			n = tmask.count('Y') + 1
			for i in range(2 ** n):
				bits = format(i, 'b').zfill(n)
				s = tmask[:]
				for b in bits:
					s = s.replace('Y', b, 1)
				mem[mask_part1(s, a)] = v
		else:
			mem[a] = mask_part1(mask, v)

r  = 0

for k in mem.keys():
	r += mem[k]

repres(r, part2)


