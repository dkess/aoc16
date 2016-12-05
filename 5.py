import hashlib

doorid = 'wtnhxymk'

pw2 = [None] * 8

positions = set()

n = 0
pw = ''
pw_done = False

while True:
    hashed = hashlib.md5((doorid + str(n)).encode('utf-8')).hexdigest()
    if hashed[:5] == '00000':
        if not pw_done:
            pw += hashed[5]
            if len(pw) == 8:
                print('Part 1:', pw)
                pw_done = True
        try:
            if not pw2[int(hashed[5])]:
                pw2[int(hashed[5])] = hashed[6]
                positions.add(int(hashed[5]))
                if len(positions) == 8:
                    break
        except KeyError:
            pass
        except IndexError:
            pass
        except ValueError:
            pass
    n += 1

print('Part 2:', ''.join(pw2))
