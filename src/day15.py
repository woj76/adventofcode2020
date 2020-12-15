#!/usr/bin/python3

from aoc import repres

data = [9,19,1,6,0,5,4]

part2 = True

turn = 1
spoken = {}

for d in data[:-1]:
	spoken[d] = turn
	turn += 1

tosay = data[-1]

while turn < (30000000 if part2 else 2020):
	if not tosay in spoken.keys():
		spoken[tosay] = turn
		tosay = 0
	else:
		lastsaid = spoken[tosay]
		spoken[tosay] = turn
		tosay = turn - lastsaid
	turn += 1

repres(tosay, part2)


