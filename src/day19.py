#!/usr/bin/python3

from aoc import repres

file = open("../data/day19.txt", "rt")
[rules, strings] = [x.strip() for x in file.read().strip().split('\n\n')]
file.close()

part2 = True

grammar = {}

for l in rules.split('\n'):
	[a, b] = l.split(': ')
	if b[0] == '\"':
		grammar[a] = b[1]
	else:
		prods = [x.split(' ') for x in b.split(' | ')]
		if part2 and a == "11":
			[x,y] = prods[0]
			for i in range(2, 6):
				t1 = [x] * i
				t1.extend([y] * i)
				prods.append(t1)
		grammar[a] = prods

def match(s, index, rule, rep8):
	if index >= len(s):
		return -1
	first = grammar[rule][0]
	if len(grammar[rule]) == 1 and isinstance(first, str):
		return (index + 1) if first == s[index] else -1
	gr = grammar[rule]
	if part2 and rule == "8":
		gr = [[gr[0][0]] * rep8]
	for rs in gr:
		index1 = index
		for rl in rs:
				index1 = match(s, index1, rl, rep8)
				if index1 == -1:
					break
		if index1 >= 0:
			return index1
	return -1

r = 0

for s in strings.split('\n'):
	for rep8 in range(1, 6 if part2 else 2):
		m = match(s, 0, "0", rep8) == len(s)
		if m:
			break
	if m:
		r += 1

repres(r, part2)
