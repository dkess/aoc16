INPUT = '11011110011011101'

def checksum(s):
    if len(s) % 2 == 1:
        return ''.join('1' if c else '0' for c in s)
    return checksum([s[i*2] == s[i*2+1] for i in range(len(s) // 2)])


def expand(data, length):
    while len(data) < length:
        a = data
        b = [not d for d in reversed(data)]
        data = a + [0] + b
    return data[:length]

data = [c == '1' for c in INPUT]

print('Part 1:', checksum(expand(data, 272)))
print('Part 2:', checksum(expand(data, 35651584)))
