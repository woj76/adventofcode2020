#!/snap/bin/pypy3

from aoc import repres

file = open("../data/day25.txt", "rt")
pub_keys = [int(x) for x in file.read().strip().split('\n') ]
file.close()

g = 7
m = 20201227

k = 1
while True:
	if pub_keys[1] == pow(g, k, m):
		break
	k += 1

repres(pow(pub_keys[0], k, m), False)
