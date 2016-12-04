import re

def is_valid_triangle(t):
    a,b,c = sorted(t)
    return a + b > c

def make_chunks(l, n):
    """Takes an iterable and breaks it up into chunks of length n.
    Example: make_chunks([1,2,3,4,5,6,7], 2) -> [[1,2], [3,4], [5,6], [7]]"""
    return [l[i:i+n] for i in range(0, len(l), n)]

triangles = [list(map(int, re.split(' +', l.strip()))) for l in open('i3.txt')]

print('Part 1:', sum(is_valid_triangle(t) for t in triangles))

triangles2 = make_chunks([ s for column in map(list, zip(*triangles)) for s in column ], 3)
print('Part 2:', sum(is_valid_triangle(t) for t in triangles2))
