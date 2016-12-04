from collections import Counter

sum = 0

def convert_letter(c, shift):
    if c == '-':
        return ' '
    return chr((ord(c) + shift - ord('a')) % 26 + ord('a'))

for l in open('i4.txt'):
    name, p2 = l.strip().rsplit('-', 1)
    sid = int(p2[:-7])
    fullname = name
    name = name.replace('-', '')
    c = Counter(name)
    checksum = ''.join(letter for _, letter in sorted(((y, x) for x, y in c.most_common()), key=lambda z: (-z[0], z[1])))[:5]
    if p2[-6:-1] == checksum:
        dec = ''.join(map(lambda c: convert_letter(c, sid), fullname))
        if dec == 'northpole object storage':
            print('Part 2:', sid)
        sum += int(p2[:-7])

print('Part 1:', sum)

