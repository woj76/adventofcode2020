import pyperclip

def repres(r, part2 = None):
    if part2 == None:
        print("Result: {}".format(r))
    else:
        print("Part {}: {}".format(2 if part2 else 1, r))
    pyperclip.copy(str(r))

#def tadd(t1, t2):
#    return tuple([sum(x) for x in zip(t1, t2)])

class loopbreak(Exception): pass