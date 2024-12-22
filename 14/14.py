import re
class Guard:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def __str__(self):
        return f'x: {self.x} y: {self.y}, dx: {self.dx} dy: {self.dy}'


def part1(guards, is_test):
    max_x = 11 if is_test else 101
    max_y = 7 if is_test else 103
    hide_x = max_x // 2
    hide_y = max_y // 2
    steps = 100
    for i in range(0, steps):
        for guard in guards:
            new_x = guard.x + guard.dx
            new_y = guard.y + guard.dy

            # Teleport x
            if new_x < 0:
                new_x = max_x + guard.dx + guard.x
            if new_x >= max_x:
                new_x = guard.dx - (max_x - guard.x)
            # Teleport y
            if new_y < 0:
                new_y = max_y + guard.dy + guard.y
            if new_y >= max_y:
                new_y = guard.dy - (max_y - guard.y)
            guard.x = new_x
            guard.y = new_y
    q1 = q2 = q3 = q4 = 0
    for guard in guards:
        if guard.x < hide_x:
            if guard.y < hide_y:
                q1 += 1
            elif guard.y > hide_y:
                q3 += 1
        elif guard.x > hide_x:
            if guard.y < hide_y:
                q2 += 1
            elif guard.y > hide_y:
                q4 += 1
    print(q1,q2,q3,q4)
    return q1*q2*q3*q4

def part2(guards, is_test):
    max_x = 11 if is_test else 101
    max_y = 7 if is_test else 103
    hide_x = max_x // 2
    hide_y = max_y // 2
    count = 100 # Set to 100 because we've already taken 100 steps
    while True:
        count += 1
        g_pos = set()
        for guard in guards:
            new_x = guard.x + guard.dx
            new_y = guard.y + guard.dy

            # Teleport x
            if new_x < 0:
                new_x = max_x + guard.dx + guard.x
            if new_x >= max_x:
                new_x = guard.dx - (max_x - guard.x)
            # Teleport y
            if new_y < 0:
                new_y = max_y + guard.dy + guard.y
            if new_y >= max_y:
                new_y = guard.dy - (max_y - guard.y)
            guard.x = new_x
            guard.y = new_y
            g_pos.add((guard.x, guard.y))
        if len(g_pos) == len(guards):
            return count, g_pos


with open('14.in') as f:
    data = f.read().split('\n')
    guards = []
    for line in data:
        # print(line)
        p,v = line.split(' ')
        p = p.split('=')[1]
        v = v.split('=')[1]
        x,y = map(int, p.split(','))
        dx,dy = map(int, v.split(','))
        guards.append(Guard(x,y,dx,dy))
        
    print('Part 1:')
    print(part1(guards, False))
    print('Part 2:')
    count, g_pos = part2(guards, False)
    print(count)
    for i in range(103):
        line = ''
        for j in range(101):
            if (j,i) in g_pos:
                line += '#'
            else:
                line += '.'
        print(line)
                