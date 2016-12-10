from collections import defaultdict
import re

bots = defaultdict(list)
instr = {}
outputs = defaultdict(list)

def bot_give(b):
    if len(bots[b]) == 2 and b in instr:
        lo, low_r, ho, high_r = instr[b]
        low, high = sorted(bots[b])
        if low == 17 and high == 61:
            print('Part 1:', b)
        bots[b] = []
        if lo:
            outputs[low_r].append(low)
        else:
            bots[low_r].append(low)
            bot_give(low_r)
        if ho:
            outputs[high_r].append(high)
        else:
            bots[high_r].append(high)
            bot_give(high_r)

goesto = re.compile(r'value (\d+) goes to bot (\d+)')
gives = re.compile(r'bot (\d+) gives low to ([^ ]+) (\d+) and high to ([^ ]+) (\d+)')

for l in open('i10.txt'):
    l = l.strip()
    m = goesto.match(l)
    if m:
        val, b = map(int, m.groups())
        bots[b].append(val)
        bot_give(b)
    else:
        m = gives.match(l)
        b = int(m.group(1))
        lo = m.group(2) == 'output'
        low_r = int(m.group(3))
        ho = m.group(4) == 'output'
        high_r = int(m.group(5))
        instr[b] = (lo, low_r, ho, high_r)
        bot_give(b)

print('Part 2:', outputs[0][0] * outputs[1][0] * outputs[2][0])
