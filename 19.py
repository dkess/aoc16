import math

INPUT = 3012210

x = int(math.log(INPUT, 2))
print('Part 1:', (INPUT - (2 ** x)) * 2 + 1)

# Is there a more elegant way to represent this pattern?  Maybe, but this is
# the best I could do.
def solve2(n):
    groupstart = 2
    c = 0
    for i in range(3, n + 1):
        if c >= groupstart - 2:
            c += 2
            if c == i:
                groupstart = c
                c = 0
        else:
            c += 1
    return c + 1

print('Part 2:', solve2(INPUT))
