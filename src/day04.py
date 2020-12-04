#!/usr/bin/python3

from aoc import repres, strcheck

file = open("../data/day04.txt", "rt")
data = [ x.replace('\n', ' ') for x in file.read().strip().split('\n\n') if x != '' ]
file.close()

r  = 0
part2 = True

required = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ] # , 'cid'

def check(key, value):
	if key == required[0]:
		y = int(value)
		return len(value) == 4 and y >= 1920 and y <= 2002
	elif key == required[1]:
		y = int(value)
		return len(value) == 4 and y >= 2010 and y <= 2020
	elif key == required[2]:
		y = int(value)
		return len(value) == 4 and y >= 2020 and y <= 2030
	elif key == required[3]:
		hs = value[:-2]
		h = int(hs) if hs != '' else 0
		u = value[-2:]
		return (u == 'cm' and h >= 150 and h <= 193) or (u == 'in' and h >= 59 and h <= 76)
	elif key == required[4]:
		return value[0] == '#' and strcheck(value[1:], '0123456789abcdef')
	elif key == required[5]:
		return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	elif key == required[6]:
		return len(value) == 9 and strcheck(value, '0123456789')
	else:
		return True

for d in data:
	keys = {}
	for field in d.split(' '):
		f = field.strip().split(':')
		keys[f[0]] = f[1]
		ok = 0
	for k in required:
		if k in keys.keys() and (not part2 or check(k, keys[k])):
			ok += 1
	if ok == len(required):
		r += 1

repres(r, part2)

