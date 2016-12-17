import heapq

INPUT = 1350
tx, ty = 31, 39

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def map_pos(x, y):
    """Returns True if wall"""
    if x < 0 or y < 0:
        return True
    z = x*x + 3*x + 2*x*y + y + y*y + INPUT
    return sum(c == '1' for c in '{0:b}'.format(z)) % 2

start = (1, 1)
goal = (tx, ty)

# a star
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
    current = frontier.get()
    cx, cy = current

    if current == goal:
        break

    new_cost = cost_so_far[current] + 1
    for nextnode in ((nx, ny)
                     for (nx, ny) in [(cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)]
                     if not map_pos(nx, ny)):
        if nextnode not in cost_so_far or new_cost < cost_so_far[nextnode]:
            cost_so_far[nextnode] = new_cost
            priority = new_cost + abs(nextnode[0] - tx) + abs(nextnode[1] - ty)
            frontier.put(nextnode, priority)
            came_from[nextnode] = current

counter = 0
path = set()
while came_from[current]:
    path.add(current)
    counter += 1
    current = came_from[current]
print('Part 1:', counter)

# BFS
frontier = [start]
cost_so_far = {}
cost_so_far[start] = 0

while frontier:
    current = frontier.pop(0)
    cx, cy = current

    new_cost = cost_so_far[current] + 1
    if new_cost > 50:
        continue
    for nextnode in ((nx, ny)
                     for (nx, ny) in [(cx-1,cy),(cx+1,cy),(cx,cy-1),(cx,cy+1)]
                     if not map_pos(nx, ny)):
        if nextnode not in cost_so_far or new_cost < cost_so_far[nextnode]:
            cost_so_far[nextnode] = new_cost
            frontier.append(nextnode)

print('Part 2:', len(cost_so_far))
