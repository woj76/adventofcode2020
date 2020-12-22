#!/snap/bin/pypy3

from aoc import repres

file = open("../data/day22.txt", "rt")
data = [x.strip() for x in file.read().strip().split('\n\n')]
file.close()

part2 = True
r = 0

[player1, player2] = [d.split('\n') for d in data]
player1 = [int(x) for x in player1[1:]]
player2 = [int(x) for x in player2[1:]]

def play(deck1, deck2):
	reps1 = []
	reps2 = []
	while deck1 != [] and deck2 != []:
		if part2:
			if deck1 in reps1 and deck2 in reps2:
				return 1, deck1
			reps1.append(deck1)
			reps2.append(deck2)
		p1,p2 = deck1[0], deck2[0]
		deck1 = deck1[1:]
		deck2 = deck2[1:]
		if part2 and len(deck1) >= p1 and len(deck2) >= p2:
			wn, _ = play(deck1[:p1], deck2[:p2])
		else:
			wn = 1 if p1 > p2 else 2
		if wn == 1:
			deck1.append(p1)
			deck1.append(p2)
		else:
			deck2.append(p2)
			deck2.append(p1)
	return wn, deck1 if wn ==1 else deck2

wn, wd = play(player1, player2)

for i,v in enumerate(reversed(wd)):
	r += (i+1)*v

repres(r, part2)
