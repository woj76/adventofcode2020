#!/usr/bin/python3

from aoc import repres

file = open("../data/day06.txt", "rt")
data = [x for x in file.read().strip().split('\n\n')]
file.close()

part2 = True
r  = 0
# one can use the string lib for this, but I want to 
# have it 'clean' ;)
alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]

for d in data:
	answers = d.split('\n')
	s = set(alphabet) if part2 else set()
	for a in answers:
		if part2:
			s &= set(a)
		else:
			s |= set(a)
	r += len(s)

repres(r, part2)

