start = [c == '.' for c in open('i18.txt').read().rstrip()]

trap_cond = {(False, False, True),
             (True, False, False),
             (False, True, True),
             (True, True, False)}

def advance(row):
    # pad with open tiles
    row = [True] + row + [True]
    return [tuple(row[i-1:i+2]) not in trap_cond for i in range(1, len(row) - 1)]

def solve(row, n):
    counter = 0
    for _ in range(n):
        counter += sum(row)
        row = advance(row)
    return counter

print('Part 1:', solve(start, 40))
print('Part 1:', solve(start, 400000))
