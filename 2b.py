keys = {  ( 0, -2): '1'
        , (-1, -1): '2'
        , ( 0, -1): '3'
        , ( 1, -1): '4'
        , (-2,  0): '5'
        , (-1,  0): '6'
        , ( 0,  0): '7'
        , ( 1,  0): '8'
        , ( 2,  0): '9'
        , (-1,  1): 'A'
        , ( 0,  1): 'B'
        , ( 1,  1): 'C'
        , ( 0,  2): 'D'
        }

with open('i2.txt') as f:
    instr = [l.strip() for l in f]

x = -2
y = 0

code = ''

for l in instr:
    for c in l:
        a = x
        b = y
        if c == 'U':
            b -= 1
        elif c == 'D':
            b += 1
        elif c == 'L':
            a -= 1
        elif c == 'R':
            a += 1
        else:
            print('error: bad input')
        
        if (a,b) in keys:
            x = a
            y = b

    code += keys[(x,y)]

print(code)
