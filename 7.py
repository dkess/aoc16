import itertools
import re

regex = re.compile(r'\[|\]')

def has_double(s):
    for n, a in enumerate(s[:-3]):
        b = s[n+1]
        if a != b and b == s[n+2] and a == s[n+3]:
            return True
    return False

def aba_sequences(s):
    for n, a in enumerate(s[:-2]):
        b = s[n+1]
        if a != b and a == s[n+2]:
            yield a, b

def supports_tls(s):
    ss = [has_double(x) for x in regex.split(s)]
    return any(ss[::2]) and not any(ss[1::2])

def supports_ssl(s):
    ss = [aba_sequences(x) for x in regex.split(s)]
    # character sequences outside brackets
    abas = set(itertools.chain.from_iterable(ss[::2]))
    if not abas:
        return False

    # character sequences inside brackets
    for b, a in itertools.chain.from_iterable(ss[1::2]):
        if (a, b) in abas:
            return True
    return False

puzzle_input = [s.strip() for s in open('i7.txt')]
print('Part 1:', sum(supports_tls(s) for s in puzzle_input))
print('Part 2:', sum(supports_ssl(s) for s in puzzle_input))
