import re

regex = re.compile(
    r'Disc .+ has (\d+) positions\; at time\=0\, it is at position (\d+)\.')

discs = [tuple(map(int, regex.search(l).groups())) for l in open('i15.txt')]

def solve(discs):
    t = 0
    while True:
        states = [(i + t + n + 1) % m for n, (m, i) in enumerate(discs)]
        if states == [0] * len(discs):
            return t
        t += 1

print('Part 1:', solve(discs))
print('Part 2:', solve(discs + [(11, 0)]))
