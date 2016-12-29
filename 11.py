# This is the slowest/ugliest solution I've written.  There is apparently a
# better way that does not involve a graph search, but this is what I came up
# with.  On my computer, takes 735 seconds to run with pypy3.

import heapq
from itertools import chain, combinations
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

def is_goal(floors):
    # check if every floor except top is empty
    return not any(floors[:-1])

def valid_floor(floor):
    # check if a chip will get fried on this floor
    for chip in (chip for t, chip in floor if t == 'm'):
        if ('g', chip) not in floor:
            # check if there is a different type generator that would fry chip
            if any(True for t, u in floor if t == 'g' and u != chip):
                return False
    return True

def possible_actions(current, floors):
    cfloor = floors[current]
    for items in chain(combinations(cfloor, 1), combinations(cfloor, 2)):
        # move down
        if current > 0:
            bottom = floors[current - 1].union(items)
            top = floors[current].difference(items)
            if valid_floor(bottom) and valid_floor(top):
                yield (current - 1,
                        floors[0:current - 1]
                        + (bottom, top)
                        + floors[current + 1:])

        # move up
        if current < len(floors) - 1:
            top = floors[current + 1].union(items)
            bottom = floors[current].difference(items)
            if valid_floor(bottom) and valid_floor(top):
                yield (current + 1,
                        floors[0:current]
                        + (bottom, top)
                        + floors[current + 2:])

def heuristic(state):
    # Heuristic: just move everything as fast as possible, without regard for
    # frying microchips or carrying 0 items on elevator
    counter = 0

    current, floors = state
    floors = [len(floor) for floor in floors]
    holding = 0

    while not is_goal(floors):
        # move to the lowest floor with items on it
        for n, items in enumerate(floors[:]):
            if items:
                counter += abs(n - current)
                current = n
                if holding:
                    floors[n] -= 1

                    # move to top floor
                    counter += abs(len(floors) - 1 - current)
                    current = len(floors) - 1
                else:
                    if items == 1:
                        floors[n] = 0
                        holding = 1
                    else:
                        floors[n] -= 2

                        # move to top floor
                        counter += abs(len(floors) - 1 - current)
                        current = len(floors) - 1
    return counter

def solve(startstate):
    # convert string names to ints for a speed boost
    floors = list(startstate[1])
    names = [u for t, u in chain.from_iterable(floors) if t == 'm']
    for i in range(len(floors)):
        floors[i] = frozenset((t, names.index(u)) for t, u in floors[i])
    startstate = (startstate[0], tuple(floors))
    
    # a star
    frontier = PriorityQueue()
    frontier.put(startstate, 0)
    came_from = {}
    cost_so_far = {}
    came_from[startstate] = None
    cost_so_far[startstate] = 0

    while frontier:
        current, floors = frontier.get()

        if is_goal(floors):
            break

        new_cost = cost_so_far[(current, floors)] + 1

        for nextstate in possible_actions(current, floors):
            if (nextstate not in cost_so_far
                    or new_cost < cost_so_far[nextstate]):
                cost_so_far[nextstate] = new_cost
                priority = new_cost + heuristic(nextstate)
                came_from[nextstate] = (current, floors)
                frontier.put(nextstate, priority)

    s = (current, floors)

    counter = 0
    while came_from[s]:
        counter += 1
        s = came_from[s]

    return counter

gen_re = re.compile(r'([^ ]+) generator')
mc_re = re.compile(r'([^ ]+)\-compatible microchip')

def interpret_line(line):
    generators = frozenset(('g', g) for g in gen_re.findall(line))
    microchips = frozenset(('m', m) for m in mc_re.findall(line))
    return generators.union(microchips)

floors = tuple(interpret_line(l) for l in open('i11.txt'))
starting_floor = 0

print('Part 1:', solve((starting_floor, floors)))


p2_items = frozenset((t, u)
        for t in ['g', 'm'] for u in ['elerium', 'dilithium'])
floors = (floors[0].union(p2_items),) + floors[1:]

print('Part 2:', solve((starting_floor, floors)))
