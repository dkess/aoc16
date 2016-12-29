import heapq
from itertools import combinations, permutations
import re

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

lines = open('i22.txt').readlines()[2:]

data = [(int(a[:-1]), int(b[:-1]), int(c[:-1])) for _, a, b, c in
        (l.strip().split()[:4] for l in lines)]

width, height = re.search(r'x(\d+)\-y(\d+)', lines[-1]).groups()
width = int(width) + 1
height = int(height) + 1

def can_copy(a, b):
    """True if a,b are viable"""
    return a[1] and a[1] < b[2]

print('Part 1:', sum(can_copy(a, b) for a, b in permutations(data, 2)))

