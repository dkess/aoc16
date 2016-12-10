from collections import Counter

inp = [l.strip() for l in open('i6.txt')]

# zip(*inp) transposes list of strings
counts = [Counter(s).most_common() for s in zip(*inp)]
print('Part 1:', ''.join(count[0][0] for count in counts))
print('Part 2:', ''.join(count[-1][0] for count in counts))
