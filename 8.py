width = 50
height = 6
grid = [False] * width * height

for line in open('i8.txt'):
    line = line.strip()
    if line.startswith('rect'):
        x, y = map(int, line.split(' ')[1].split('x'))
        for a in range(y):
            for b in range(x):
                grid[width * a + b] = True
    elif line.startswith('rotate row'):
        i1, _, i2 = line.split(' ')[2:]
        y = int(i1[2:])
        amount = int(i2)
        row = grid[width * y:width * (y+1)]
        for n in range(width):
            grid[width * y + n] = row[(n - amount) % width]
    elif line.startswith('rotate column'):
        i1, _, i2 = line.split(' ')[2:]
        x = int(i1[2:])
        amount = int(i2)
        col = grid[x::width]
        for n in range(height):
            grid[width * n + x] = col[(n - amount) % height]

print('Part 1:', sum(grid))
print('Part 2:')
for row in range(height):
    print(''.join('#' if c else ' ' for c in grid[width * row:width * (row+1)]))
