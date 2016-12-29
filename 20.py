ALL_AMOUNT = 4294967296

# reconstruct the intervals to eliminate overlaps
# ranges is a dict where key is start and value is end
ranges = {}

for l in open('i20.txt'):
    s, e = map(int, l.rstrip().split('-'))
    
    to_delete = []
    for k, v in ranges.items():
        if k <= s <= v:
            s = v + 1
        
        if k <= e <= v:
            e = k - 1

        if s < k and e > v:
            to_delete.append(k)

    # delete ranges that are completely covered by another interval
    for d in to_delete:
        del ranges[d]

    # make sure the interval isn't already completely covered
    if e >= s:
        ranges[s] = e

smallest = 0
while smallest in ranges:
    smallest = ranges[smallest] + 1

print('Part 1:', smallest)

blocked_count = sum(v - k + 1 for k, v in ranges.items())

print('Part 2:', ALL_AMOUNT - blocked_count)
