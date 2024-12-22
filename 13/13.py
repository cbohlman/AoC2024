import re

def part1(inp):
    output = 0
    for machine in inp:
        Ax, Ay = machine['A']
        Bx, By = machine['B']
        Px, Py = machine['P']
        NumB = (Px*Ay - Ax*Py) / (Bx*Ay - Ax*By)

        if not NumB.is_integer():
            continue
        NumA = (Py - By*NumB)/Ay
        if not NumA.is_integer():
            continue
        output += 3*NumA + NumB
    return output

def part2(inp):
    output = 0
    for machine in inp:
        Ax, Ay = machine['A']
        Bx, By = machine['B']
        Px, Py = machine['P']
        Px += 10000000000000
        Py += 10000000000000
        NumB = (Px*Ay - Ax*Py) / (Bx*Ay - Ax*By)

        if not NumB.is_integer():
            continue
        NumA = (Py - By*NumB)/Ay
        if not NumA.is_integer():
            continue
        output += 3*NumA + NumB
    return output




with open('13.in') as f:
    machines = f.read().split('\n\n')
    inp = []
    for machine in machines:
        tmp = {}
        A, B, prize = machine.split('\n')
        matches = re.findall('\d+', A)
        tmp['A'] = (int(matches[0]), int(matches[1]))
        matches = re.findall('\d+', B)
        tmp['B'] = (int(matches[0]), int(matches[1]))
        matches = re.findall('\d+', prize)
        tmp['P'] = (int(matches[0]), int(matches[1]))
        inp.append(tmp)
    print('Part 1:')
    print(int(part1(inp)))
    print('Part 2:')
    print(int(part2(inp)))


# 8400 * 34 - 94 * 5400 = 285600 - 507600 = -222000
# 22 * 34 - 94 * 67 = 748 - 6298 = -5550