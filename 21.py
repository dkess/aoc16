import re

# the left shift to undo rotate based, determined manually
ROTATEBASED_REVERSED = [1, 1, 6, 2, 7, 3, 0, 4]

p1text = 'abcdefgh'
p2text = 'fbgdceah'

swappos_re = re.compile(r'swap position (\d+) with position (\d+)')
swaplet_re = re.compile(r'swap letter (.) with letter (.)')
rotate_re = re.compile(r'rotate ([^ ]+) (\d+) step')
rotatebased_re = re.compile(r'rotate based on position of letter (.)')
reverse_re = re.compile(r'reverse positions (\d+) through (\d+)')
move_re = re.compile(r'move position (\d+) to position (\d+)')

def decode_instr(instr, reverse=False):
    m = swappos_re.match(instr)
    if m:
        x, y = map(int, m.groups())
        def swappos(text):
            a, b = text[x], text[y]
            text[x] = b
            text[y] = a
            return text
        return swappos

    m = swaplet_re.match(instr)
    if m:
        a, b = m.groups()
        def swaplet(text):
            x = text.index(a)
            y = text.index(b)
            text[x] = b
            text[y] = a
            return text
        return swaplet

    m = rotate_re.match(instr)
    if m:
        direction, val = m.groups()
        def rotate(text):
            amount = int(val) % len(text)
            if (direction == 'left') == reverse:
                amount = -amount
            text = text[amount:] + text[:amount]
            return text
        return rotate

    m = rotatebased_re.match(instr)
    if m:
        a, = m.groups()
        def rotatebased(text):
            x = text.index(a)
            if reverse:
                amount = ROTATEBASED_REVERSED[x]
            else:
                amount = 1 + x
                if x >= 4:
                    amount += 1
                amount = -(amount % len(text))
            text = text[amount:] + text[:amount]
            return text
        return rotatebased

    m = reverse_re.match(instr)
    if m:
        x, y = map(int, m.groups())
        def do_reverse(text):
            return text[:x] + list(reversed(text[x:y+1])) + text[y+1:]
        return do_reverse

    m = move_re.match(instr)
    if m:
        x, y = map(int, m.groups())
        if reverse:
            x, y = y, x
        def move(text):
            a = text.pop(x)
            text.insert(y, a)
            return text
        return move


def apply_funcs(start, instrs):
    text = list(start)
    for instr in instrs:
        text = instr(text)
    return text


instrs = [l.rstrip() for l in open('i21.txt')]
print('Part 1:', ''.join(apply_funcs(p1text,
    (decode_instr(l) for l in instrs))))

print('Part 2:', ''.join(apply_funcs(p2text,
    (decode_instr(l, reverse=True) for l in reversed(instrs)))))
