pointer = 0
regs = {}


def mov_pointer(steps=1):
    global pointer
    pointer += steps


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


def jnz2(val, n, regs=regs):
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


def simple_assembler(program):
    p_size = len(program)
    if p_size == 0:
        return regs
    while pointer < p_size:
        cmd = program[pointer]
        res = interpret(cmd)
        if res:
            pass
        else:
            print('Invalid command. Cancelled.')
            break
        if pointer == p_size:
            print('Program accomplished.')
            break
        if pointer > 0 or pointer < p_size:
            pass
        else:
            print('Pointer is out of program. Cancelled.')
    # return a dictionary with the registers
    return regs
