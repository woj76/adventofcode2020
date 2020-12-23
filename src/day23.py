#!/snap/bin/pypy3

from aoc import repres

input = "925176834"

part2 = True

l = 1000000 if part2 else 9

class Cup:
	def __init__(self, v):
		self.val = v
		self.prev = self
		self.next = self
	def append(self,v):
		node = Cup(v)
		node.prev = self.prev
		self.prev.next = node
		node.next = self
		self.prev = node
		return node
	def move_three(self, dest):
		after_dest = dest.next
		t1 = self.next
		t3 = t1.next.next
		after_self = t3.next
		dest.next = t1
		t1.prev = dest
		t3.next = after_dest
		after_dest.prev = t3
		self.next = after_self
		after_self.prev = self

node_refs = [0] * 9

current_cup = None
for v in [int(x) for x in input]:
	if current_cup == None:
		current_cup = Cup(v)
		node_refs[v-1] = current_cup
	else:
		current_cup.append(v)
		node_refs[v-1] = current_cup.prev

for i in range(10, l+1):
	current_cup.append(i)
	node_refs.append(current_cup.prev)

for _ in range(10000000 if part2 else 100):
	take_outs = [current_cup.next.val, current_cup.next.next.val, current_cup.next.next.next.val]

	dest_cup = current_cup.val - 1
	if dest_cup == 0:
		dest_cup = l
	while dest_cup in take_outs:
		dest_cup -= 1
		if dest_cup == 0:
			dest_cup = l

	dest_node = node_refs[dest_cup-1]
	current_cup.move_three(dest_node)

	current_cup = current_cup.next

node = node_refs[0].next

if part2:
	r = node.val * node.next.val
else:
	r = ""
	for i in range(8):
		r += str(node.val)
		node = node.next

repres(r, part2)
