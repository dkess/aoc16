import hashlib

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

INPUT = 'rrrbmfta'
#INPUT = 'ihgpwlah'

DIRS = [('U', 0, -1),
        ('D', 0, 1),
        ('L', -1, 0),
        ('R', 1, 0)]
OPEN = set('bcdef')

start = (0, 0)
goal = (3, 3)

# BFS
frontier = [(start, '')]

while frontier:
    current, path = frontier.pop(0)
    
    if current == goal:
        break

    cx, cy = current

    opendoors = md5(INPUT + path)[:4]

    for n, (d, dx, dy) in enumerate(DIRS):
        nx, ny = cx + dx, cy + dy
        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue

        if opendoors[n] not in OPEN:
            continue

        frontier.append(((nx, ny), path + d))

print('Part 1:', path)

# DFS
frontier = [(start, '')]
longpath = 0

while frontier:
    current, path = frontier.pop()
    
    if current == goal:
        if len(path) > longpath:
            longpath = len(path)
        continue

    cx, cy = current

    opendoors = md5(INPUT + path)[:4]

    for n, (d, dx, dy) in enumerate(DIRS):
        nx, ny = cx + dx, cy + dy
        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue

        if opendoors[n] not in OPEN:
            continue

        frontier.append(((nx, ny), path + d))

print('Part 2:', longpath)
