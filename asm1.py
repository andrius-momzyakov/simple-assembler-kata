def simple_assembler(program):
    pointer = [0]
    regs = {}

    def mov_pointer(steps=1, pointer=pointer):
        pointer[0] += steps

    def mov(reg, val, regs=regs):
        regs[reg] = int(val)
        mov_pointer()

    def mov2(reg, reg2, regs=regs):
        regs[reg] = regs[reg2]
        mov_pointer()

    def inc(reg, regs=regs):
        regs[reg] = regs[reg] + 1
        mov_pointer()

    def dec(reg, regs=regs):
        regs[reg] -= 1
        mov_pointer()

    def jnz(reg, n, regs=regs):
        if regs.get(reg) is None:
            print('register {} not initialized. command skipped.'.format(reg))
            return -1
        else:
            if regs[reg] != 0:
                mov_pointer(steps=int(n))
                return
            mov_pointer()

    def jnz2(val, n):
        if val is None:
            print('value {} not initialized. command skipped.'.format(val))
            return -1
        else:
            val = int(val)
            if val != 0:
                mov_pointer(steps=int(n))
                return
            mov_pointer()

    def interpret(cmd):
        tokens = [
            (r'mov (?P<reg>[0-9a-z]+) (?P<val>\d+)', mov),
            (r'mov (?P<reg>[0-9a-z]+) (?P<reg2>[a-z]+)', mov2),
            (r'inc (?P<reg>[0-9a-z]+)', inc),
            (r'dec (?P<reg>[0-9a-z]+)', dec),
            (r'jnz (?P<reg>[a-z]+) (?P<n>\-?\d+)', jnz),
            (r'jnz (?P<val>\-?\d+) (?P<n>\-?\d+)', jnz2),
        ]
        import re
        for token in tokens:
            r = re.match(token[0], cmd)
            if r:
                args = r.groups()
                res = token[1](*args)
                if res == -1:
                    return False
                return True
        return False

    p_size = len(program)
    if p_size == 0:
        return regs
    while pointer[0] < p_size:
        cmd = program[pointer[0]]
        print(cmd)
        print(regs)
        res = interpret(cmd)
        if res:
            pass
        else:
            print('Invalid command. Cancelled.')
            break
        if pointer[0] == p_size:
            print('Program accomplished.')
            break
        if pointer[0] > 0 or pointer[0] < p_size:
            pass
        else:
            print('Pointer is out of program. Cancelled.')
    # return a dictionary with the registers
    return regs
