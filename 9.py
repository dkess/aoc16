import re

raw = open('i9.txt').read().replace('\n', '')

pos = 0

regex = re.compile(r'\((\d+)x(\d+)\)')

count = len(raw)
while True:
    a  = regex.search(raw[pos:])
    if not a:
        break
    x, y = map(int, a.groups())
    count -= a.end() - a.start()
    count += x * (y - 1)
    pos += a.end() + x
print('Part 1:', count)

def decompressed_count(s):
    pos = 0
    count = 0
    while True:
        a = regex.search(s[pos:])
        if not a:
            return count + len(s) - pos
        count += a.start()
        x, y = map(int, a.groups())
        count += y * decompressed_count(s[pos+a.end():pos+a.end()+x])
        pos += a.end() + x

print('Part 2:', decompressed_count(raw))
