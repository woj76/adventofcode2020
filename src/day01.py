#!/usr/bin/python3

from aoc import repres, loopbreak

file = open("../data/day01.txt", "rt")
data = [int(x) for x in file.read().split('\n') if x != '']
file.close()

part2 = True
r = 0
l = len(data)

try:
    for i1 in range(l):
        d1 = data[i1]
        for i2 in range(i1+1, l):
            d2 = data[i2]
            if part2:
                for i3 in range(i2+1, l):
                    d3 = data[i3]
                    if d1 + d2 + d3 == 2020:
                        r = d1 * d2 * d3
                        raise loopbreak()
            else:
                if d1 + d2 == 2020:
                    r = d1 * d2
                    raise loopbreak()
except loopbreak:
    pass

repres(r, part2)