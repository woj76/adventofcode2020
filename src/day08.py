#!/usr/bin/python3

from aoc import repres

file = open("../data/day08.txt", "rt")
data = [ (x[:3], int(x[4:])) for x in file.read().strip().split('\n')]
file.close()

part2 = True
r  = 0
last_line = len(data)

if part2: 
	flips = [i for i, (ins, _) in enumerate(data) if ins == 'nop' or ins == 'jmp']
else:
	flips = [-1]

for f in flips:
	acc = line = 0
	lines = []
	while True:
		lines.append(line)
		ins, param = data[line]
		if ins == 'acc':
			acc += param
		elif part2 and line == f:
			if ins == 'nop':
				ins = 'jmp'
			else:
				ins = 'nop'
		line += (param if ins == 'jmp' else 1)
		if (part2 and line == last_line) or line in lines:
			r = acc
			break
	if line == last_line:
		break

repres(r, part2)

