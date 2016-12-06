inp = [l.strip() for l in open('i6.txt')]

# Transpose
msg = list(map(list, zip(*inp)))

print('Part 1:', ''.join(max(set(letterlist), key=letterlist.count) for letterlist in msg))
print('Part 2:', ''.join(min(set(letterlist), key=letterlist.count) for letterlist in msg))
