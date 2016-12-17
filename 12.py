instrs = [l.strip().split() for l in open('i12.txt')]

def run_program(program, regfile):
    def read_value(x):
        try:
            y = int(x)
            return y
        except ValueError:
            return regfile[x]

    pc = 0
    while pc < len(program):
        instr = program[pc]
        pc += 1
        if instr[0] == 'cpy':
            regfile[instr[2]] = read_value(instr[1])
        elif instr[0] == 'inc':
            regfile[instr[1]] += 1
        elif instr[0] == 'dec':
            regfile[instr[1]] -= 1
        elif instr[0] == 'jnz':
            if read_value(instr[1]) != 0:
                pc += int(instr[2]) - 1

regfile_1 = {r: 0 for r in 'abcd'}
run_program(instrs, regfile_1)
print('Part 1:', regfile_1['a'])

regfile_2 = {r: 0 for r in 'abcd'}
regfile_2['c'] = 1
run_program(instrs, regfile_2)
print('Part 2:', regfile_2['a'])
