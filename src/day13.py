#!/usr/bin/python3

from aoc import repres

file = open("../data/day13.txt", "rt")
timestamp = int(file.readline().strip())
buses = [(int(x) if x != 'x' else 0) for x in file.readline().strip().split(',')]
file.close()

minutes = []

for b in buses:
	if b > 0:
		minutes.append(b - timestamp % b)
	else:
		minutes.append(float('inf'))

wait = min(minutes)

repres(wait * buses[minutes.index(wait)], False)

# Chinese Reminder Theorem, the reminders were a bit tricky to figure out

crt = []

for i, b in enumerate(buses):
	if b > 0:
		crt.append((b, (b - i) % b))

n, x = crt[0]

for nx, ax in crt[1:]:
	while True:
		x += n
		if x % nx == ax:
			break
	n *= nx

repres(x, True)

