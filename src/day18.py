#!/usr/bin/python3

from aoc import repres

file = open("../data/day18.txt", "rt")
data = [ x for x in file.read().strip().split('\n')]
file.close()

part2 = True

r = 0

def eval(e, index):
	if len(e) - index == 1:
		return e[index]
	e1 = e[index]
	op = e[index + 1]
	e2 = e[index + 2]
	if isinstance(e1, list):
		e1 = eval(e1, 0)
		e[index] = e1
	if isinstance(e2, list):
		e2 = eval(e2, 0)
		e[index + 2] = e2
	if op == '+':
		er = e1 + e2
		del e[index:index + 2]
		e[index] = er
		return eval(e, 0)
	else:
		if len(e) - index == 3 or not part2:
			er = e1 * e2
			del e[index:index + 2]
			e[index] = er
			return eval(e, 0)
		else:
			return eval(e, index + 2)

for d in data:
	l = []
	stack = []
	for c in d:
		if c == ' ':
			continue
		elif c == '(':
			stack.append(l)
			l = []
		elif c == ')':
			t = l
			l = stack.pop()
			l.append(t)
		elif c == '*' or c == '+':
			l.append(c)
		else:
			l.append(int(c))
	r += eval(l,0)

repres(r, part2)
