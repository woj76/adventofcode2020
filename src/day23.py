#!/snap/bin/pypy3

from aoc import repres

input = "925176834"

part2 = True

total_cups = 1000000 if part2 else 9

class Cup:
	def __init__(self, v):
		self.val = v
		self.next = self
		self.prev = self
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
	def last_node(self):
		return self.prev
	def next_node(self):
		return self.next
	def get_value(self):
		return self.val

node_refs = [0] * 9

current_cup = None
for v in [int(x) for x in input]:
	if current_cup == None:
		current_cup = Cup(v)
		node_refs[v-1] = current_cup
	else:
		current_cup.append(v)
		node_refs[v-1] = current_cup.last_node()

for i in range(10, total_cups+1):
	current_cup.append(i)
	node_refs.append(current_cup.last_node())

for _ in range(10000000 if part2 else 100):
	node = current_cup.next_node()
	take_outs = []
	for _ in range(3):
		take_outs.append(node.get_value())
		node = node.next_node()

	dest_cup = current_cup.get_value()

	while dest_cup == current_cup.get_value() or dest_cup in take_outs:
		dest_cup -= 1
		if dest_cup == 0:
			dest_cup = total_cups

	dest_node = node_refs[dest_cup-1]
	current_cup.move_three(dest_node)

	current_cup = current_cup.next_node()

node = node_refs[0].next_node()

if part2:
	r = node.get_value() * node.next_node().get_value()
else:
	r = ""
	for i in range(total_cups-1):
		r += str(node.get_value())
		node = node.next_node()

repres(r, part2)
