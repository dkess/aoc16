from collections import defaultdict
import hashlib

INPUT = 'ahsbgdzn'


def has_consecutive(s, n):
    for i, x in enumerate(s[:-n+1]):
        if all(s[j] == s[i] for j in range(i+1, i+n)):
            return s[i]
    return False

def md5(x):
    return hashlib.md5(x.encode('utf-8')).hexdigest()

def run(hashfunc):
    quintuples = defaultdict(int)

    def load_quintuple(n):
        hashed = hashfunc(INPUT + str(n))
        c = has_consecutive(hashed, 5)
        if c:
            quintuples[c] = n

    for n in range(999):
        load_quintuple(n)

    n = 0
    counter = 0
    while True:
        load_quintuple(n + 999)
        hashed = hashfunc(INPUT + str(n))
        c = has_consecutive(hashed, 3)
        if c and n < quintuples[c]:
            counter += 1
            if counter == 64:
                break
        n += 1
    return n

print('Part 1:', run(md5))

def md5_2016(x):
    for n in range(2017):
        x = md5(x)
    return x
print('Part 2:', run(md5_2016))
