def bounded(mi, x, ma):
    if x < mi:
        return mi
    elif x > ma:
        return ma
    else:
        return x

with open('i2.txt') as f:
    instr = [l.strip() for l in f]

x = 1
y = 1

num = ''

for l in instr:
    for c in l:
        if c == 'U':
            y = bounded(0, y-1, 2)
        elif c == 'D':
            y = bounded(0, y+1, 2)
        elif c == 'L':
            x = bounded(0, x-1, 2)
        elif c == 'R':
            x = bounded(0, x+1, 2)
        else:
            print('error: bad input')

    num += str(y*3 + x + 1)

print(num)
