#!/usr/bin/python3

from aoc import repres

file = open("../data/day16.txt", "rt")
data = [ x.strip() for x in file.read().strip().split('\n\n')]
file.close()

part2 = False

r = 0

my_ticket = [int(x) for x in data[1].split('\n')[1].split(',')]
tickets = [[int(y) for y in x.split(',')] for x in data[2].split('\n')[1:]]

names = []
ranges = []

for d in data[0].split('\n'):
	[n,rs] = d.split(': ')
	names.append(n)
	[r1, r2] = rs.split(' or ')
	[a,b] = r1.split('-')
	[c,d] = r2.split('-')
	ranges.append(((int(a),int(b)),(int(c),int(d))))

valid_tickets = []

for t in tickets:
	valid_ticket = True
	for f in t:
		invalid_field = True
		for ((a,b),(c,d)) in ranges:
			if a <= f <= b or c <= f <= d:
				invalid_field = False
				break
		if invalid_field:
			valid_ticket = False
			r += f
	if valid_ticket:
		valid_tickets.append(t)

repres(r, part2)

part2 = True

all_matches = [ set(range(len(ranges))) for i in range(len(ranges))]

for t in valid_tickets:
	matches = [set() for i in range(len(ranges))]
	for j, f in enumerate(t):
		for i, ((a,b),(c,d)) in enumerate(ranges):
			if a <= f <= b or c <= f <= d:
				matches[j] = matches[j] | {i}
	for i in range(len(all_matches)):
		all_matches[i] = all_matches[i] & matches[i]

while [x for x in all_matches if len(x) > 1] != []:
	single_pos = [i for i,x in enumerate(all_matches) if len(x) == 1]
	for sp in single_pos:
		for j in range(len(all_matches)):
			if j != sp:
				all_matches[j] = all_matches[j] - all_matches[sp]

r = 1

for i,x in enumerate(all_matches):
	for j in x:
		if "departure" in names[j]:
			r *= my_ticket[i]

repres(r, part2)
