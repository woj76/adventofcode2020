#!/usr/bin/python3

from aoc import repres

file = open("../data/day07.txt", "rt")
data = [ x for x in file.read().strip().replace(" bags", "").replace(" bag", "").split('\n') ]
file.close()

part2 = True
r  = 0

bag_deps = {}

for d in data:
	dep = d.split(" contain ")
	l = [x.strip() for x in dep[1][:-1].split(',')]
	bag_deps[dep[0].strip()] = [(x[2:], int(x[:1])) for x in l if x != "no other"]

my_bag = 'shiny gold'

## Imperative / BFS version for part 1
#for k in bag_deps.keys():
#	i = 0
#	l = [x[0] for x in bag_deps[k]]
#	while i < len(l):
#		bag = l[i]
#		for b in [x[0] for x in bag_deps[bag] if not x[0] in l]:
#			l.append(b)
#		i += 1
#	if my_bag in l:
#		r += 1
#
#repres(r)

def find_bags(bag):
	if not part2 and bag == my_bag:
		return 1
	res = 0
	for b,n in bag_deps[bag]:
		if part2:
			res += n * (find_bags(b)+1)
		else:
			res = find_bags(b)
			if res == 1:
				break
	return res

if part2:
	r = find_bags(my_bag)
else:
	r = sum([find_bags(k) for k in bag_deps.keys() if k != my_bag])

repres(r, part2)
