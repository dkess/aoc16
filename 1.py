visited = set()

x = 0
y = 0

p2x = None
p2y = None

# 0: north
# 1: east
# 2: south
# 3: west
d = 0

finished_part2 = False

for instr in open('i1.txt').read().strip().split(', '):
    if instr[0] == 'L':
        d = (d - 1) % 4
    elif instr[0] == 'R':
        d = (d + 1) % 4
    else:
        print('bad input')

    amount = int(instr[1:])
    for _ in range(amount):
        if d == 0:
            y += 1
        elif d == 1:
            x += 1
        elif d == 2:
            y -= 1
        else:
            x -= 1

        if not finished_part2 and (x, y) in visited:
            p2x = x
            p2y = y
            finished_part2 = True
        visited.add((x, y))

print('Part 1:', abs(x) + abs(y))
print('Part 2:', abs(p2x) + abs(p2y))
