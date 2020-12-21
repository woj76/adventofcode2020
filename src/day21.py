#!/usr/bin/python3

from aoc import repres
file = open("../data/day21.txt", "rt")
data = [x.strip() for x in file.read().strip().split('\n')]
file.close()

part2 = False

foods = []
ingredients = set()
allergens = set()

for d in data:
	[ingrs, allers] = d.split(' (')
	allers = [x.strip() for x in allers[9:-1].split(', ')]
	ingrs = [x.strip() for x in ingrs.split(' ')]
	ingredients |= set(ingrs)
	allergens |= set(allers)
	foods.append((ingrs,allers))

neutrals = ingredients.copy()

for ings, als in foods:
	i = set(ings)
	for a in als:
		for ings1, als1 in foods:
			if a in als1:
				i &= set(ings1)
		neutrals -= i

r = sum([len([x for x in ings if x in neutrals]) for ings, als in foods])

repres(r, False)

ai = {}

for a in allergens:
	allergic_ingredients = ingredients - neutrals
	for ings, als in foods:
		if a in als:
			allergic_ingredients &= set(ings)
	ai[a] = list(allergic_ingredients)

unresolved = True

while unresolved:
	unresolved = False
	for a, ais in ai.items():
		if len(ais) == 1:
			for a1 in ai.keys():
				if a != a1 and ais[0] in ai[a1]:
					ai[a1].remove(ais[0])
		else:
			unresolved = True

r = ",".join([b for a, b in sorted([(x,y[0]) for x,y in ai.items()])])

repres(r, True)
